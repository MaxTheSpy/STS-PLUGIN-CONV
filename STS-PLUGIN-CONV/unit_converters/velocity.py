def convert_velocity(value, from_unit, to_unit):
    """Convert velocity between various units and show the formula."""
    conversion_to_mps = {
        "Meters per second (m/s)": 1,
        "Kilometers per hour (km/h)": 0.277778,
        "Miles per hour (mph)": 0.44704,
        "Knots": 0.514444,
        "Mach": 343
    }

    if from_unit not in conversion_to_mps or to_unit not in conversion_to_mps:
        raise ValueError(f"Unsupported units: {from_unit} or {to_unit}")

    steps = []
    steps.append(f"Step 1: Convert {value} {from_unit} to meters per second")
    value_in_mps = value * conversion_to_mps[from_unit]
    steps.append(f"Formula: {value} × {conversion_to_mps[from_unit]} = {value_in_mps} m/s")

    steps.append(f"Step 2: Convert {value_in_mps} meters per second to {to_unit}")
    result = value_in_mps / conversion_to_mps[to_unit]
    steps.append(f"Formula: {value_in_mps} ÷ {conversion_to_mps[to_unit]} = {result} {to_unit}\n")

    steps.append(f"Final Result: {result} {to_unit}")

    return result, "\n".join(steps)