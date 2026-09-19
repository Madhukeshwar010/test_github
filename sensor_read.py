from sensor_read import check_temperature, read_sensor
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

def test_read_sensor():
    assert read_sensor(101) == 25.5

def test_normal():
    assert check_temperature(25.5) == "NORMAL"

def test_high():
    assert check_temperature(100) == "HIGH"

def test_low():
    assert check_temperature(-10) == "LOW"
    
def read_sensor(sensor_id):
    """Simulate reading a sensor value."""
    return 25.5


def check_temperature(temperature):
    """Check whether the temperature is within the safe range."""
    if temperature > 80:
        return "HIGH"
    elif temperature < 0:
        return "LOW"
    return "NORMAL"


def main():
    sensor_id = 101
    temperature = read_sensor(sensor_id)

    status = check_temperature(temperature)

    print(f"Sensor ID: {sensor_id}")
    print(f"Temperature: {temperature} °C")
    print(f"Status: {status}")


if __name__ == "__main__":
    main()