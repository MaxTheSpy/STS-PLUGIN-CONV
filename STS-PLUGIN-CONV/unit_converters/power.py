def convert_power(value, from_unit, to_unit):
    """Convert power between various units and show formula"""
    conversion_to_watts = {
        "Watt (W)": 1,
        "Kilowatt (kW)": 1000,
        "Horsepower (hp)": 745.7,
        "Foot-pound-force per second (ft·lbf/s)": 1.35582
    }

    if from_unit not in conversion_to_watts or to_unit not in conversion_to_watts:
        raise ValueError(f"Unsupported units: {from_unit} or {to_unit}")
    
    steps = []
    steps.append(f"Step 1: Convert {value} {from_unit} to watts")
    value_in_watts = value * conversion_to_watts[from_unit]
    steps.append(f"Formula: {value} × {conversion_to_watts[to_unit]} = {value_in_watts} watts")

    steps.append(f"Step 2: Convert {value_in_watts} watts to {to_unit}")
    result = value_in_watts / conversion_to_watts[to_unit]
    steps.append(f"Formula: {value_in_watts} ÷ {conversion_to_watts[to_unit]} = {result} {to_unit}\n")

    steps.append(f"Final Result: {result} {to_unit}")
    return result, "\n".join(steps)
