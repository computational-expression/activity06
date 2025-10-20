"""
Activity 6: Refactoring Lab 5 with Functions - SOLUTION
CMPSC 100 - Computational Expression

Purpose: Refactor Lab 5 Smart Home Status Monitor using functions
to improve code organization and demonstrate function concepts.

This solution demonstrates how to break down the Lab 5 code into
8 focused functions, making the code more organized and reusable.
"""

# Import necessary modules
from machine import Pin
import time
import sys

def setup_hardware():
    """Sets up and returns all hardware pin objects"""
    # Create LED pin objects for the 3 home systems
    led_security = Pin(15, Pin.OUT)   # Red LED - Security system
    led_hvac = Pin(14, Pin.OUT)       # Yellow LED - HVAC system
    led_lighting = Pin(13, Pin.OUT)   # Green LED - Lighting system
    
    # Create button pin object for control
    button = Pin(12, Pin.IN, Pin.PULL_UP)  # Control button
    
    # Return all pin objects (multiple values separated by commas)
    return led_security, led_hvac, led_lighting, button

def display_device_status(user_name, active_devices, available_devices):
    """Displays current status of active and available devices"""
    # Show user's smart home status with their name
    print(f"\n{user_name}'s Smart Home Status:")
    
    # Show active devices list with numbering
    print("Active devices:")
    if len(active_devices) == 0:
        print("  No devices currently active")
    else:
        for i in range(len(active_devices)):
            print(f"  {i + 1}. {active_devices[i]}")
    
    # Show available devices list with count
    print(f"\nAvailable devices ({len(available_devices)} total):")
    for i in range(len(available_devices)):
        print(f"  {i + 1}. {available_devices[i]}")

def update_led_indicators(active_devices, led_security, led_hvac, led_lighting):
    """Updates LED status based on active devices"""
    # Turn on security LED if front door lock is active
    if "front_door_lock" in active_devices:
        led_security.on()
    else:
        led_security.off()
    
    # Turn on HVAC LED if thermostat is active
    if "thermostat" in active_devices:
        led_hvac.on()
    else:
        led_hvac.off()
    
    # Turn on lighting LED if living room lights are active
    if "living_room_lights" in active_devices:
        led_lighting.on()
    else:
        led_lighting.off()

def test_system_leds(led_security, led_hvac, led_lighting):
    """Tests all LED systems at startup"""
    # Create list of LED systems to test
    systems = [
        (led_security, "Security system"),
        (led_hvac, "HVAC system"),
        (led_lighting, "Lighting system")
    ]
    
    # Test each LED system with appropriate message
    print("\nTesting home systems...")
    for led, system_name in systems:
        print(f"{system_name}...")
        led.on()        # Turn on LED
        time.sleep(0.5) # Wait 0.5 seconds
        led.off()       # Turn off LED
    
    print("All systems operational!")

def get_available_devices_to_turn_on(active_devices, available_devices):
    """Returns list of devices that can be turned on"""
    # Create list of devices that are available but not active
    off_devices = []
    for device in available_devices:
        if device not in active_devices:
            off_devices.append(device)
    
    # Return the list
    return off_devices

def wait_for_button_confirmation(button):
    """Waits for button press and handles confirmation"""
    # Print confirmation message
    print("Press button to confirm...")
    
    # Wait for button press (while button.value() == 1)
    while button.value() == 1:
        time.sleep(0.1)
    
    # Add debounce delay
    time.sleep(0.2)
    
    # Print confirmation received message
    print("Button pressed - command confirmed!")

def turn_on_device(active_devices, available_devices, button, led_security, led_hvac, led_lighting):
    """Handles turning on a device with user selection and confirmation"""
    # Get list of devices that can be turned on
    off_devices = get_available_devices_to_turn_on(active_devices, available_devices)
    
    # Display available devices to user
    print("\nAvailable devices to turn ON:")
    
    if len(off_devices) == 0:
        print("All devices are already ON!")
        return  # Exit function early if no devices available
    
    # Show numbered list of available devices
    for i in range(len(off_devices)):
        print(f"  {i + 1}. {off_devices[i]}")
    
    # Get user's device choice
    device_choice = int(input(f"Choose device (1-{len(off_devices)}): "))
    selected_device = off_devices[device_choice - 1]
    
    # Wait for button confirmation
    wait_for_button_confirmation(button)
    
    # Add selected device to active_devices list
    active_devices.append(selected_device)
    
    # Update LED indicators
    update_led_indicators(active_devices, led_security, led_hvac, led_lighting)
    
    # Print confirmation message
    print(f"Turned ON: {selected_device}")

