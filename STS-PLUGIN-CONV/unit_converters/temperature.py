def convert_temperature(value, from_unit, to_unit):
    """Convert temperature between Celsius (°C), Fahrenheit (°F), Kelvin (K), Rankine (°R), Delisle (°De), Newton (°N), Réaumur (°Re), and Rømer (°Rø), and show the formula step-by-step."""
    steps = []  # List to hold the formula and its simplification

    # Case where no conversion is needed
    if from_unit == to_unit:
        steps.append(f"No conversion needed: {value} {from_unit} = {value} {to_unit}")
        return value, "\n".join(steps)

    # Convert input value to Celsius (°C)
    if from_unit == "Fahrenheit (°F)":
        steps.append(f"Formula: ({value}°F − 32) × 5/9")
        value = (value - 32) * 5 / 9
        steps.append(f"Result: {value}°C")
    elif from_unit == "Kelvin (K)":
        steps.append(f"Formula: {value}K − 273.15")
        value = value - 273.15
        steps.append(f"Result: {value}°C")
    elif from_unit == "Rankine (°R)":
        steps.append(f"Formula: ({value}°R − 491.67) × 5/9")
        value = (value - 491.67) * 5 / 9
        steps.append(f"Result: {value}°C")
    elif from_unit == "Delisle (°De)":
        steps.append(f"Formula: 100 − ({value}°De × 2/3)")
        value = 100 - (value * 2 / 3)
        steps.append(f"Result: {value}°C")
    elif from_unit == "Newton (°N)":
        steps.append(f"Formula: {value}°N × 100/33")
        value = value * 100 / 33
        steps.append(f"Result: {value}°C")
    elif from_unit == "Réaumur (°Re)":
        steps.append(f"Formula: {value}°Re × 5/4")
        value = value * 5 / 4
        steps.append(f"Result: {value}°C")
    elif from_unit == "Rømer (°Rø)":
        steps.append(f"Formula: ({value}°Rø − 7.5) × 40/21")
        value = (value - 7.5) * 40 / 21
        steps.append(f"Result: {value}°C")
    elif from_unit == "Celsius (°C)":
        steps.append(f"Starting with {value}°C")

    # Convert Celsius (°C) to the target unit
    if to_unit == "Fahrenheit (°F)":
        steps.append(f"Formula: ({value} × 9/5) + 32")
        value = (value * 9 / 5) + 32
        steps.append(f"Result: {value}°F")
    elif to_unit == "Kelvin (K)":
        steps.append(f"Formula: {value}°C + 273.15")
        value = value + 273.15
        steps.append(f"Result: {value}K")
    elif to_unit == "Rankine (°R)":
        steps.append(f"Formula: ({value}°C × 9/5) + 491.67")
        value = (value * 9 / 5) + 491.67
        steps.append(f"Result: {value}°R")
    elif to_unit == "Delisle (°De)":
        steps.append(f"Formula: (100 − {value}°C) × 3/2")
        value = (100 - value) * 3 / 2
        steps.append(f"Result: {value}°De")
    elif to_unit == "Newton (°N)":
        steps.append(f"Formula: {value}°C × 33/100")
        value = value * 33 / 100
        steps.append(f"Result: {value}°N")
    elif to_unit == "Réaumur (°Re)":
        steps.append(f"Formula: {value}°C × 4/5")
        value = value * 4 / 5
        steps.append(f"Result: {value}°Re")
    elif to_unit == "Rømer (°Rø)":
        steps.append(f"Formula: ({value}°C × 21/40) + 7.5")
        value = (value * 21 / 40) + 7.5
        steps.append(f"Result: {value}°Rø")

    steps.append("\n") 
    steps.append(f"Final Result: {value} {to_unit}")

    # Return the final value and the steps as a string
    return value, "\n".join(steps)
