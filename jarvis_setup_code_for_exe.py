import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.

#pass packages in list becuz some packages wont import and show an error better to add the package name we used in code to avoid error conflict

build_exe_options = {"packages": ["pyttsx3","speech_recognition","datetime",'os',"cv2","time","random","pywhatkit",
                                  "pyautogui","requests","bs4","wikipedia","webbrowser","pydub","mediapipe","psutil","numpy","sys"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"


setup(
    name = "jarvis_exe_code.py",   #write code name here
    version = "0.1",
    description = "My jarvis application!", #description,version is ur wish
    options = {"build_exe": build_exe_options},#builds and downloads the packages we mentioned
    executables = [Executable("jarvis_exe_code.py", base=base)] #here our code name should be their
)


'''after completion of code write the following command in terminal or cmd(path should be of code location(pycharms) )'''
#python filename.py build(filename should be this code name)

#python jarvis_setupcodefor_exe.py build

#exe file will be created in the specified location later add video,audio,image files, zip it and send to clients
