def convert_length(value, from_unit, to_unit):
    """Converts length units (cm, m, km)."""
    conversion_factors = {
        'm': 1,        # Meter is the base unit
        'km': 0.001,   # Kilometer to meter
        'cm': 0.01     # Centimeter to meter (corrected to 0.01 instead of 100)
    }
    
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Unrecognized length units. Use 'cm', 'm', or 'km'.")
    
    value_in_meters = value * conversion_factors[from_unit]
    converted_value = value_in_meters / conversion_factors[to_unit]
    
    # Round the result to 2 decimal places
    return round(converted_value, 2)

def convert_weight(value, from_unit, to_unit):
    """Converts weight units (g, kg, lb)."""
    conversion_factors = {
        'g': 1,        # Gram is the base unit
        'kg': 0.001,   # Kilogram to gram
        'lb': 0.00220462 # Pound to gram
    }
    
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Unrecognized weight units. Use 'g', 'kg', or 'lb'.")
    
    value_in_grams = value * conversion_factors[from_unit]
    converted_value = value_in_grams / conversion_factors[to_unit]
    
    # Round the result to 2 decimal places
    return round(converted_value, 2)

def convert_temperature(value, from_unit, to_unit):
    """Converts temperature units (Celsius, Fahrenheit, Kelvin)."""
    if from_unit == 'C' and to_unit == 'F':
        return round((value * 9/5) + 32, 2)
    elif from_unit == 'C' and to_unit == 'K':
        return round(value + 273.15, 2)
    elif from_unit == 'F' and to_unit == 'C':
        return round((value - 32) * 5/9, 2)
    elif from_unit == 'F' and to_unit == 'K':
        return round((value - 32) * 5/9 + 273.15, 2)
    elif from_unit == 'K' and to_unit == 'C':
        return round(value - 273.15, 2)
    elif from_unit == 'K' and to_unit == 'F':
        return round((value - 273.15) * 9/5 + 32, 2)
    else:
        raise ValueError("Temperature conversion not supported.")

def main():
    print("Welcome to the Unit Converter!")
    
    while True:
        print("\nConversion options:")
        print("1. Convert length (cm, m, km)")
        print("2. Convert weight (g, kg, lb)")
        print("3. Convert temperature (Celsius, Fahrenheit, Kelvin)")
        print("4. Quit")
        
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            value = float(input("Enter the value to convert: "))
            from_unit = input("Enter the source unit (cm, m, km): ")
            to_unit = input("Enter the target unit (cm, m, km): ")
            try:
                result = convert_length(value, from_unit, to_unit)
                print(f"{value} {from_unit} is equal to {result} {to_unit}.")
            except ValueError as e:
                print(e)

        elif choice == "2":
            value = float(input("Enter the value to convert: "))
            from_unit = input("Enter the source unit (g, kg, lb): ")
            to_unit = input("Enter the target unit (g, kg, lb): ")
            try:
                result = convert_weight(value, from_unit, to_unit)
                print(f"{value} {from_unit} is equal to {result} {to_unit}.")
            except ValueError as e:
                print(e)

        elif choice == "3":
            value = float(input("Enter the value to convert: "))
            from_unit = input("Enter the source unit (C, F, K): ")
            to_unit = input("Enter the target unit (C, F, K): ")
            try:
                result = convert_temperature(value, from_unit, to_unit)
                print(f"{value} {from_unit} is equal to {result} {to_unit}.")
            except ValueError as e:
                print(e)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
