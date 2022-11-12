import pyautogui, pyperclip, time, random
print("\nTool Spam Password v1.0")
m = (input("press any key..."))

#Chuẩn bị
print("\nChuan bi")
for i in range(5,0,-1):
    print(i,end=" ",flush=True)
    time.sleep(1)
print("\nBat dau")
#Spam
for j in range(112616,1000000):
    pyperclip.copy(j)
    print(j)
    pyautogui.hotkey("ctrl","v")
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    #time.sleep(m) #Delay
