# Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.

import itertools

from fvcore.common.benchmark import benchmark
from pytorch3d.renderer import AbsorptionOnlyRaymarcher, EmissionAbsorptionRaymarcher
from test_raymarching import TestRaymarching


def bm_raymarching() -> None:
    case_grid = {
        "raymarcher_type": [EmissionAbsorptionRaymarcher, AbsorptionOnlyRaymarcher],
        "n_rays": [10, 1000, 10000],
        "n_pts_per_ray": [10, 1000, 10000],
    }
    test_cases = itertools.product(*case_grid.values())
    kwargs_list = [dict(zip(case_grid.keys(), case)) for case in test_cases]

    benchmark(TestRaymarching.raymarcher, "RAYMARCHER", kwargs_list, warmup_iters=1)
