import os
import sys
import logging
from PyQt5 import QtWidgets, uic # type: ignore

# Add the plugin directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

class CONVApp(QtWidgets.QWidget):
    def __init__(self, parent=None, logger=None):
        super().__init__(parent)
        self.logger = logger or logging.getLogger("CONV_Fallback")  # Use provided logger or fallback

        # Load the UI file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "CONV.ui")
        if os.path.exists(ui_path):
            uic.loadUi(ui_path, self)
            self.logger.info("UI file loaded successfully.")
        else:
            error_message = f"UI file not found: {ui_path}"
            self.logger.error(error_message)
            raise FileNotFoundError(error_message)

        # Initialize the UI components
        self.load_converters()

        # Connect signals to slots
        self.select_converter.currentTextChanged.connect(self.update_conversion_units)
        self.button_convert.clicked.connect(self.perform_conversion)

    def load_converters(self):
        """Populate the select_converter combobox with available converters."""
        self.select_converter.addItem("Temperature")        # Temperature converter
        self.select_converter.addItem("Distance")           # Distance converter
        self.select_converter.addItem("Weight")             # Weight Converter
        self.select_converter.addItem("Fluids")             # Fluids Converter
        self.select_converter.addItem("Time")               # Time converter
        self.select_converter.addItem("Energy")             # Energy Converter
        self.select_converter.addItem("Power")              # Power Converter
        self.select_converter.addItem("Pressure")           # Pressure Converter
        self.select_converter.addItem("Velocity")           # Velocity Converter
        self.select_converter.addItem("Area")               # Area Converter
        self.select_converter.addItem("Data Storage")       # Data Storage Converter

    def update_conversion_units(self):
        """Update the unit selection based on the chosen converter."""
        converter = self.select_converter.currentText()
        self.select_from.clear()
        self.select_to.clear()

        if converter == "Temperature":
            units = [
                "Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)", "Rankine (°R)", 
                "Delisle (°De)", "Newton (°N)", "Réaumur (°Re)", "Rømer (°Rø)"
            ]
        elif converter == "Distance":
            units = [
                "Foot (ft)", "Yard (yd)", "Mile (mi)", "Nautical Mile (NM)", "Centimeter (cm)", "Meter (m)", 
                "kilometer (km)", "Nanometer (nm)", "Micrometer (µm)", "League (lea)", "Chain (ch)", 
                "Rod (rd)", "Cubit (cbt)", "furlong (fur)", "Inch (in)", "Astronomical Unit (AU)", 
                "Light-Year (ly)", "Parsec (pc)", "Planck Length (lP)", "Fathom (fath)", "Hand (hand)", 
                "Perch (perch)", "Palm (palm)", "Barleycorn (barleycorn)", "Ell (ell)", "Span (span)", 
                "Step (step)", "Smoot (sm)"
            ]
        elif converter == "Weight":
            units = [
                "Milligram (mg)", "Centigram (cg)", "Decigram (dg)", "Gram (g)", "Kilogram (kg)", "Metric Ton (t)",
                "Ounce (oz)", "Pound (lb)", "Stone (st)", "US Hundredweight (cwt)", "UK Hundredweight (cwt)", 
                "US Ton (Short Ton)", "UK Ton (Long Ton)", "Grain (gr)", "Pennyweight (dwt)", "Troy Ounce (oz t)", 
                "Troy Pound (lb t)", "Carat (ct)", "Dram (dr)", "Shekel", "Mina", "Talent", "Obol", 
                "Slug (slug)", "Atomic Mass Unit (amu)", "Solar Mass (M☉)"
            ]
        elif converter == "Fluids":
            units = [
                "Milliliter (mL)", "Centiliter (cL)", "Deciliter (dL)", "Liter (L)", "Cubic Meter (m³)", 
                "Cubic Centimeter (cm³)", "Cubic Millimeter (mm³)", "Teaspoon (tsp)", "Tablespoon (tbsp)", 
                "Fluid Ounce (US)", "Fluid Ounce (Imperial)", "Cup (US)", "Cup (Metric)", "Cup (Imperial)", 
                "Pint (US)", "Pint (Imperial)", "Quart (US)", "Quart (Imperial)", "Gallon (US)", "Gallon (Imperial)", 
                "Fluid Dram (US)", "Fluid Dram (Imperial)", "Gill (US)", "Gill (Imperial)", "Barrel (Oil)", 
                "Barrel (Beer, US)", "Barrel (Beer, UK)", "Hogshead (US)", "Hogshead (UK)", "Drop (gtt)", 
                "Cubic Inch (in³)", "Cubic Foot (ft³)", "Cubic Yard (yd³)", "Acre-Foot (ac⋅ft)", "Board Foot"
            ]
        elif converter == "Time":
            units = [
                "Milliseconds (ms)", "Seconds (s)", "Minutes (min)", "Hours (hr)", "Days (d)", 
                "Weeks (wk)", "Months (approx)", "Years (yr)", "Decades", "Centuries",
                "Microseconds (µs)", "Nanoseconds (ns)", "Picoseconds (ps)"
            ]
        elif converter == "Energy":
            units = [
                "Joule (J)", "Kilojoule (kJ)", "Calorie (cal)", "Kilocalorie (kcal)",
                "Watt-hour (Wh)", "Kilowatt-hour (kWh)", "Electronvolt (eV)", 
                "British Thermal Unit (BTU)", "Therm"
            ]
        elif converter == "Power":
            units = [
                "Watt (W)", "Kilowatt (kW)", "Horsepower (hp)", "Foot-pound-force per second (ft·lbf/s)"
            ]
        elif converter == "Pressure":
            units = [
                "Pascal (Pa)", "Bar", "Atmosphere (atm)", "Pounds Per Square Inch (psi)", "Torr", "Millimeters of Mercury (mmHg)"
            ]

        elif converter == "Velocity":
            units = [
                "Meters per second (m/s)", "Kilometers per hour (km/h)", "Miles per hour (mph)", 
                "Knots", "Mach"
            ]

        elif converter == "Area":
            units = [
                "Square Meter (m²)", "Square Kilometer (km²)", "Square Foot (ft²)", "Square Yard (yd²)"
                "Acre", "Hectare", "Square Mile (mi²)", "Square Inch (in²)"
            ]

        elif converter == "Data Storage":
            units = [
                "Bit", "Byte (B)", "Kilobyte (KB)", "Megabyte (MB)", "Gigabyte (GB)", "Terabyte (TB)",
                "Petabyte (PB)", "Exabyte (EB)", "Zettabyte (ZB)" , "Yottabyte (YB)"
            ]

        else:
            units = []  # Fallback for unknown converters

        self.select_from.addItems(units)
        self.select_to.addItems(units)



    def perform_conversion(self):
        """Perform the conversion, clear results, and display the calculation steps."""
        from unit_converters.temperature import convert_temperature
        from unit_converters.distance import convert_distance
        from unit_converters.weight import convert_weight
        from unit_converters.fluids import convert_fluids
        from unit_converters.time import convert_time
        from unit_converters.energy import convert_energy
        from unit_converters.power import convert_power
        from unit_converters.pressure import convert_pressure
        from unit_converters.velocity import convert_velocity
        from unit_converters.area import convert_area
        from unit_converters.data_storage import convert_data_storage

        try:
            # Retrieve inputs from the UI
            converter = self.select_converter.currentText()
            from_unit = self.select_from.currentText()
            to_unit = self.select_to.currentText()
            value_text = self.edit_from.text()

            # Validate input
            if not value_text:
                raise ValueError("Please enter a numeric value to convert.")

            value = float(value_text)  # Convert input to a float

            # Check if a valid converter is selected
            
            if converter == "Temperature":
                result, steps = convert_temperature(value, from_unit, to_unit)

            elif converter == "Distance":
                result, steps = convert_distance(value, from_unit, to_unit)

            elif converter == "Weight":
                result, steps = convert_weight(value, from_unit, to_unit)

            elif converter == "Fluids":
                result, steps = convert_fluids(value, from_unit, to_unit)

            elif converter == "Time":
                result, steps = convert_time(value, from_unit, to_unit)
            
            elif converter == "Energy":
                result, steps = convert_energy(value, from_unit, to_unit)
            
            elif converter == "Power":
                result, steps = convert_power(value, from_unit, to_unit)

            elif converter == "Pressure":
                result, steps = convert_pressure(value, from_unit, to_unit)

            elif converter == "Velocity":
                result, steps = convert_velocity(value, from_unit, to_unit)

            elif converter == "Area":
                result, steps = convert_area(value, from_unit, to_unit)

            elif converter == "Data Storage":
                result, steps = convert_data_storage(value, from_unit, to_unit)

            else:
                self.display_results.append("Error: No converter selected.")
                return

            # Clear previous results
            self.display_results.clear()

            # Display the steps and result
            self.display_results.append("Conversion Steps:\n")
            self.display_results.append(steps)

        except ValueError as e:
            self.display_results.clear()
            self.display_results.append(f"Error: {str(e)}")
        except Exception as e:
            self.display_results.clear()
            self.display_results.append(f"Error: {str(e)}")

def main(parent_widget=None, parent_logger=None):
    # If a parent logger is provided, create a child logger for the plugin
    if parent_logger:
        plugin_logger = parent_logger.getChild("CONV")
    else:
        # Fallback logger in case no parent logger is provided
        import logging
        plugin_logger = logging.getLogger("CONV_Fallback")

    # Log the plugin initialization
    plugin_logger.info("CONV Plugin initialized.")

    # Pass the logger to the CONVApp instance
    app = CONVApp(parent_widget, plugin_logger)
    return app
