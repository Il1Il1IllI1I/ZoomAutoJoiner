import pyautogui
import schedule
from datetime import datetime
import pytz
import random
import time

def random_sleep():
    sleep_time = random.uniform(1, 2)  # 1초에서 2초 사이의 랜덤한 실수를 생성
    time.sleep(sleep_time)  # 랜덤한 시간 동안 휴식

# 함수를 호출하여 랜덤한 시간 동안 휴식을 취합니다.
random_sleep()

def job():
    # Zoom을 엽니다 (이 부분은 Windows 시스템에 맞춰 수정되었습니다)
    pyautogui.hotkey('win')  # '실행' 대화 상자를 엽니다 (Windows에서)
    random_sleep()
    pyautogui.write('Zoom')
    random_sleep()
    pyautogui.press('enter')
    
    # 몇 초 기다린 후 회의 참가 버튼을 눕니다
    time.sleep(5)
    pyautogui.click(x=958, y=529)  # '회의 참가' 버튼의 위치
    
    # 회의 ID를 입력합니다
    time.sleep(5)
    pyautogui.write('5696409247')
    random_sleep()
    pyautogui.press('enter')
    
    # 비밀번호를 입력합니다
    time.sleep(5)
    pyautogui.write('0705')
    random_sleep()
    pyautogui.press('enter')

# 한국 시간으로 오전 8시 45분에 job 함수를 실행합니다
def run_schedule():
    seoul = pytz.timezone('Asia/Seoul')
    while True:
        current_time = datetime.now(seoul).strftime('%H:%M')
        if current_time == '01:12':
            job()
            time.sleep(60)  # 1분 동안 대기하여 중복 실행을 방지합니다
        time.sleep(1)  # 1초 대기

# 스케쥴러를 실행합니다
run_schedule()
