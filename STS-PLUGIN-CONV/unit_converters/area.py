def convert_area(value, from_unit, to_unit):
    """Convert area between various units and show the formula."""
    conversion_to_sq_meters = {
        "Square Meter (m²)": 1,
        "Square Kilometer (km²)": 1e6,
        "Square Foot (ft²)": 0.092903,
        "Square Yard (yd²)": 0.836127,
        "Acre": 4046.86,
        "Hectare": 1e4,
        "Square Mile (mi²)": 2.59e6,
        "Square Inch (in²)": 0.00064516
    }

    if from_unit not in conversion_to_sq_meters or to_unit not in conversion_to_sq_meters:
        raise ValueError(f"Unsupported units: {from_unit} or {to_unit}")

    steps = []
    steps.append(f"Step 1: Convert {value} {from_unit} to square meters")
    value_in_sq_meters = value * conversion_to_sq_meters[from_unit]
    steps.append(f"Formula: {value} × {conversion_to_sq_meters[from_unit]} = {value_in_sq_meters} m²")

    steps.append(f"Step 2: Convert {value_in_sq_meters} square meters to {to_unit}")
    result = value_in_sq_meters / conversion_to_sq_meters[to_unit]
    steps.append(f"Formula: {value_in_sq_meters} ÷ {conversion_to_sq_meters[to_unit]} = {result} {to_unit}\n")

    steps.append(f"Final Result: {result} {to_unit}")

    return result, "\n".join(steps)