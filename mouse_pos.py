import pyautogui

current_mouse_position = pyautogui.position()
old_mouse_position = pyautogui.position()

while True:
    current_mouse_position = pyautogui.position()
    if current_mouse_position != old_mouse_position:
        print (f"{current_mouse_position}                  ", end="\r")
        old_mouse_position = current_mouse_position
# ate CTRL-C
# Point(x=1528, y=543)
# Point(x=1876, y=543)
# y=963