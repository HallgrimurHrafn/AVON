import Main
import menu
import Rotary
import Render
import subprocess
import threading

t1=threading.Thread(target=rot)
t1.start()
t2=threading.Thread(target=main)
t2.start()

def rot(channel):
    subprocess.call(['python', 'Rotary.py'])

def main(channel):
    subprocess.call(['python', 'Main.py'])

while True:
    pass
