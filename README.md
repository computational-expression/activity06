# Activity 6: Refactoring Lab 5 with Functions

## Learning Objectives
- Apply function concepts to restructure existing code
- Practice breaking complex programs into smaller, reusable functions
- Understand the benefits of function-based code organization
- Use parameters to make functions flexible and reusable

## Overview
In this activity, you will take your Lab 5 Smart Home Status Monitor code and **refactor** it using functions. Refactoring means restructuring existing code to improve its organization without changing what it does.

## Why Refactor with Functions?

Your Lab 5 code probably had everything in one large `main()` function. While this works, it can be improved by:

- **Breaking down complex tasks** into smaller, focused functions
- **Reducing repetition** by reusing code through function calls
- **Making code easier to test** by isolating specific behaviors
- **Improving readability** with descriptive function names
- **Enabling reuse** of logic in other programs

## Required Functions to Create

Based on the functions concepts from Week 9 slides, restructure your Lab 5 code by creating these specific functions:

### 1. Hardware Setup Function
```python
def setup_hardware():
    """Sets up and returns all hardware pin objects"""
    # Return LED pins and button pin
    pass
```

### 2. Device Display Function
```python
def display_device_status(active_devices, available_devices):
    """Displays current status of active and available devices"""
    # Show which devices are on/off
    pass
```

### 3. LED Update Function
```python
def update_led_indicators(active_devices, led_security, led_hvac, led_lighting):
    """Updates LED status based on active devices"""
    # Turn LEDs on/off based on device types
    pass
```

### 4. System Test Function
```python
def test_system_leds(led_security, led_hvac, led_lighting):
    """Tests all LED systems at startup"""
    # Blink each LED to verify it works
    pass
```

### 5. Device Selection Function
```python
def get_available_devices_to_turn_on(active_devices, available_devices):
    """Returns list of devices that can be turned on"""
    # Return devices that are available but not active
    pass
```

### 6. Button Confirmation Function
```python
def wait_for_button_confirmation(button):
    """Waits for button press and handles confirmation"""
    # Handle button press with proper timing
    pass
```

### 7. Turn On Device Function
```python
def turn_on_device(active_devices, available_devices, button, led_security, led_hvac, led_lighting):
    """Handles turning on a device with user selection and confirmation"""
    # Complete workflow for adding a device
    pass
```

### 8. Turn Off Device Function
```python
def turn_off_device(active_devices, button, led_security, led_hvac, led_lighting):
    """Handles turning off a device with user selection and confirmation"""
    # Complete workflow for removing a device
    pass
```

## Function Implementation Guidelines

### Use Parameters Effectively
- **Pass data into functions** instead of using global variables
- **Return values** when functions need to give data back
- **Keep functions focused** - each should do one main task

### Example Before/After:

**Before (all in main):**
```python
def main():
    led_security = Pin(15, Pin.OUT)
    led_hvac = Pin(14, Pin.OUT)
    led_lighting = Pin(13, Pin.OUT)
    button = Pin(12, Pin.IN, Pin.PULL_UP)
    
    print("Testing security system...")
    led_security.on()
    time.sleep(0.5)
    led_security.off()
    # ... more LED testing code
    
    # ... 200+ lines of other code
```

**After (with functions):**
```python
def setup_hardware():
    """Sets up and returns all hardware pin objects"""
    led_security = Pin(15, Pin.OUT)
    led_hvac = Pin(14, Pin.OUT)
    led_lighting = Pin(13, Pin.OUT)
    button = Pin(12, Pin.IN, Pin.PULL_UP)
    return led_security, led_hvac, led_lighting, button

def test_system_leds(led_security, led_hvac, led_lighting):
    """Tests all LED systems at startup"""
    systems = [
        (led_security, "Security system"),
        (led_hvac, "HVAC system"),
        (led_lighting, "Lighting system")
    ]
    
    for led, name in systems:
        print(f"Testing {name}...")
        led.on()
        time.sleep(0.5)
        led.off()

def main():
    # Set up hardware using function
    led_security, led_hvac, led_lighting, button = setup_hardware()
    
    # Test LEDs using function
    test_system_leds(led_security, led_hvac, led_lighting)
    
    # ... rest of main logic
```

## Steps to Complete

1. **Copy your Lab 5 code** into `main.py`
2. **Identify repetitive code** that can be extracted into functions
3. **Create each required function** one at a time
4. **Test each function** as you create it
5. **Update your main()** to use the new functions
6. **Verify your program still works** the same way as before

## Testing Your Refactored Code

Your refactored program should:
- **Behave exactly the same** as your original Lab 5
- **Use all 8 required functions** with appropriate parameters
- **Have a cleaner, more organized main()** function
- **Be easier to read and understand**

## What to Submit

- `main.py` - Your refactored Lab 5 code using the 8 required functions
- Make sure your code still runs correctly and produces the same output

## Grading Criteria

- **Function creation**: All 8 functions implemented correctly
- **Parameter usage**: Functions use parameters effectively instead of global variables
- **Code organization**: Main function is cleaner and more readable
- **Functionality**: Program works the same as original Lab 5
- **Best practices**: Good function names, appropriate return values

This activity will help you see the power of functions for organizing code and making it more maintainable!