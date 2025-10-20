"""
Activity 6: Refactoring Lab 5 with Functions
CMPSC 100 - Computational Expression

Student Name: [Your Name]
Date: [Today's Date]

Purpose: Refactor Lab 5 Smart Home Status Monitor using functions
to improve code organization and demonstrate function concepts.

Instructions:
1. Copy your Lab 5 main.py code below
2. Refactor it by creating the 8 required functions
3. Update main() to use these functions
4. Test to ensure it works the same as original

Required Functions to Implement:
- setup_hardware()
- display_device_status(active_devices, available_devices)  
- update_led_indicators(active_devices, led_security, led_hvac, led_lighting)
- test_system_leds(led_security, led_hvac, led_lighting)
- get_available_devices_to_turn_on(active_devices, available_devices)
- wait_for_button_confirmation(button)
- turn_on_device(active_devices, available_devices, button, led_security, led_hvac, led_lighting)
- turn_off_device(active_devices, button, led_security, led_hvac, led_lighting)
"""

# Import necessary modules
from machine import Pin
import time
import sys

# TODO: Create the setup_hardware function
def setup_hardware():
    """Sets up and returns all hardware pin objects"""
    # TODO: Create LED and button pin objects
    # TODO: Return all pin objects as a tuple
    pass

# TODO: Create the display_device_status function  
def display_device_status(active_devices, available_devices):
    """Displays current status of active and available devices"""
    # TODO: Show active devices list
    # TODO: Show available devices list with count
    pass

# TODO: Create the update_led_indicators function
def update_led_indicators(active_devices, led_security, led_hvac, led_lighting):
    """Updates LED status based on active devices"""
    # TODO: Turn on security LED if "front_door_lock" in active_devices
    # TODO: Turn on HVAC LED if "thermostat" in active_devices  
    # TODO: Turn on lighting LED if "living_room_lights" in active_devices
    # TODO: Turn off LEDs for inactive devices
    pass

# TODO: Create the test_system_leds function
def test_system_leds(led_security, led_hvac, led_lighting):
    """Tests all LED systems at startup"""
    # TODO: Test each LED system with appropriate message
    # TODO: Turn on each LED, wait 0.5 seconds, turn off
    pass

# TODO: Create the get_available_devices_to_turn_on function
def get_available_devices_to_turn_on(active_devices, available_devices):
    """Returns list of devices that can be turned on"""
    # TODO: Create list of devices that are available but not active
    # TODO: Return the list
    pass

# TODO: Create the wait_for_button_confirmation function
def wait_for_button_confirmation(button):
    """Waits for button press and handles confirmation"""
    # TODO: Print confirmation message
    # TODO: Wait for button press (while button.value() == 1)
    # TODO: Add debounce delay
    # TODO: Print confirmation received message
    pass

# TODO: Create the turn_on_device function
def turn_on_device(active_devices, available_devices, button, led_security, led_hvac, led_lighting):
    """Handles turning on a device with user selection and confirmation"""
    # TODO: Get list of devices that can be turned on
    # TODO: Display available devices to user
    # TODO: Get user's device choice
    # TODO: Wait for button confirmation
    # TODO: Add selected device to active_devices list
    # TODO: Update LED indicators
    # TODO: Print confirmation message
    pass

# TODO: Create the turn_off_device function  
def turn_off_device(active_devices, button, led_security, led_hvac, led_lighting):
    """Handles turning off a device with user selection and confirmation"""
    # TODO: Display active devices to user
    # TODO: Get user's device choice
    # TODO: Wait for button confirmation
    # TODO: Remove selected device from active_devices list
    # TODO: Update LED indicators  
    # TODO: Print confirmation message
    pass

def main():
    """Main function that runs the smart home monitoring system."""
    
    # TODO: Replace direct hardware setup with function call
    # Example: led_security, led_hvac, led_lighting, button = setup_hardware()
    
    # TODO: Copy and refactor your Lab 5 code here
    # TODO: Replace repetitive code with function calls
    # TODO: Use the functions you created above
    
    print("Smart Home Control System")
    print("Select option 3 to exit the program")
    
    # TODO: Initialize device lists
    active_devices = ["thermostat"]
    available_devices = ["thermostat", "front_door_lock", "living_room_lights"]
    
    # TODO: Add user interaction, system testing, and main control loop
    # TODO: Use your functions instead of inline code
    
    pass  # Remove this when you add your code

# Run the main function when the script is executed directly
if __name__ == "__main__":
    main()