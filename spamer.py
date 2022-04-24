import pyautogui, time, os

onexploit = 'onexploit~# '
def menu():
    print('''
    [1] -> spamer
    [99] -> exit
    ''')
menu()
typer = int(input(onexploit))

def spamer():
    
    time.sleep(3)
    with open('message.txt', 'r') as file:
        word = file.read()
        while True:
            for i in word:
                pyautogui.typewrite(i)
#                pyautogui.press('enter')

def exiit():
    exit()
if typer == 1:
    spamer()
elif typer == 99:
    exiit()
else:
    os.system('cls')
    menu()


