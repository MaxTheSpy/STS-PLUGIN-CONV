def convert_pressure(value, from_unit, to_unit):
    """Convert pressure between various units and show formula"""
    conversion_to_pascals = {
        "Pascal (Pa)": 1,
        "Bar": 1e5,
        "Atmosphere (atm)": 101325,
        "Pounds Per Square Inch (psi)": 6894.76,
        "Torr": 133.322,
        "Millimeters of Mercury (mmHg)":133.322
    }

    if from_unit not in conversion_to_pascals or to_unit not in conversion_to_pascals:
        raise ValueError(f"Unsupported units: {from_unit} or {to_unit}")
    
    steps = []
    steps.append(f"Step 1: Convert {value} {from_unit} to pascals")
    value_in_pascals = value * conversion_to_pascals[from_unit]
    steps.append(f"Formula: {value} × {conversion_to_pascals[to_unit]} = {value_in_pascals} pascals")

    steps.append(f"Step 2: Convert {value_in_pascals} pascals to {to_unit}")
    result = value_in_pascals / conversion_to_pascals[to_unit]
    steps.append(f"Formula: {value_in_pascals} ÷ {conversion_to_pascals[to_unit]} = {result} {to_unit}\n")

    steps.append(f"Final Result: {result} {to_unit}")
    return result, "\n".join(steps)