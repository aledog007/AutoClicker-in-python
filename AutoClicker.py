import time
import threading
import PySimpleGUI as sg
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode


layout = [
    [sg.Text("Press '-' to start/stop the Auto Clicker")],
    [sg.Button("Close Application")]
]

window = sg.Window("Auto Clicker by aledog007", layout, margins=(50, 50))

TOGGLE_KEY = KeyCode.from_char("-")
clicking = False
mouse = Controller()


def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.001) 



def toggle_event(key):
    global clicking
    if key == TOGGLE_KEY:
        clicking = not clicking


click_thread = threading.Thread(target=clicker)
click_thread.daemon = True 
click_thread.start()

# Starte den Tastatur-Listener
with Listener(on_press=toggle_event) as listener:
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Close Application":
            break

window.close()
