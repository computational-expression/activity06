"""
Lab 5: Smart Home Status Monitor - Solution
CMPSC 100 - Computational Expression

This is the reference solution for Lab 5. You can use this code
or your own Lab 5 implementation for Activity 6.

Purpose: Create a smart home monitoring system using lists to track device status.
Practice adding and removing devices from lists while using LED indicators and button control.

"""

# Import necessary modules for hardware control
from machine import Pin
import time
import sys

def main():
    """Main function to run the smart home monitoring system."""
    
    # Set up hardware for IoT simulation
    # 3 LEDs represent different home systems + 1 button for control
    # Updated for 30-row half breadboard layout
    led_security = Pin(15, Pin.OUT)   # Red LED - Security system (Pin 20 → Row 21)
    led_hvac = Pin(14, Pin.OUT)       # Yellow LED - Heating/AC system (Pin 19 → Row 22)
    led_lighting = Pin(13, Pin.OUT)   # Green LED - Smart lighting system (Pin 17 → Row 23)
    button = Pin(12, Pin.IN, Pin.PULL_UP)  # Control button (Pin 16 → Rows 27/29)

    # Create two lists for IoT device management
    # List 1: Active devices (devices currently ON)
    active_devices = ["thermostat"]

    # List 2: Available devices (all devices that can be controlled)
    # Each device corresponds to one of the 3 LED systems
    available_devices = ["thermostat", "front_door_lock", "living_room_lights"]

    # Main program - single session
    print("Smart Home Control System")
    print("Select option 3 to exit the program")

    # Initialize active devices
    active_devices = ["thermostat"]

    # Start session
    print("\n" + "="*50)
    print("SMART HOME SESSION")
    print("="*50)

    # Get user name
    user_name = input("\nHomeowner name: ")

    # Welcome and system test
    print("*** Smart Home Status Monitor ***")
    print("=" * 38)
    print("Welcome to your IoT device manager!")
    print("=" * 38)
    print(f"\nWelcome home, {user_name}!")

    # Test LED system indicators
    print("\nTesting home systems...")
    print("Security system...")
    led_security.on()
    time.sleep(0.5)
    led_security.off()

    print("HVAC system...")
    led_hvac.on()
    time.sleep(0.5)
    led_hvac.off()

    print("Lighting system...")
    led_lighting.on()
    time.sleep(0.5)
    led_lighting.off()
    print("All systems operational!")

    # Initialize available devices
    time.sleep(1)
    print("\nInitializing smart home devices...")
    print("Adding devices to available control list...")
    time.sleep(1.5)
    print("Device setup complete!")

    # Show initial device status
    print(f"\n{user_name}'s Smart Home Status:")
    print("Active devices:")
    for i in range(len(active_devices)):
        print(f"  {i + 1}. {active_devices[i]}")

    print(f"\nAvailable devices ({len(available_devices)} total):")
    for i in range(len(available_devices)):
        print(f"  {i + 1}. {available_devices[i]}")

    # Main IoT control loop - continue until user wants to finish
    operation_count = 0
    while True:
        operation_count += 1
        print(f"\n" + "="*38)
        print(f"Home Control Operation {operation_count}")
        
        # Update LED status based on active devices
        # Security LED: ON if front door lock is active
        if "front_door_lock" in active_devices:
            led_security.on()
        else:
            led_security.off()
        
        # HVAC LED: ON if thermostat is active
        if "thermostat" in active_devices:
            led_hvac.on()
        else:
            led_hvac.off()
        
        # Lighting LED: ON if living room lights are active
        if "living_room_lights" in active_devices:
            led_lighting.on()
        else:
            led_lighting.off()
        
        print("\nChoose an action:")
        print("1. Turn ON a device (add to active list)")
        print("2. Turn OFF a device (remove from active list)")
        print("3. Exit program")
        
        choice = input("Enter choice (1, 2, or 3): ")
        
        if choice == "1":
            # ADD DEVICE (turn ON)
            print("\nAvailable devices to turn ON:")
            off_devices = []
            for device in available_devices:
                if device not in active_devices:
                    off_devices.append(device)
            
            if len(off_devices) == 0:
                print("All devices are already ON!")
            else:
                for i in range(len(off_devices)):
                    print(f"  {i + 1}. {off_devices[i]}")
                
                device_choice = int(input(f"Choose device (1-{len(off_devices)}): "))
                selected_device = off_devices[device_choice - 1]
                
                # Wait for button confirmation AFTER device selection
                print("Press button to confirm...")
                while button.value() == 1:  # Wait for button press
                    time.sleep(0.1)
                time.sleep(0.2)  # Prevent button bounce
                print("Button pressed - command confirmed!")
                
                active_devices.append(selected_device)  # Add to active list
                print(f"Turned ON: {selected_device}")
        
        elif choice == "2":
            # REMOVE DEVICE (turn OFF)
            print("\nActive devices to turn OFF:")
            
            if len(active_devices) == 0:
                print("No devices are currently ON!")
            else:
                for i in range(len(active_devices)):
                    print(f"  {i + 1}. {active_devices[i]}")
                
                device_choice = int(input(f"Choose device (1-{len(active_devices)}): "))
                selected_device = active_devices[device_choice - 1]
                
                print("Press button to confirm...")
                while button.value() == 1:  # Wait for button press
                    time.sleep(0.1)
                time.sleep(0.2)  # Prevent button bounce
                print("Button pressed - command confirmed!")
                
                active_devices.remove(selected_device)  # Remove from active list
                print(f"Turned OFF: {selected_device}")
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