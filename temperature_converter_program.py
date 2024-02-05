def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67

def main():
    print("Temperature Converter")
    print("Available Scales: Celsius, Fahrenheit, Kelvin")
    
    while True:
        try:
            temperature = float(input("Enter temperature value: "))
            original_scale = input("Enter original unit of measurement (Celsius, Fahrenheit, Kelvin): ").lower()

            if original_scale == 'celsius':
                fahrenheit = celsius_to_fahrenheit(temperature)
                kelvin = celsius_to_kelvin(temperature)
                print(f"{temperature} Celsius is equal to {fahrenheit} Fahrenheit and {kelvin} Kelvin")
            elif original_scale == 'fahrenheit':
                celsius = fahrenheit_to_celsius(temperature)
                kelvin = fahrenheit_to_kelvin(temperature)
                print(f"{temperature} Fahrenheit is equal to {celsius} Celsius and {kelvin} Kelvin")
            elif original_scale == 'kelvin':
                celsius = kelvin_to_celsius(temperature)
                fahrenheit = kelvin_to_fahrenheit(temperature)
                print(f"{temperature} Kelvin is equal to {celsius} Celsius and {fahrenheit} Fahrenheit")
            else:
                print("Invalid input! Please enter either Celsius, Fahrenheit, or Kelvin.")
                continue

            break  # Exit loop if input is valid and conversion is done
        except ValueError:
            print("Invalid input! Please enter a valid temperature value.")
            continue

if __name__ == "__main__":
    main()
