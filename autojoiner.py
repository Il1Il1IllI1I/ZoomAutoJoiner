import pyautogui
import random
import time
from datetime import datetime
import pytz

def random_sleep():
    time.sleep(random.uniform(1, 2))

def perform_action(action, *args, **kwargs):
    action(*args, **kwargs)
    random_sleep()

def job():
    perform_action(pyautogui.hotkey, 'win')
    perform_action(pyautogui.write, 'Zoom')
    perform_action(pyautogui.press, 'enter')

    time.sleep(5)
    perform_action(pyautogui.click, x=958, y=529)

    time.sleep(5)
    perform_action(pyautogui.write, '5696409247')
    perform_action(pyautogui.press, 'enter')

    time.sleep(5)
    perform_action(pyautogui.write, '0705')
    perform_action(pyautogui.press, 'enter')

def run_schedule():
    seoul = pytz.timezone('Asia/Seoul')
    while True:
        if datetime.now(seoul).strftime('%H:%M') == '01:19':
            job()
            time.sleep(60)
        time.sleep(1)

if __name__ == "__main__":
    run_schedule()
