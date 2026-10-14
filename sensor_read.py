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