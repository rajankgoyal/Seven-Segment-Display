import machine
import utime

# Defines segment pins for left display
segments = [machine.Pin(pin, machine.Pin.OUT) for pin in [1, 2, 3, 4, 5, 6, 7, 8]]

# Defines common anode pin for left display
common_pin = machine.Pin(0, machine.Pin.OUT)

# Defines segment pins for right display
segments_b = [machine.Pin(pin, machine.Pin.OUT) for pin in [17, 18, 19, 20, 21, 22, 26, 27]]
# Defines common anode pin for right display
common_pin_b = machine.Pin(16, machine.Pin.OUT)

# Map segments to GPIO pins on left display
segment_map = {
    'A': segments[0],
    'B': segments[1],
    'C': segments[2],
    'D': segments[3],
    'E': segments[4],
    'F': segments[5],
    'G': segments[6],
    'DP': segments[7]
}

# Map segments to GPIO pins on right display
segment_map_b = {
    'A': segments_b[0],
    'B': segments_b[1],
    'C': segments_b[2],
    'D': segments_b[3],
    'E': segments_b[4],
    'F': segments_b[5],
    'G': segments_b[6],
    'DP': segments_b[7]
}


def display_digit(digit,digit_b):
    # Defines the segments for each digit (0-9)
    digit_segments = {
        0: ['G', 'DP'],
        1: ['A', 'D', 'E', 'F', 'G', 'DP'],
        2: ['C', 'F', 'DP'],
        3: ['E', 'F', 'DP'],
        4: ['A', 'D', 'E', 'DP'],
        5: ['B', 'E', 'DP'],
        6: ['B', 'DP'],
        7: ['D', 'E', 'F', 'G', 'DP'],
        8: ['DP'],
        9: ['E', 'DP'],
    }

    # Turns on all segments on left display
    for segment in segment_map.values():
        segment.off()

    # Keeps segments for the given digit on for left display
    for segment_key in digit_segments[digit]:
        segment_map[segment_key].on()

    # Turns on the common anode to display the digit
    common_pin.on()
    
    
    # Turns on all segments on right display
    for segment_b in segment_map_b.values():
        segment_b.off()

    # Keeps segments for the given digit on for right display
    for segment_key_b in digit_segments[digit_b]:
        segment_map_b[segment_key_b].on()

    
    # Turns on the common anode to second display the digit
    common_pin_b.on()
   
def print_digit(number):
    #Turns off the dot next to second display to indicate negitive number
    segments_b[7].on()
    # If number is positive two digit number
    # Print positive numbers between 0 to 99
    if number < 100 and number >= 0:
        digit = int(number/10)
        digit_b = number%10
        display_digit(digit,digit_b)
    # Print negitive numbers between -1 to -99
    elif number < 0 and number >= -99:
        number = number * -1
        digit = int(number/10)
        digit_b = number%10
        display_digit(digit,digit_b)
        # turns on the dot next to second display to indicate negitive number
        segments_b[7].off()
    # Prints a statement indicating number is too large to be printed 
    else:
        print("Number is too big to print", number)
        for segment in segment_map.values():
            segment.on()
        for segment_b in segment_map_b.values():
            segment_b.on()
    
    utime.sleep(0.25)