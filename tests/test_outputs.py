import json
from pathlib import Path
REPORT = Path("/app/report.json")
def load():
    """Load the generated report."""
    assert REPORT.exists(), "report.json not found"
    return json.loads(REPORT.read_text())
def test_report_exists():
    """Success Criterion 1: Create /app/report.json."""
    assert REPORT.exists()
def test_total_requests():
    """Success Criterion 2: total_requests equals 6."""
    assert load()["total_requests"] == 6
def test_unique_ips():
    """Success Criterion 3: unique_ips equals 3."""
    assert load()["unique_ips"] == 3
def test_top_path():
    """Success Criterion 4: top_path equals '/index.html'."""
    assert load()["top_path"] == "/index.html"