import json
from pathlib import Path

import pytest

import page


def test_version():
    assert page.__version__ == "0.4.1"


def test_default_safety_limits():
    limits = page.SafetyLimits()

    assert limits.max_input_size == page.SafetyLimits.DEFAULT_MAX_INPUT_SIZE
    assert limits.max_decoded_stream_size == 32 * 1024 * 1024
    assert limits.max_object_count == 1_000_000
    assert limits.max_reference_depth == 256


def test_custom_safety_limits():
    limits = page.SafetyLimits(max_input_size=42, max_reference_depth=7)

    assert limits.max_input_size == 42
    assert limits.max_reference_depth == 7


def test_explicit_profile_returns_parser_report_for_invalid_bytes():
    report = page.validate_bytes_with_profile(
        b"not a PDF", page.ValidationProfile.PDF_A_1B
    )

    assert report.profile == page.ValidationProfile.PDF_A_1B
    assert report.checks_passed is False
    assert report.checks.failed == 1
    assert report.failures[0].category == page.FailureCategory.PARSER
    assert report.exit_code() == 2
    assert "PDF-PARSE-001" in str(report)


def test_report_exports_stable_json():
    report = page.validate_bytes_with_profile(
        b"not a PDF", page.ValidationProfile.PDF_A_1B
    )

    exported = json.loads(report.to_json())

    assert exported == {
        "profile": "a-1b",
        "valid": False,
        "failures": [],
        "error": {
            "kind": "parser",
            "rule": "PDF-PARSE-001",
            "message": report.failures[0].message,
        },
    }


def test_inferred_profile_raises_for_invalid_bytes():
    with pytest.raises(page.ValidationError):
        page.validate_bytes(b"not a PDF")


def test_explicit_profile_reports_missing_file(tmp_path: Path):
    missing_file = tmp_path / "missing.pdf"
    report = page.validate_file_with_profile(
        missing_file, page.ValidationProfile.PDF_A_1B
    )

    assert report.has_operational_failure() is True
    assert report.failures[0].category == page.FailureCategory.OPERATIONAL
    assert report.exit_code() == 1
    assert json.loads(report.to_json())["file"] == str(missing_file)
