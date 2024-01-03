import machine
import utime

# Define segment pins
segments = [machine.Pin(pin, machine.Pin.OUT) for pin in [1, 2, 3, 4, 5, 6, 7, 8]]

# Define common anode/cathode pin
common_pin = machine.Pin(0, machine.Pin.OUT)

# Define segment pins for second display
segments_b = [machine.Pin(pin, machine.Pin.OUT) for pin in [17, 18, 19, 20, 21, 22, 26, 27]]
# Define common anode/cathode pin for second display
common_pin_b = machine.Pin(16, machine.Pin.OUT)

# Map segments to GPIO pins
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

# Map segments to GPIO pins on second display
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
    # Define the segments for each digit (0-9)
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
        9: ['E', 'DP']
    }

    # Turn off all segments
    for segment in segment_map.values():
        segment.off()

    # Turn on segments for the given digit
    for segment_key in digit_segments[digit]:
        segment_map[segment_key].on()

    # Turn on the common anode/cathode to display the digit
    common_pin.on()
    
    
    # Turn off all segments on second display
    for segment_b in segment_map_b.values():
        segment_b.off()

    # Turn on segments for the given digit on second display
    for segment_key_b in digit_segments[digit_b]:
        segment_map_b[segment_key_b].on()

    
    # Turn on the common anode/cathode to second display the digit
    common_pin_b.on()


# Main loop
while True:
    for number in range(100):
        digit = int(number/10)
        digit_b = number%10
        print(number)
        display_digit(digit,digit_b)
        
        utime.sleep(0.2)
