def convert_fluids(value, from_unit, to_unit):
    """Convert fluid volumes between various units and show the formula."""
    # Conversion factors to liters (base unit)
    conversion_to_liters = {
        # Metric Units
        "Milliliter (mL)": 0.001,
        "Centiliter (cL)": 0.01,
        "Deciliter (dL)": 0.1,
        "Liter (L)": 1,
        "Cubic Meter (m³)": 1000,
        "Cubic Centimeter (cm³)": 0.001,
        "Cubic Millimeter (mm³)": 1e-6,

        # Imperial and US Customary Units
        "Teaspoon (tsp)": 0.00492892,
        "Tablespoon (tbsp)": 0.0147868,
        "Fluid Ounce (US)": 0.0295735,
        "Fluid Ounce (Imperial)": 0.0284131,
        "Cup (US)": 0.236588,
        "Cup (Metric)": 0.25,
        "Cup (Imperial)": 0.284131,
        "Pint (US)": 0.473176,
        "Pint (Imperial)": 0.568261,
        "Quart (US)": 0.946353,
        "Quart (Imperial)": 1.13652,
        "Gallon (US)": 3.78541,
        "Gallon (Imperial)": 4.54609,
        "Fluid Dram (US)": 0.00369669,
        "Fluid Dram (Imperial)": 0.00355163,
        "Gill (US)": 0.118294,
        "Gill (Imperial)": 0.142065,

        # Specialized and Historical Units
        "Barrel (Oil)": 159,
        "Barrel (Beer, US)": 117,
        "Barrel (Beer, UK)": 163.66,
        "Hogshead (US)": 238.48,
        "Hogshead (UK)": 327.32,
        "Drop (gtt)": 0.00005,

        # Cubic Units
        "Cubic Inch (in³)": 0.016387,
        "Cubic Foot (ft³)": 28.3168,
        "Cubic Yard (yd³)": 764.555,

        # Large Volumes for Industrial Use
        "Acre-Foot (ac⋅ft)": 1233.48,
        "Board Foot": 0.00236,
    }

    # Ensure units are valid
    if from_unit not in conversion_to_liters or to_unit not in conversion_to_liters:
        raise ValueError(f"Unsupported units: {from_unit} or {to_unit}")

    # Convert from the source unit to liters
    steps = []
    steps.append(f"Step 1: Convert {value} {from_unit} to liters")
    value_in_liters = value * conversion_to_liters[from_unit]
    steps.append(f"Formula: {value} × {conversion_to_liters[from_unit]} = {value_in_liters} liters")

    # Convert from liters to the target unit
    steps.append(f"Step 2: Convert {value_in_liters} liters to {to_unit}")
    result = value_in_liters / conversion_to_liters[to_unit]
    steps.append(f"Formula: {value_in_liters} ÷ {conversion_to_liters[to_unit]} = {result} {to_unit}\n")

    # Add the final result
    steps.append(f"Final Result: {result} {to_unit}")

    return result, "\n".join(steps)