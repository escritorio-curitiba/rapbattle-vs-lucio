# Take a screenshot, and get the text out of it.

import pyautogui
from pyautogui import ImageNotFoundException
from pytesseract import pytesseract


def get_lucio_text () -> str:

    # These are the bounds of Lucio's box.
    #   So far, this is the only way we have to change them.
    # (x, y, width, height)
    lucio_region = (1528, 543, 350, 420)

    # Tesseract stuff!
    tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.tesseract_cmd = tesseract_path

    lucio_scrot = pyautogui.screenshot(
        imageFilename=None,
        region=lucio_region,
        allScreens=False
    )

    text = pytesseract.image_to_string(lucio_scrot)

    return text

# Function to track down whereever Lucio is
#   Disactivated for now, we'll just do it manually
def find_lucio (banner_path: str) -> tuple[int, int, int, int] | None:
    screen = pyautogui.screenshot()
    try:
        lucio_banner_location = pyautogui.locateOnScreen(banner_path)
    except ImageNotFoundException:
        print ("ERROR: Lucio not found")
        return None
    print (lucio_banner_location)
    return None

