def convert_time(value, from_unit, to_unit):
    """Convert time between various units and show the formula."""
    # Conversion factors to seconds (base unit)
    conversion_to_seconds = {
        # Common Time Units
        "Milliseconds (ms)": 0.001,
        "Seconds (s)": 1,
        "Minutes (min)": 60,
        "Hours (hr)": 3600,
        "Days (d)": 86400,
        "Weeks (wk)": 604800,
        "Months (approx)": 2_629_746,  # 30.44 days
        "Years (yr)": 31_556_952,      # 365.25 days
        "Decades": 315_569_520,       # 10 years
        "Centuries": 3_155_695_200,   # 100 years

        # Scientific Time Units
        "Microseconds (µs)": 1e-6,
        "Nanoseconds (ns)": 1e-9,
        "Picoseconds (ps)": 1e-12
    }

    # Ensure units are valid
    if from_unit not in conversion_to_seconds or to_unit not in conversion_to_seconds:
        raise ValueError(f"Unsupported units: {from_unit} or {to_unit}")

    # Convert from the source unit to seconds
    steps = []
    steps.append(f"Step 1: Convert {value} {from_unit} to seconds")
    value_in_seconds = value * conversion_to_seconds[from_unit]
    steps.append(f"Formula: {value} × {conversion_to_seconds[from_unit]} = {value_in_seconds} seconds")

    # Convert from seconds to the target unit
    steps.append(f"Step 2: Convert {value_in_seconds} seconds to {to_unit}")
    result = value_in_seconds / conversion_to_seconds[to_unit]
    steps.append(f"Formula: {value_in_seconds} ÷ {conversion_to_seconds[to_unit]} = {result} {to_unit}\n")

    # Add the final result
    steps.append(f"Final Result: {result} {to_unit}")

    return result, "\n".join(steps)