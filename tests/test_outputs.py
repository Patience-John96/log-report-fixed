import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def _load_report():
    assert REPORT_PATH.exists(), "no /app/report.json found"
    with open(REPORT_PATH) as f:
        return json.load(f)


def test_report_is_valid_json():
    """The agent produced a well-formed JSON report at /app/report.json."""
    data = _load_report()
    assert isinstance(data, dict), "report.json must contain a JSON object"


def test_report_has_required_keys():
    """The report contains exactly the three required keys."""
    data = _load_report()
    required = {"total_requests", "unique_ips", "top_path"}
    assert required.issubset(data.keys()), f"missing keys: {required - data.keys()}"


def test_total_requests_correct():
    """total_requests exactly matches the number of log lines in access.log."""
    data = _load_report()
    assert data.get("total_requests") == 6, f"expected 6, got {data.get('total_requests')}"


def test_unique_ips_correct():
    """unique_ips exactly matches the count of distinct client IPs in access.log."""
    data = _load_report()
    assert data.get("unique_ips") == 3, f"expected 3, got {data.get('unique_ips')}"


def test_top_path_correct():
    """top_path is the most-requested path in access.log (/index.html, 3 hits)."""
    data = _load_report()
    assert data.get("top_path") == "/index.html", f"expected /index.html, got {data.get('top_path')}"