def turn_off_device(active_devices, button, led_security, led_hvac, led_lighting):
    """Handles turning off a device with user selection and confirmation"""
    # Display active devices to user
    print("\nActive devices to turn OFF:")
    
    if len(active_devices) == 0:
        print("No devices are currently ON!")
        return  # Exit function early if no devices active
    
    # Show numbered list of active devices
    for i in range(len(active_devices)):
        print(f"  {i + 1}. {active_devices[i]}")
    
    # Get user's device choice
    device_choice = int(input(f"Choose device (1-{len(active_devices)}): "))
    selected_device = active_devices[device_choice - 1]
    
    # Wait for button confirmation
    wait_for_button_confirmation(button)
    
    # Remove selected device from active_devices list
    active_devices.remove(selected_device)
    
    # Update LED indicators
    update_led_indicators(active_devices, led_security, led_hvac, led_lighting)
    
    # Print confirmation message
    print(f"Turned OFF: {selected_device}")

def main():
    """Main function that runs the smart home monitoring system."""
    
    # Set up hardware using function - receives multiple return values
    led_security, led_hvac, led_lighting, button = setup_hardware()
    
    # Initialize device lists
    active_devices = ["thermostat"]
    available_devices = ["thermostat", "front_door_lock", "living_room_lights"]
    
    # Main program startup
    print("Smart Home Control System")
    print("Select option 3 to exit the program")
    
    # Start session
    print("\n" + "="*50)
    print("SMART HOME SESSION")
    print("="*50)
    
    # Get user name and show welcome message
    user_name = input("\nHomeowner name: ")
    
    print("*** Smart Home Status Monitor ***")
    print("=" * 38)
    print("Welcome to your IoT device manager!")
    print("=" * 38)
    print(f"\nWelcome home, {user_name}!")
    
    # Use test_system_leds() function for LED testing
    test_system_leds(led_security, led_hvac, led_lighting)
    
    # Initialize available devices
    time.sleep(1)
    print("\nInitializing smart home devices...")
    print("Adding devices to available control list...")
    time.sleep(1.5)
    print("Device setup complete!")
    
    # Use display_device_status() to show initial status
    display_device_status(user_name, active_devices, available_devices)
    
    # Main IoT control loop using refactored functions
    operation_count = 0
    while True:
        operation_count += 1
        print(f"\n" + "="*38)
        print(f"Home Control Operation {operation_count}")
        
        # Update LED indicators using function
        update_led_indicators(active_devices, led_security, led_hvac, led_lighting)
        
        # Show menu options
        print("\nChoose an action:")
        print("1. Turn ON a device (add to active list)")
        print("2. Turn OFF a device (remove from active list)")
        print("3. Exit program")
        
        choice = input("Enter choice (1, 2, or 3): ")
        
        if choice == "1":
            # Use turn_on_device function
            turn_on_device(active_devices, available_devices, button, led_security, led_hvac, led_lighting)
            
        elif choice == "2":
            # Use turn_off_device function
            turn_off_device(active_devices, button, led_security, led_hvac, led_lighting)
            
        elif choice == "3":
            # EXIT PROGRAM
            print("\nExiting Smart Home Control System...")
            print("All systems powered down. Goodbye!")
            # Turn off all LEDs before exit
            led_security.off()
            led_hvac.off()
            led_lighting.off()
            sys.exit()
        
        else:
            print("Invalid action!")
        
        # Show updated status
        print(f"\nUpdated Status ({len(active_devices)} devices active):")
        if len(active_devices) == 0:
            print("  No devices currently active")
        else:
            for device in active_devices:
                print(f"  {device}")
        
        time.sleep(1)

# Run the main function when the script is executed directly
if __name__ == "__main__":
    main()