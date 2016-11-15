import subprocess
import threading
import time

def main():
    subprocess.call(['python', 'initMain.py'])

def rot():
    subprocess.call(['python', 'Rotary.py'])


t1=threading.Thread(target=rot)
t1.start()
t2=threading.Thread(target=main)
t2.start()

while True:
    time.sleep(10)
