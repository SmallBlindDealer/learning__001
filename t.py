from pynput.mouse import Button, Controller
import time
c = 0
obj = Controller()
while True:
    x, y  = obj.position
    print("->--->", c, x, y)
    obj.click(Button.left)
    c+=1

    time.sleep(5)