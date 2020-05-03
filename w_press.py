from pynput.keyboard import Key, Listener, Controller
from win32gui import GetWindowText, GetForegroundWindow
import threading 
import time
import sys, os

debugEnable = False 
# change this value to True to enable debugging

desired_window_name = "WoT Blitz"
esc = False
alt = False
checkWindow = True
wFlag = False
t1, log = None, None       # initial dummy value

if debugEnable == True:
    log = open('keypress.txt','w')
    
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

def press_W(c1):
    while wFlag == True:
        #time.sleep(0.05)   # idk if it is required or not
        c1.press('w')
    c1.release('w')
    return

c1 = Controller()
def on_press(key):
    global alt, checkWindow, wFlag, t1
    print('{0} pressed'.format(key))
    
    if key == Key.alt_l:
        print('Alt_L pressed\nk:',key.name,'val:',key.value)
        alt = True
    elif key == Key.tab:
        print('TAB pressed')
        if alt == True:
            checkWindow = True
            alt = False
            return False
    
    #elif hasattr(key, 'char'):
    if hasattr(key, 'char'):
        alt = False
        if key.char == 'q':
            print('Q PRESSED')
            if wFlag == False:
                t1 = threading.Thread(target=press_W, args=(c1,))
                wFlag = True
                t1.start()
            elif wFlag == True:
                wFlag = False
                t1.join()
            
        elif key.char == 's':
            if wFlag == True:              
                wFlag = False
                t1.join()
    log.write(str(key)+'\n')

def on_release(key):
    global esc
    # Stop listener on esc key
    if key == Key.esc:
        esc = True
        return False

if debugEnable == False
    blockPrint()

while True:
    current_window = (GetWindowText(GetForegroundWindow()))
    if desired_window_name in current_window:
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
            if checkWindow == True:
                checkWindow = False
                continue
            if esc == True:
                break
            continue

