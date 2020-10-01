import os
import pywinauto
import win32gui
import win32api
import win32process
import win32con
import pyautogui
import keyboard
import mouse
from time import sleep


def window_enum_handler(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))


def get_app_list(handles=[]):
    mlst = []
    win32gui.EnumWindows(window_enum_handler, handles)
    for handle in handles:
        mlst.append(handle)
    return mlst


def show_apps():
    appwindows = get_app_list()
    for i in appwindows:
        print(i)


def Activate_AO_Client():
    app_path = r"AnarchyOnline.exe"
    fol_path = r"C:\Funcom\Anarchy Online"

    os.chdir(fol_path)
    os.startfile(app_path)
    sleep(1)
    handle = win32gui.FindWindow(0, "End User License Agreement:")  # //paassing 0 as I dont know classname
    win32gui.SetForegroundWindow(handle)  # //put the window in foreground

    # pyautogui.press("enter")
    keyboard.press_and_release('enter')
    sleep(3)

    # pyautogui.press("enter")
    keyboard.press_and_release('enter')
    sleep(2)

    handle = win32gui.FindWindow(0, "Anarchy Online")  # //paassing 0 as I dont know classname
    win32gui.SetForegroundWindow(handle)  # //put the window in foreground
    move_AO_window()


def move_AO_window():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 960, 0, 2890, 1660, 0)


def select_acc(avatar=""):
    from lists import alist
    from lists import pas
    account = ""
    user = 0

    # for accounts in alist:
    #     if avatar in accounts[1]:
    #         # print(accounts,accounts[1].index(avatar))
    #         account = accounts[0]
    #         user = accounts[1].index(avatar)

    for accounts in alist:
        x = 0
        for acca in accounts[1]:
            if avatar in acca[0]:
                account = accounts[0]
                user = x
            x += 1
        # if avatar in accounts[1]:
        #     # print(accounts,accounts[1].index(avatar))
        #     account = accounts[0]
        #     user = accounts[1].index(avatar)


    mouse.move(2400, 800, absolute=True, duration=0)
    mouse.click(button='left')
    sleep(0.4)
    for x in range(30):
        keyboard.press_and_release('backspace')

    sleep(0.4)
    keyboard.write(account)

    sleep(0.3)
    mouse.move(2400, 840, absolute=True, duration=0)
    mouse.click(button='left')

    sleep(0.3)
    keyboard.write(pas)

    keyboard.press_and_release('enter')

    sleep(1)
    for x in range(8):
        keyboard.press_and_release('up')

    for x in range(user):
        keyboard.press_and_release('down')

    keyboard.press_and_release('enter')
    sleep(3)


def run_setup(acc_list):
    for acc in acc_list:
        Activate_AO_Client()
        sleep(1)
        select_acc(acc)


if __name__ == "__main__":
    # lista = ["Fixalala","Saleotra3","Mspid"]
    # lista = ["Engiskill","Fixalala"]
    # lista = ["Fixalala", "Stiladv","Ontertop","Saleotra3"]
    # lista = ["Fixalala","Stiladv","Ontertop","Saleotra3","Stilmp"]
    # lista = ["Kriatonita","Saleotra3","Fixalala","Stiladv"]
    # lista = ["Fixalala","Ontertop"]

    # lista = ["Fixalala"] # fixer 200
    # lista = ["Engiskill"] # engineer 200
    # lista = ["Ontertop"] # MA 200
    lista = ["Saleotra3"]  # treader 181
    # lista = ["Stiladv"] # adventurer 120
    # lista = ["Elmanages"] # Soldier 60
    # lista = ["Shivnano"] # bureaucrat 60
    # lista = ["Stilmp"] # MP 60
    # lista = ["Grafunia"] # clan lvl 60 MA
    # lista = ["Moisenf"] # Enforcer 25
    # lista = ["Stilnt"] # NT 23
    # lista = ["Stildocs"] # Doc 34
    # lista = ["Stilcrat"] # bureaucrat 29
    # lista = ["Stilenf"] # Enf 15
    # lista = ["Steamyma"]
    # lista = ["Ramidocs"] # Doc 31

    # lista = ["Mspid"] # MP 60 overtune LOCKED
    # lista = ["Elleffe10"] # fixer 15 LOCKED
    # lista = ["Lvlvlvl2"] # adv 2 LOCKED
    # lista = ["Amanetfix2"] # Arete langind FIXER BUFFER LOCKED start
    # lista = ["Banderlogit"] # Arete langind FIXER BUFFER LOCKED end
    # lista = ["Manoob"] # Arete langind MA LOCKED

    # lista = ["Fixalala","Saleotra3","Mspid"]
    # lista = ["Fixalala","Saleotra3","Stilmp"]
    # lista = ["Manoob","Banderlogit"]

    ######################## - paid - #############
    # lista = ["Kipi-1"]
    # lista = ["Kipi2"]
    # lista = ["Norenmp"]

    run_setup(lista)
