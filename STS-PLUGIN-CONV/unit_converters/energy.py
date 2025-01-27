def convert_energy(value, from_unit, to_unit):
    """Convert energy between various units and show formula"""
    conversion_to_joules = {
        "Joule (J)": 1,
        "Kilojoule (kJ)": 1000,
        "Calorie (cal)": 4.184,
        "Kilocalorie (kcal)": 4184,
        "Watt-hour (Wh)" : 3600,
        "Kilowatt-hour (kWh)": 3.6e6,
        "Electronvolt (eV)": 1.60218e-19,
        "British Thermal Unit (BTU)": 1055.06,
        "Therm":1.05506e8,
    }
    if from_unit not in conversion_to_joules or to_unit not in conversion_to_joules:
        raise ValueError(f"Unsupported Units: {from_unit} or {to_unit}")
    
    steps = []
    steps.append(f"step 1: convert {value}{from_unit} to joules")
    value_in_joules = value * conversion_to_joules[from_unit]
    steps.append(f"Formula: {value} × {conversion_to_joules[from_unit]} = {value_in_joules} joules")

    steps.append(f"Step 2: convert {value_in_joules} joules to {to_unit}")
    result = value_in_joules / conversion_to_joules[to_unit]
    steps.append(f"Formua: {value_in_joules} ÷ {conversion_to_joules[to_unit]} = {result} {to_unit}\n")

    steps.append(f"Final Result: {result} {to_unit}")
    
    return result, "\n".join(steps)
