# py-page

Python bindings for [`page`](https://crates.io/crates/page_validation), a PDF/A and PDF/UA validator.

<br>

## Validate a PDF

```python
import page

report = page.validate_file("document.pdf")
print(report)

if not report.checks_passed:
    for failure in report.failures:
        print(f"[{failure.rule_id}] {failure.message}")
```

`validate_file()` and `validate_bytes()` infer the PDF/A or PDF/UA profile from the document's XMP metadata. They raise `page.ValidationError` when the profile declaration is missing, malformed, or unsupported, or when the input cannot be read or parsed.

To select the profile yourself, use the explicit-profile variant:

```python
import page

report = page.validate_file_with_profile(
    "document.pdf",
    page.ValidationProfile.PDF_A_1B,
)
```

The explicit-profile functions always return a `ValidationReport`. Parser, operational, and conformance problems are represented in `report.failures`.

You can export the results as JSON with:

```python
with open("report.json", "w") as f:
    f.write(report.to_json())
```

<br>

## Configure safety limits

All validation functions accept an optional `SafetyLimits` instance:

```python
limits = page.SafetyLimits(
    max_input_size=100 * 1024 * 1024,
    max_decoded_stream_size=32 * 1024 * 1024,
    max_object_count=500_000,
    max_reference_depth=128,
)

report = page.validate_file("document.pdf", limits)
```
