def convert_temperature(value, from_unit, to_unit):
    """Convert temperature between Celsius, Fahrenheit, and Kelvin, and show the formula step-by-step."""
    steps = []  # List to hold the formula and its simplification

    # Case where no conversion is needed
    if from_unit == to_unit:
        steps.append(f"No conversion needed: {value} {from_unit} = {value} {to_unit}")
        return value, "\n".join(steps)

    # Convert input value to Celsius
    if from_unit == "Fahrenheit":
        steps.append(f"Formula: ({value}°F − 32) × 5/9")
        value = value - 32
        steps.append(f"Step 1: Subtract 32 → ({value} × 5/9)")
        value = value * 5 / 9
        steps.append(f"Step 2: Multiply by 5/9 → {value}°C")
    elif from_unit == "Kelvin":
        steps.append(f"Formula: {value}K − 273.15")
        value = value - 273.15
        steps.append(f"Step 1: Subtract 273.15 → {value}°C")
    elif from_unit == "Celsius":
        steps.append(f"Starting with {value}°C")

    # Convert Celsius to the target unit
    if to_unit == "Fahrenheit":
        steps.append(f"Formula: ({value} × 9/5) + 32")
        intermediate = value * 9 / 5
        steps.append(f"Step 1: Multiply by 9/5 → {intermediate}")
        value = intermediate + 32
        steps.append(f"Step 2: Add 32 → {value}°F")
    elif to_unit == "Kelvin":
        steps.append(f"Formula: {value}°C + 273.15")
        value = value + 273.15
        steps.append(f"Step 1: Add 273.15 → {value}K")

    steps.append("\n") 
    steps.append(f"Final Result: {value} {to_unit}")

    # Return the final value and the steps as a string
    return value, "\n".join(steps)
