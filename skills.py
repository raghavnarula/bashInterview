import time
import pyautogui


skills = ["Python","Django","AWS","JavaScript","React.js","HTML5","CSS","MVC","Express.js","Node.js","Docker","Ruby","Ruby On Rails","Git","Jira","Linux","MySQL","Selenium","TypeScript","Pandas","Apache Jmeter","Matlab","R","Tensorflow","PyTorch"]
for i in skills:
    pyautogui.typewrite(i)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.hotkey('shift','tab')
    # time.sleep(0.5)