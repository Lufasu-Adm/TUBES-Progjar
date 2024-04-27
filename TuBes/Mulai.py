import subprocess
import platform
import time


def run_command_in_terminal(command):
    if platform.system() == "Windows":
        subprocess.Popen(["start", "cmd", "/k", command], shell=True)
    elif platform.system() == "Linux":
        subprocess.Popen(["x-terminal-emulator", "-e", command])
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", "-a", "Terminal", command])
    else:
        print("Platform tidak mendukung!")


commands = [
    "python server.py",
    "python client_1.py",
    "python client_2.py",
    "python client_3.py",
    "python client_4.py",
    "python client_5.py",
    "python client_6.py",
    "python client_7.py",
    "python client_8.py",
    "python client_9.py",
    "python client_10.py",
]

for command in commands:
    run_command_in_terminal(command)
    time.sleep(1)