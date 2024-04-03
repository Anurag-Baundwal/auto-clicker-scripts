# script start
# heals about 1430 troops per minute but reqiores us to intervene once a queue is completely healed
import pyautogui
import time
import random
import winsound
import keyboard

def suppress_key(e):
    pass

time.sleep(10) # 15?

i = 0;
try:
    while True:
        print(f"Loop iteration {i}... ")
        if keyboard.is_pressed('ctrl+y'):
            print("Paused.")
            while True:
                time.sleep(0.1)
                if keyboard.is_pressed('ctrl+m'):
                    print("Resumed.")
                    break

        # Suppress arrow keys
        keyboard.on_press_key('up', suppress_key, suppress=True)
        keyboard.on_press_key('down', suppress_key, suppress=True)
        keyboard.on_press_key('left', suppress_key, suppress=True)
        keyboard.on_press_key('right', suppress_key, suppress=True)

        pyautogui.press('enter')
        time.sleep(0.05)
        pyautogui.write("u gay")
        time.sleep(0.05)
        pyautogui.press('enter')

        # Remove suppression on arrow keys
        time.sleep(0.05)  # introduce a small delay
        keyboard.unhook_key('up')
        print('unhooked up arrow key')
        keyboard.unhook_key('down')
        print('unhooked down arrow key')
        keyboard.unhook_key('left')
        print('unhooked left arrow key')
        keyboard.unhook_key('right')
        print('unhooked right arrow key')

        print(keyboard._hooks)

        pyautogui.press('up')
        pyautogui.press('down')
        pyautogui.press('left')
        pyautogui.press('right')

        time.sleep(random.uniform(2, 5))
        i += 1
except KeyboardInterrupt:
    print("Script for sending messages terminated by user.")

#script end