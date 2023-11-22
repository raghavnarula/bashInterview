import sys
import time
import pyautogui
 
# final = pyautogui.hotkey('ctrl', 'v')

final = f'''
Hey Isaac, 
I hope this message finds you well. My name is Raghav Narula, and I am currently a Masters of Computer Science student at North Carolina State University.
 
I am reaching out to express my strong interest in working at {sys.argv[1]}.
 
My academic background, coupled with my hands-on experience has equipped me with a solid foundation in software development, testing, and Machine Learning. I have attached my resume for your reference. 
 
Would it be possible to  discuss potential summer internship opportunities at {sys.argv[1]} starting 2024?
'''
time.sleep(0.2)
pyautogui.typewrite(final)

