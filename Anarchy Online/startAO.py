import os
import pywinauto
import win32gui
import win32api
import win32process
import win32con
import pyautogui
from time import sleep


def window_enum_handler(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))


def get_app_list(handles=[]):
    mlst=[]
    win32gui.EnumWindows(window_enum_handler, handles)
    for handle in handles:
        mlst.append(handle)
    return mlst


def show_apps():
    appwindows = get_app_list()
    for i in appwindows:
        print (i)


def Activate_AO_Client():
    app_path =r"AnarchyOnline.exe"
    fol_path =r"C:\Funcom\Anarchy Online"

    os.chdir(fol_path)
    os.startfile(app_path)
    sleep(1)
    handle = win32gui.FindWindow(0, "End User License Agreement:")  #//paassing 0 as I dont know classname
    win32gui.SetForegroundWindow(handle)  #//put the window in foreground
    pyautogui.press("enter")
    sleep(3)
    pyautogui.press("enter")
    sleep(2)
    handle = win32gui.FindWindow(0, "Anarchy Online")  #//paassing 0 as I dont know classname
    win32gui.SetForegroundWindow(handle)  #//put the window in foreground
    move_AO_window()


def move_AO_window():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 960, 0, 2890, 1660, 0)


def select_acc(avatar=""):
    from lists import alist
    from lists import pas

    for accounts in alist:
        if avatar in accounts[1]:
            # print(acca,acca[1].index(ava))
            account = accounts[0]
            user = accounts[1].index(avatar)

    pyautogui.click(2400,800,clicks=1,button="left")
    pyautogui.press('backspace',presses=30)
    sleep(0.2)
    pyautogui.typewrite(account)

    sleep(0.3)
    pyautogui.click(2400,840,clicks=1,button="left")
    pyautogui.typewrite(pas)
    pyautogui.press('enter')

    sleep(1)
    pyautogui.press('up',presses=8)
    pyautogui.press('down',presses=user)
    pyautogui.press('enter')
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
    lista = ["Saleotra3"] # treader 181
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