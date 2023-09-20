import pyautogui
import time

def job():
    # Zoom을 엽니다 (이 부분은 Windows 시스템에 맞춰 수정되었습니다)
    pyautogui.hotkey('win')  # '실행' 대화 상자를 엽니다 (Windows에서)
    time.sleep(1)
    pyautogui.write('Zoom')
    pyautogui.press('enter')

job()
