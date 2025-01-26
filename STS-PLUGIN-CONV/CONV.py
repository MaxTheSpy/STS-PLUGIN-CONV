import os
import sys
import logging
from PyQt5 import QtWidgets, uic # type: ignore

# Add the plugin directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from unit_converters.temperature import convert_temperature  # Import the converter

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
        self.select_converter.addItem("Select Converter")  # Default label
        self.select_converter.addItem("Temperature")       # Temperature converter
        self.select_converter.addItem("Distance")          # Distance converter

    def update_conversion_units(self):
        """Update the unit selection based on the chosen converter."""
        converter = self.select_converter.currentText()
        self.select_from.clear()
        self.select_to.clear()

        if converter == "Temperature":
            units = ["Celsius", "Fahrenheit", "Kelvin"]
            self.select_from.addItems(units)
            self.select_to.addItems(units)

        if converter == "Distance":
            units = ["foot", "yard", "mile","nautical mile", "centimeter", "meter", "kilometer",
                    "nanometer", "micrometer", "league", "chain", "rod", "cubit", "furlong"]
            self.select_from.addItems(units)
            self.select_to.addItems(units)



    def perform_conversion(self):
        """Perform the conversion, clear results, and display the calculation steps."""
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
                from unit_converters.temperature import convert_temperature
                result, steps = convert_temperature(value, from_unit, to_unit)

                # Clear previous results
                self.display_results.clear()

                # Display the steps and result
                self.display_results.append("Conversion Steps:\n")
                self.display_results.append(steps)

                return  # Exit the function

            elif converter == "Distance":
                from unit_converters.distance import convert_distance
                result, steps = convert_distance(value, from_unit, to_unit)

                # Clear previous results
                self.display_results.clear()

                # Display the steps and result
                self.display_results.append("Conversion Steps:\n")
                self.display_results.append(steps)

                return  # Exit the function

            # Handle the case where no valid converter is selected
            self.display_results.append("Error: No converter selected.")


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
