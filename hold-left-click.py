import pyautogui
import keyboard

# Flag to keep track of clicking state
is_clicking = False

# Function to toggle mouseDown and mouseUp
def toggle_click(e):
    global is_clicking
    if is_clicking:
        pyautogui.mouseUp()
    else:
        pyautogui.mouseDown()
    is_clicking = not is_clicking

# Listen for 'e' key press to toggle clicking
keyboard.on_press_key('e', toggle_click)

# Keep the program running
keyboard.wait()
