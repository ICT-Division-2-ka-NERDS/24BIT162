class Weather:
    def _init_(self, parameters):
        self.parameters = parameters  # A list of weather parameters (e.g., temperature, humidity, etc.)

    def _contains_(self, item):
        # Overloading the in operator to check if item exists in parameters list
        return item in self.parameters

# Example usage:
weather = Weather(['temperature', 'humidity', 'pressure', 'wind_speed', 'rain'])

# Checking if certain parameters are in the weather list
if 'temperature' in weather:
    print("Temperature is present in the weather parameters.")
else:
    print("Temperature is not present in the weather parameters.")

if 'sunlight' in weather:
    print("Sunlight is present in the weather parameters.")
else:
    print("Sunlight is not present in the weather parameters.")
