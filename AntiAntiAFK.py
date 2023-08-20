import subprocess
import time
import random
import datetime

def checkTime():
    currentTime = datetime.datetime.now()
    if currentTime.hour == 1:
        print("[", currentTime.hour, ":", currentTime.minute, ":", currentTime.second, "]", "Quitting...")
        exit(0)

def hold_key(key, duration):
    subprocess.run(["xdotool", "keydown", key])
    time.sleep(duration)
    subprocess.run(["xdotool", "keyup", key])
def move_mouse_by_offset(x_offset, y_offset):
    subprocess.run(["xdotool", "mousemove_relative", "--", str(x_offset), str(y_offset)])

try:
    numOfTimesRan = 0
    time.sleep(3)
    while True:
        numOfTimesRan = numOfTimesRan + 1
        randomKey = random.choice(['w', 's', 'a', 'd'])
        hold_key(randomKey, 0.2)
        move_mouse_by_offset(random.randint(20, 1920), 0)
        currentTime = datetime.datetime.now()
        print ("[", currentTime.hour, ":", currentTime.minute, ":", currentTime.second, "]", "Waiting...")
        checkTime()
        time.sleep(random.randint(300, 900))

except KeyboardInterrupt:
    print("\nStopped.")