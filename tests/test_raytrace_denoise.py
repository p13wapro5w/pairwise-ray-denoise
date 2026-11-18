import pytest
from render import raytrace_denoise as mod

CASES = [
    ("spatial_near", "m.spatial_weight(0.0) == approx(1.0)"),
    ("spatial_far", "m.spatial_weight(1.0) == approx(0.5)"),
    ("temporal_half", "m.temporal_alpha(10, 20) == approx(0.5)"),
    ("temporal_full", "m.temporal_alpha(20, 20) == approx(1.0)"),
    ("guide_perfect", "m.guide_weight(0.0, 0.0) == approx(1.0)"),
    ("guide_diff", "m.guide_weight(1.0, 1.0) < 1.0"),
    ("ray_zero", "m.ray_length_weight(0.0) == approx(1.0)"),
    ("highlight_keep", "m.protect_highlight(10.0, 5.0) == approx(10.0)"),
    ("highlight_low", "m.protect_highlight(2.0, 5.0) == approx(2.0)"),
    ("reset_true", "m.reset_on_motion(True) is True"),
    ("upsample_same", "m.upsample_reflection(1.0, 1.0) == approx(1.0)"),
    ("upsample_diff", "m.upsample_reflection(1.0, 2.0) == approx(0.5)"),
    ("samples_low", "m.adaptive_samples(0.5) == 8"),
    ("samples_high", "m.adaptive_samples(1.0) == 16"),
    ("linear_one", "m.linear_space(1.0) == approx(1.0)")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
