# Inspired by ENGR 102 Ascii clock school assignment. Changed it to work in real time
# - PK


import time
import os

# Simplified function to clear screen (for real-time display)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ASCII art for digits 0-9 and colon (:)
ascii_digits = {
    '0': ['###', '# #', '# #', '# #', '###'],
    '1': ['  #', '  #', '  #', '  #', '  #'],
    '2': ['###', '  #', '###', '#  ', '###'],
    '3': ['###', '  #', '###', '  #', '###'],
    '4': ['# #', '# #', '###', '  #', '  #'],
    '5': ['###', '#  ', '###', '  #', '###'],
    '6': ['###', '#  ', '###', '# #', '###'],
    '7': ['###', '  #', '  #', '  #', '  #'],
    '8': ['###', '# #', '###', '# #', '###'],
    '9': ['###', '# #', '###', '  #', '###'],
    ':': ['   ', ' # ', '   ', ' # ', '   ']
}

def ascii_clock_display(hour, minute, second):
    # Splits time into different digits
    hour1, hour2 = str(hour).zfill(2)
    minute1, minute2 = str(minute).zfill(2)
    second1, second2 = str(second).zfill(2)
    
    # Prepare lines in each row
    for i in range(5):
        # Display hour, colon, minute, colon, second
        print(f"{ascii_digits[hour1][i]} {ascii_digits[hour2][i]} {ascii_digits[':'][i]} {ascii_digits[minute1][i]} {ascii_digits[minute2][i]} {ascii_digits[':'][i]} {ascii_digits[second1][i]} {ascii_digits[second2][i]}")
    
while True:
    # Get the current time

    current_time = time.localtime()

    hour = current_time.tm_hour

    minute = current_time.tm_min

    second = current_time.tm_sec
    
    # Quickly clears screen and refreshes in real time
    clear_screen()
    
    # Display the current time with digits made above
    ascii_clock_display(hour, minute, second)
    
    # Update every one second
    time.sleep(1)