import pyautogui
import random
import time
from datetime import datetime
import pytz

# 전역 변수로 회의 ID, 암호, 실행 시간을 저장
meeting_id = ""
meeting_password = ""
execution_time = ""

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
    perform_action(pyautogui.write, meeting_id)
    perform_action(pyautogui.press, 'enter')

    time.sleep(5)
    perform_action(pyautogui.write, meeting_password)
    perform_action(pyautogui.press, 'enter')

def run_schedule():
    global meeting_id, meeting_password, execution_time
    
    meeting_id = input("회의 ID 또는 개인 링크 이름 : ")
    meeting_password = input("회의 암호 : ")
    execution_time = input("실행할 시간 (HH:MM 형식으로 입력) : ")
    
    seoul = pytz.timezone('Asia/Seoul')
    while True:
        if datetime.now(seoul).strftime('%H:%M') == execution_time:
            job()
            time.sleep(60)
        time.sleep(1)

if __name__ == "__main__":
    run_schedule()
