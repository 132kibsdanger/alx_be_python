global FAHRENHEIT_TO_CELSIUS_FACTOR
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
global CELSIUS_TO_FAHRENHEIT_FACTOR
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):

    """
    Convert Fahrenheit to Celsius.
    
    :param fahrenheit: Temperature in Fahrenheit
    :return: Temperature in Celsius
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.

    :param celsius: Temperature in Celsius
    :return: Temperature in Fahrenheit
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temp_to_convert = float(input("Enter the temperature to convert: "))
    conversion_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if conversion_type.upper() == 'C':
        converted_temp = convert_to_fahrenheit(temp_to_convert)
        print(f"{temp_to_convert}°C is {converted_temp}°F")
    elif conversion_type.upper() == 'F':
        converted_temp = convert_to_celsius(temp_to_convert)
        print(f"{temp_to_convert}°F is {converted_temp}°C")
    else:
        print("Kindly input valid temperature")


if __name__ == "__main__":
    main()

