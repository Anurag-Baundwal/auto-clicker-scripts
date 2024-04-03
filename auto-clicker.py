# heals about 1430 troops per minute but reqiores us to intervene once a queue is completely healed
import pyautogui
import time
import random
import winsound
import keyboard


time.sleep(5) # 15?
winsound.Beep(1000, 200)

# Store the initial position of the mouse
previous_x, previous_y = pyautogui.position()

clicks = 0
max_offset = 1  # Maximum offset in pixels

max_dist = 1
start_x, start_y = pyautogui.position()
try:
    while True:
        # Check for pause and go keyword
        if keyboard.is_pressed('ctrl+y'):
            print("Paused.")
            while True:  # Loop until 'go' is pressed
                time.sleep(0.1)  # Avoid busy-waiting
                if keyboard.is_pressed('ctrl+m'):
                    print("Resumed.")
                    break
                
        # Get the current mouse position
        x, y = pyautogui.position()
        
        # Calculate random jiggle
        jiggle_x = random.randint(-max_offset, max_offset)
        jiggle_y = random.randint(-max_offset, max_offset)
        pyautogui.moveTo(x, y)

        # Check if the jiggled position stays within bounds
        if abs(start_x - (x + jiggle_x)) <= max_dist and abs(start_y - (y + jiggle_y)) <= max_dist:
            x += jiggle_x
            y += jiggle_y
            pyautogui.moveTo(x, y)

        # Calculate the difference between the current position and the previous one
        diff_x = abs(x - previous_x)
        diff_y = abs(y - previous_y)
        # # Check if the mouse has moved more than 100 pixels in either direction
        # if diff_x > 500 or diff_y > 500:
        #     print("Rapid mouse movement detected. Stopping the clicks for 15s...")
        #     time.sleep(15)
        # perform the click
        
        pyautogui.click() 
        clicks += 1
        
        # Store the current position for the next iteration's comparison
        previous_x, previous_y = x, y
        
        # Sleep for a random time interval between 0.5 and 3 seconds
        time.sleep(random.uniform(0.5, 1))

except KeyboardInterrupt:
    print("Script terminated by user.")