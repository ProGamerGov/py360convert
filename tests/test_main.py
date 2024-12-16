import numpy as np
import pytest

import py360convert

AVG_DIFF_THRESH = 1.2


def diff(x, y):
    return np.abs(x.astype(float) - y.astype(float))


def test_c2e_dice(equirec_image, dice_image):
    equirec_actual = py360convert.c2e(dice_image, 512, 1024)
    equirec_diff = diff(equirec_image, equirec_actual)
    assert equirec_diff.mean() < AVG_DIFF_THRESH


def test_c2e_horizon(equirec_image, horizon_image):
    equirec_actual = py360convert.c2e(horizon_image, 512, 1024, cube_format="horizon")
    equirec_diff = diff(equirec_image, equirec_actual)
    assert equirec_diff.mean() < AVG_DIFF_THRESH


def test_c2e_dict(equirec_image, dict_image):
    equirec_actual = py360convert.c2e(dict_image, 512, 1024, cube_format="dict")
    equirec_diff = diff(equirec_image, equirec_actual)
    assert equirec_diff.mean() < AVG_DIFF_THRESH


def test_c2e_list(equirec_image, list_image):
    equirec_actual = py360convert.c2e(list_image, 512, 1024, cube_format="list")
    equirec_diff = diff(equirec_image, equirec_actual)
    assert equirec_diff.mean() < AVG_DIFF_THRESH


def test_e2c_dice(equirec_image, dice_image):
    dice_actual = py360convert.e2c(equirec_image, cube_format="dice")
    dice_diff = diff(dice_image, dice_actual)
    assert dice_diff.mean() < AVG_DIFF_THRESH


def test_e2c_horizon(equirec_image, horizon_image):
    horizon_actual = py360convert.e2c(equirec_image, 256, cube_format="horizon")
    horizon_diff = diff(horizon_image, horizon_actual)
    assert horizon_diff.mean() < AVG_DIFF_THRESH


def test_e2c_dict(equirec_image, dict_image):
    dict_actual = py360convert.e2c(equirec_image, 256, cube_format="dict")
    dict_diff = {k: diff(dict_image[k], dict_actual[k]) for k in "FRBLUD"}

    assert dict_diff["F"].mean() < AVG_DIFF_THRESH
    assert dict_diff["R"].mean() < AVG_DIFF_THRESH
    assert dict_diff["B"].mean() < AVG_DIFF_THRESH
    assert dict_diff["L"].mean() < AVG_DIFF_THRESH
    assert dict_diff["U"].mean() < AVG_DIFF_THRESH
    assert dict_diff["D"].mean() < AVG_DIFF_THRESH


def test_e2c_list(equirec_image, list_image):
    list_actual = py360convert.e2c(equirec_image, 256, cube_format="list")
    list_diff = [diff(list_image[i], list_actual[i]) for i in range(6)]

    assert list_diff[0].mean() < AVG_DIFF_THRESH
    assert list_diff[1].mean() < AVG_DIFF_THRESH
    assert list_diff[2].mean() < AVG_DIFF_THRESH
    assert list_diff[3].mean() < AVG_DIFF_THRESH
    assert list_diff[4].mean() < AVG_DIFF_THRESH
    assert list_diff[5].mean() < AVG_DIFF_THRESH