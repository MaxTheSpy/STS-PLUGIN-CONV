def convert_weight(value, from_unit, to_unit):
    """Convert weight between various units and show the formula."""
    # Conversion factors to grams (base unit)
    conversion_to_grams = {
        # Metric Units
        "Milligram (mg)": 0.001,
        "Centigram (cg)": 0.01,
        "Decigram (dg)": 0.1,
        "Gram (g)": 1,
        "Kilogram (kg)": 1000,
        "Metric Ton (t)": 1_000_000,

        # Imperial and US Customary Units
        "Ounce (oz)": 28.3495,
        "Pound (lb)": 453.592,
        "Stone (st)": 6350.29,
        "US Hundredweight (cwt)": 45_359.2,
        "UK Hundredweight (cwt)": 50_802.3,
        "US Ton (Short Ton)": 907_184.7,
        "UK Ton (Long Ton)": 1_016_046.9,

        # Troy and Apothecaries' Units
        "Grain (gr)": 0.06479891,
        "Pennyweight (dwt)": 1.55517384,
        "Troy Ounce (oz t)": 31.1034768,
        "Troy Pound (lb t)": 373.2417216,

        # Ancient and Historical Units
        "Carat (ct)": 0.2,
        "Dram (dr)": 1.771845195,
        "Shekel": 11.5,  # Approximate
        "Mina": 500,     # Approximate
        "Talent": 30_000,  # Approximate
        "Obol": 0.72,    # Approximate

        # Specialized Units
        "Slug (slug)": 14_593.9,
        "Atomic Mass Unit (amu)": 1.66053906660e-24,
        "Solar Mass (M☉)": 1.989e33,
    }

    # Ensure units are valid
    if from_unit not in conversion_to_grams or to_unit not in conversion_to_grams:
        raise ValueError(f"Unsupported units: {from_unit} or {to_unit}")

    # Convert from the source unit to grams
    steps = []
    steps.append(f"Step 1: Convert {value} {from_unit} to grams")
    value_in_grams = value * conversion_to_grams[from_unit]
    steps.append(f"Formula: {value} × {conversion_to_grams[from_unit]} = {value_in_grams} grams")

    # Convert from grams to the target unit
    steps.append(f"Step 2: Convert {value_in_grams} grams to {to_unit}")
    result = value_in_grams / conversion_to_grams[to_unit]
    steps.append(f"Formula: {value_in_grams} ÷ {conversion_to_grams[to_unit]} = {result} {to_unit}\n")

    # Add the final result
    steps.append(f"Final Result: {result} {to_unit}")

    return result, "\n".join(steps)
