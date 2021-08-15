import pyautogui
import time
import win32gui


#Win32

GAME_REGION = () # (left, top, width, height)


def getGameRegion():

    global GAME_REGION
    kappa = win32gui.FindWindow(None, 'Timberman')
    win32gui.BringWindowToTop(kappa)
    win32gui.SetForegroundWindow(kappa)
    rect = win32gui.GetWindowRect(kappa)
    GAME_REGION = (rect[0],rect[1],rect[2]-rect[0],rect[3]-rect[1])
    print(GAME_REGION)
    
def pass_main_menu():
    button = pyautogui.locateOnScreen('single_player_button.png', grayscale = True, region=GAME_REGION, confidence=0.7)
    if button is None:
        raise Exception("Can't find singlePlayer button")
    clickButton = pyautogui.center(button)
    pyautogui.click(clickButton)
    

def second_play_button():
    button = pyautogui.locateOnScreen('second_play_button.png', grayscale = True, region=GAME_REGION)
    if button is None:
        raise Exception("Can't find singleplayer button")
    clickButton = pyautogui.center(button)
    pyautogui.click(clickButton)
   
def playing_the_game():
    
    #Something Not working here
    
    
    x1 = GAME_REGION[0] + 218
    x2 = GAME_REGION[0] + 358
    y1 = GAME_REGION[1] + 342

    kappa = pyautogui.screenshot('kappa.png',region=GAME_REGION)
    originalColorL = kappa.getpixel((x1,y1))
    
    while(True):
       
        time.sleep(0.15)
        if(pyautogui.pixelMatchesColor(x1,y1, (originalColorL[0],originalColorL[1],originalColorL[2]))):
            pyautogui.press('left')
            print('L')
            
            
        elif(pyautogui.pixelMatchesColor(x2,y1, (originalColorL[0],originalColorL[1],originalColorL[2]))):
            pyautogui.press('right')
            print('R')
            
            
        else:
            pyautogui.press('left')
            print('else')


def main():
    getGameRegion()
    pass_main_menu()
    time.sleep(.7)
    second_play_button()
    time.sleep(.5)
    playing_the_game()





if __name__ == '__main__':
    main()