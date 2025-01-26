def convert_distance(value, from_unit, to_unit):
    """Convert distance between various units and show the formula."""
    # Conversion factors to meters
    conversion_to_meters = {
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.344,
        "nautical mile": 1852,
        "centimeter": 0.01,
        "meter": 1,
        "kilometer": 1000,
        "nanometer": 1e-9,
        "micrometer": 1e-6,
        "league": 4828.032,
        "chain": 20.1168,
        "rod": 5.0292,
        "cubit": 0.4572,
        "furlong": 201.168,
    }

    # Ensure units are valid
    if from_unit not in conversion_to_meters or to_unit not in conversion_to_meters:
        raise ValueError(f"Unsupported units: {from_unit} or {to_unit}")

    # Convert from the source unit to meters
    steps = []
    steps.append(f"Step 1: Convert {value} {from_unit} to meters")
    value_in_meters = value * conversion_to_meters[from_unit]
    steps.append(f"Formula: {value} × {conversion_to_meters[from_unit]} = {value_in_meters} meters")

    # Convert from meters to the target unit
    steps.append(f"Step 2: Convert {value_in_meters} meters to {to_unit}")
    result = value_in_meters / conversion_to_meters[to_unit]
    steps.append(f"Formula: {value_in_meters} ÷ {conversion_to_meters[to_unit]} = {result} {to_unit}\n")

    # Add the final result
    steps.append(f"Final Result: {result} {to_unit}")

    return result, "\n".join(steps)
