from pynput.mouse import Listener, Button, Controller
import time

mouse = Controller()
stop_code = False

def on_click(x, y, button, pressed):
    stop_code = True
    mouse_position = mouse.position
    print('\nMouse clicked at position {0}, {1}'.format(int(mouse_position[0]), int(mouse_position[1])))

    test_clicks = input('\nPlease enter number of test clicks: ')
    delay_clicks = input('Please enter the delay in seconds between clicks: ')

    print('\nStarting automated clicks in 5 seconds, make sure to click on the test window......')
    time.sleep(5)
    mouse.position = (int(mouse_position[0]), int(mouse_position[1]))
    mouse.click(Button.left, 1)

    for click in range (0, int(test_clicks)):
        print('Click Test No: {0}'.format(click+1))
        mouse.position = (int(mouse_position[0]), int(mouse_position[1]))
        mouse.click(Button.left, 1)
        time.sleep(int(delay_clicks))


    print('\nTest clicks ready......\n')
    stop_code = False
    exit()

if stop_code == False:
    print('\nClick on test element.....')
    with Listener(on_click=on_click) as listener:
        listener.join()