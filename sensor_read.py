from sensor_read import check_temperature, read_sensor

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