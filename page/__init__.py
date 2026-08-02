"""Python bindings for the ``page_validation`` Rust crate."""

from ._page import (
    FailureCategory,
    PdfDocument,
    PdfObjectId,
    SafetyLimits,
    ValidationCounts,
    ValidationError,
    ValidationFailure,
    ValidationProfile,
    ValidationReport,
    validate_bytes,
    validate_bytes_with_profile,
    validate_file,
    validate_file_with_profile,
)

__version__ = "0.0.1"

__all__ = [
    "FailureCategory",
    "PdfDocument",
    "PdfObjectId",
    "SafetyLimits",
    "ValidationCounts",
    "ValidationError",
    "ValidationFailure",
    "ValidationProfile",
    "ValidationReport",
    "validate_bytes",
    "validate_bytes_with_profile",
    "validate_file",
    "validate_file_with_profile",
]
