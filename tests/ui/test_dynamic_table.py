import pytest

pytestmark = [pytest.mark.ui, pytest.mark.flaky(reruns=2, reruns_delay=1)]

def test_chrome_cpu_matches_label(dynamic_table_page):
    dynamic_table_page.load()
    dynamic_table_page.verify_chrome_cpu_matches_label()
