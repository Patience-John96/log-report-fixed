import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def _load_report():
    """Load /app/report.json as a JSON object (shared precondition for every criterion)."""
    assert REPORT_PATH.exists(), "no /app/report.json found"
    with open(REPORT_PATH) as f:
        data = json.load(f)
    assert isinstance(data, dict), "report.json must contain a JSON object"
    return data


def test_total_requests_correct():
    """instruction.md criterion 1 -- "total_requests": integer, the total number of
    log lines (requests) in the file. access.log has 6 requests."""
    data = _load_report()
    assert data.get("total_requests") == 6, f"expected 6, got {data.get('total_requests')}"


def test_unique_ips_correct():
    """instruction.md criterion 2 -- "unique_ips": integer, the count of distinct client
    IP addresses that made requests. access.log has 3 distinct IPs."""
    data = _load_report()
    assert data.get("unique_ips") == 3, f"expected 3, got {data.get('unique_ips')}"


def test_top_path_correct():
    """instruction.md criterion 3 -- "top_path": string, the request path that appears
    most often (ties -> first in the log). access.log top_path is /index.html (3 hits)."""
    data = _load_report()
    assert data.get("top_path") == "/index.html", f"expected /index.html, got {data.get('top_path')}"
