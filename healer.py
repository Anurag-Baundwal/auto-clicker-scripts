# faster version heals about 455 troops per minute
##########################
'''
auto healer script. 
IMPORTANT: RUN IT WITH ADMINSTRATOR PRIVILEGES (for clicks in bluestacks)
run python-healer.py
you get 10s to navigate to the game and open the healing screen
then hover mouse over the quick select button until beep is heard
then hover mouse over the amount field until beep is heard
then hover mouse over the amount2 field (second amount) until beep is heard
then hover mouse over the heal button until beep is heard
'''
##########################
import pyautogui
import time
import winsound
import json
import pyperclip
import os
import clipboard

##########################################################################################

# Give user some time to navigate to the game/application window
print("Navigate to the game/application. Script will start in 10 seconds...")
time.sleep(10)
winsound.Beep(1000, 200)

def capture_position_and_beep(prompt_message):
    """Capture the mouse position and play a beep sound."""
    print(prompt_message)
    time.sleep(5)  # Wait 3 seconds to let the user click
    pos = pyautogui.position()
    winsound.Beep(1000, 200)  # Beep at 1000 Hz for 200 ms
    return pos

def load_positions_from_file():
    """Load button positions from a JSON file."""
    if os.path.exists('button_positions.json'):
        with open('button_positions.json', 'r') as f:
            return json.load(f)
    return None

amt2_none_flag = False
def get_amount2(): # read amount2, convert it to an int if possible, and return the int
    global amt2_none_flag
    for _ in range(75):  # Attempt up to 15 times
        print(f"get_amoun2 loop iteration {_}")
        pyautogui.click(amount_x2, amount_y2)
        time.sleep(0.2)
        pyperclip.copy('abcde')
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.1)
        amount2_ = pyperclip.paste()
        try:
            return int(amount2_)
        except ValueError:
            continue
    amt2_none_flag = True
    return None  # Return None if unable to get integer after 10 attempts
# blank field - returns none
# amount2 button not present - returns last value in clipboard -> none in case of garbage value


button_positions = load_positions_from_file()
if not button_positions:
    select_x, select_y = capture_position_and_beep("Please click the 'select' button...")
    amount_x, amount_y = capture_position_and_beep("Please click the 'amount' button...")
    amount_x2, amount_y2 = capture_position_and_beep("Please click the 'amount2' button...")
    heal_x, heal_y = capture_position_and_beep("Please click the 'heal' button...")

    # then, save the positions to the file
    button_positions = {
        'select': {'x': select_x, 'y': select_y},
        'amount': {'x': amount_x, 'y': amount_y},
        'amount2': {'x': amount_x2, 'y': amount_y2},
        'heal': {'x': heal_x, 'y': heal_y},
    }
    with open('button_positions.json', 'w') as f:
        json.dump(button_positions, f)
else:
    select_x = button_positions['select']['x']
    select_y = button_positions['select']['y']
    amount_x = button_positions['amount']['x']
    amount_y = button_positions['amount']['y']
    amount_x2 = button_positions['amount2']['x']
    amount_y2 = button_positions['amount2']['y']
    heal_x = button_positions['heal']['x']
    heal_y = button_positions['heal']['y']

i=0;
target_amount = '250'
amount = ''
amount2 = ""
try:
    while True:
        print (f"This is loop iteration no. {i}.......................")
        while True and amt2_none_flag == False:
            amount2 = get_amount2()
            print(f"\t--> amount2 was read to be: {amount2}")
            pyautogui.click(amount_x2, amount_y2) # close it
            time.sleep(0.1)
            # Check if we need to click the quick select button
            print("Checking condition... ")
            if amount2== 0: # or amount2 == None: 
                break
            # if value is None then we did not manage to read it successfully. go to the start of this loop and try to read it again
            elif amount2 == None: 
                # continue
                break
            else:
                print("\t-->Condition not met. Clicking quick select button.")
                pyautogui.click(select_x, select_y)
                time.sleep(0.1)
        

        ####### Next step #############
        pyautogui.click(amount_x, amount_y)
        print("Clicked 'amount'")
        print("\t--> Setting amount to train")
        time.sleep(0.5)
        # Simulate pressing backspace three times to clear any existing value
        # for _ in range(5):
        #     pyautogui.press('backspace')
        #     time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.1)
        for letter in target_amount:
            pyautogui.write(letter)
            time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.5)
        ################################
        
        # Click 'heal' button twice
        pyautogui.click(heal_x, heal_y)
        print("Clicked heal")
        time.sleep(1.25)
        pyautogui.click(heal_x, heal_y)
        print("Clicked heal")
        time.sleep(0.25)

        # wait for the help button to be pressed by someone
        time.sleep(0.25)

        i+=1
except KeyboardInterrupt:
    print("Script terminated by user.")