def test_read_sensor_returns_a_number():
    assert isinstance(read_sensor(101), (int, float))


def test_read_sensor_is_deterministic():
@pytest.mark.parametrize("temperature", [0, 25.5, 80])

@pytest.mark.parametrize("temperature", [80.1, 100, 1000])
def test_check_temperature_high(temperature):
    assert check_temperature(temperature) == "LOW"
    assert check_temperature(read_sensor(101)) == "NORMAL"