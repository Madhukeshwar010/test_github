"""Unit tests for sensor_read."""

import pytest

from sensor_read import check_temperature, read_sensor


def test_read_sensor_returns_a_number():
    assert isinstance(read_sensor(101), (int, float))


def test_read_sensor_is_deterministic():
    assert read_sensor(101) == read_sensor(101)


@pytest.mark.parametrize("temperature", [0, 25.5, 80])
def test_check_temperature_normal_range(temperature):
    assert check_temperature(temperature) == "NORMAL"


@pytest.mark.parametrize("temperature", [80.1, 100, 1000])
def test_check_temperature_high(temperature):
    assert check_temperature(temperature) == "HIGH"


@pytest.mark.parametrize("temperature", [-0.1, -10, -273])
def test_check_temperature_low(temperature):
    assert check_temperature(temperature) == "LOW"


def test_default_sensor_reading_is_normal():
    assert check_temperature(read_sensor(101)) == "NORMAL"