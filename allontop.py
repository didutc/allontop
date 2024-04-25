import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
from pynput import keyboard
import sys
from pynput.mouse import Listener, Button
import keyboard
import win32gui
import win32con
import time
import pyzard

que = []
def on_quit(icon, item):
    print("종료 버튼을 눌러 프로그램을 종료합니다.")
    # 여기에 종료 전에 수행할 작업을 추가하세요
    for hwnd in que:
        try:
            win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                                win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        except:
            continue
    icon.stop()
def my_function():
    global que
    print("특정 함수가 실행되었습니다.")
    flags, hcursor, (x, y) = win32gui.GetCursorInfo()
    hwnd = win32gui.WindowFromPoint((x, y))
    
    if hwnd not in que:
 
        print(que)
        que.append(hwnd)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    else:
        
        print(que)
        que = pyzard.lst_comprehension(que,hwnd)

        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


# 아이콘 클릭 시의 동작
def on_clicked(icon, item):
    print("아이콘 클릭됨")

# 키 이벤트 핸들러
def on_click(x, y, button, pressed):
    global que
    if pressed:

        if keyboard.is_pressed('ctrl') and button == Button.left:

            my_function()
# 키보드 리스너 시작
def start_keyboard_listener():
    listener = Listener(on_click=on_click)
    listener.start()

# 아이콘 초기화
def initialize_icon():
    icon = pystray.Icon("아이콘 이름")
    icon.title = "항상위" 
    icon.icon = Image.open("icon.png")  # 아이콘 이미지 파일명
    icon.menu = [ item('종료', on_quit)]
    return icon

# 시스템 트레이 아이콘 실행
def run_tray_icon():
    icon = initialize_icon()
    start_keyboard_listener()
    icon.run()

if __name__ == "__main__":
    run_tray_icon()