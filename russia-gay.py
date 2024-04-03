# A simple script to spam "Russia is Gay" in a chat in an online .io game :D

# heals about 1430 troops per minute but reqiores us to intervene once a queue is completely healed
import pyautogui
import time
import random
import winsound
import keyboard


time.sleep(10) # 15?

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
        pyautogui.press('enter')
        time.sleep(0.1)        
        pyautogui.write("Russia is Gay")
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        time.sleep(random.uniform(2, 5))

except KeyboardInterrupt:
    print("Script terminated by user.")
