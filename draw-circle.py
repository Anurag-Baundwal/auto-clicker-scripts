import winsound
import pyautogui
import time
import math

def capture_position_and_beep(prompt_message):
    """Capture the mouse position and play a beep sound."""
    print(prompt_message)
    time.sleep(5)  # Wait 3 seconds to let the user click
    pos = pyautogui.position()
    winsound.Beep(1000, 200)  # Beep at 1000 Hz for 200 ms
    return pos

print("Navigate to the game/application. Script will start in 10 seconds...")
time.sleep(5)

# Set the center and radius of the circle
center_x, center_y = capture_position_and_beep("Hover the mouse over the center of the circle...")
point_x, point_y = capture_position_and_beep("Hover the mouse over any point on the boundary of the circle...")

radius = ((center_x - point_x)**2 + (center_y - point_y)**2)**0.5

delay_ms = 0.1

# Hold down the left button
# pyautogui.mouseDown()

# 1 degree = 0.0174533 radian
c = math.pi/180
points = [(center_x + radius * math.cos(angle*c*6), center_y + radius * math.sin(angle*c*6)) for angle in range(360//6)]

pyautogui.moveTo(points[0])
pyautogui.mouseDown()
# Move the mouse along the circle
for point in points:
    x, y = point
    pyautogui.moveTo(x, y)
    # time.sleep(delay_ms/1000)
pyautogui.moveTo(points[0])
# Release the left button
pyautogui.mouseUp()