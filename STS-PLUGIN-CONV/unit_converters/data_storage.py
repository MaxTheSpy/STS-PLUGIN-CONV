def convert_data_storage(value, from_unit, to_unit):
    """Convert data storage between various units and show the formula."""
    conversion_to_bytes = {
        "Bit": 1 / 8,
        "Byte (B)": 1,
        "Kilobyte (KB)": 1024,
        "Megabyte (MB)": 1024**2,
        "Gigabyte (GB)": 1024**3,
        "Terabyte (TB)": 1024**4,
        "Petabyte (PB)": 1024**5,
        "Exabyte (EB)": 1024**6,
        "Zettabyte (ZB)": 1024**7,
        "Yottabyte (YB)": 1024**8
    }

    if from_unit not in conversion_to_bytes or to_unit not in conversion_to_bytes:
        raise ValueError(f"Unsupported units: {from_unit} or {to_unit}")

    steps = []
    steps.append(f"Step 1: Convert {value} {from_unit} to bytes")
    value_in_bytes = value * conversion_to_bytes[from_unit]
    steps.append(f"Formula: {value} × {conversion_to_bytes[from_unit]} = {value_in_bytes} bytes")

    steps.append(f"Step 2: Convert {value_in_bytes} bytes to {to_unit}")
    result = value_in_bytes / conversion_to_bytes[to_unit]
    steps.append(f"Formula: {value_in_bytes} ÷ {conversion_to_bytes[to_unit]} = {result} {to_unit}\n")

    steps.append(f"Final Result: {result} {to_unit}")

    return result, "\n".join(steps)