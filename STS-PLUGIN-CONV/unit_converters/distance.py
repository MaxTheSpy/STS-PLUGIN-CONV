def convert_distance(value, from_unit, to_unit):
    """Convert distance between various units and show the formula."""
    # Conversion factors to meters
    conversion_to_meters = {
        "Foot (ft)": 0.3048,
        "Yard (yd)": 0.9144,
        "Mile (mi)": 1609.344,
        "Nautical Mile (NM)": 1852,
        "Centimeter (cm)": 0.01,
        "Meter (m)": 1,
        "kilometer (km)": 1000,
        "Nanometer (nm)": 1e-9,
        "Micrometer (µm)": 1e-6,
        "League (lea)": 4828.032,
        "Chain (ch)": 20.1168,
        "Rod (rd)": 5.0292,
        "Cubit (cbt)": 0.4572,
        "furlong (fur)": 201.168,
        "Inch (in)": 0.0254,
        "Astronomical Unit (AU)": 149597870700,
        "Light-Year (ly)": 9.4607e15,
        "Parsec (pc)": 3.0857e16,
        "Planck Length (lP)": 1.616255e-35,
        "Fathom (fath)": 1.8288,
        "Hand (hand)": 0.1016,
        "Perch (perch)": 5.0292,  # Same as Rod
        "Palm (palm)": 0.0762,
        "Barleycorn (barleycorn)": 0.00847,
        "Ell (ell)": 1.143,
        "Span (span)": 0.2286,
        "Step (step)": 0.762,
        "Smoot (sm)": 1.7018,
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
