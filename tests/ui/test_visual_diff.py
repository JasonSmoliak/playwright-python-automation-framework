from pathlib import Path

import pytest
from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch

pytestmark = [pytest.mark.ui, pytest.mark.visual]

def test_visual_diff_against_baseline(page):
    baseline_path = Path("visual_baselines/welcome_page.png")
    actual_path = Path("visual_actual/welcome_page.png")
    diff_path = Path("visual_diffs/welcome_page_diff.png")

    actual_path.parent.mkdir(exist_ok=True)
    diff_path.parent.mkdir(exist_ok=True)
    baseline_path.parent.mkdir(exist_ok=True)

    page.set_viewport_size({"width": 800, "height": 600})

    page.set_content("""
    <html>
      <body style="font-family: Arial; padding: 40px;">
        <h1>Welcome</h1>
        <p>This is a visual regression test.</p>
        <button style="padding: 10px 16px;">Click Me</button>
      </body>
    </html>
    """)

    page.screenshot(path=str(actual_path), full_page=True)

    if not baseline_path.exists():
        actual_path.replace(baseline_path)
        pytest.fail(
            f"Baseline screenshot created at {baseline_path}. "
            "Re-run the test to compare against it."
        )

    baseline = Image.open(baseline_path).convert("RGBA")
    actual = Image.open(actual_path).convert("RGBA")

    diff = Image.new("RGBA", baseline.size)

    mismatched_pixels = pixelmatch(
        baseline,
        actual,
        diff,
        threshold=0.1,
    )

    if mismatched_pixels > 0:
        diff.save(diff_path)

    assert mismatched_pixels == 0, (
        f"Visual diff found: {mismatched_pixels} pixels differ. "
        f"Diff saved to {diff_path}"
    )
