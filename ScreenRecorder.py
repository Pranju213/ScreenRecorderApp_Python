import numpy as np
import pyautogui
import keyboard
import datetime
import cv2

def Screen_record(file_name,fps=30):
    video_size=(pyautogui.size())
    codec=cv2.VideoWriter_fourcc(*"mp4v")
    output=cv2.VideoWriter(file_name,codec,fps,video_size)
    print("Press 'Ctrl+Q' to stop screen recording.")
    while True:
        img=pyautogui.screenshot()
        frame=cv2.cvtColor(np.array(img),cv2.COLOR_RGB2BGR)
        output.write(frame)
        if keyboard.is_pressed('ctrl+q'):
            break
    output.release()
    cv2.destroyAllWindows()
    print("Screen Recording Complete.")
    
if __name__=="__main__":
    current_time=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name=f"screen_record_{current_time}.mp4"
    Screen_record(file_name)