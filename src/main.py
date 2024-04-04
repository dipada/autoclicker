import pyautogui
import time
import keyboard
import tkinter as tk

START_SHORTCUT = "F4"
STOP_SHORTCUT = "F6"
CLICK_INTERVAL = 0.5 # Seconds

def autoclick(click_interval):
    try:
        while True:
            pyautogui.click()
            time.sleep(click_interval)
            if keyboard.is_pressed(STOP_SHORTCUT):
                break
    except KeyboardInterrupt:
        print("Autoclicker terminated.")

def start_autoclick():
    autoclick(CLICK_INTERVAL)

def start_clicker_from_button():
    autoclick(CLICK_INTERVAL)

def stop_clicker_from_button():
    print("Autoclicker stopped.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Autoclicker GUI - by dipada")
    root.minsize(400, 200)
    
    start_button = tk.Button(root, text=f"Start Autoclicker ({START_SHORTCUT})", command=start_clicker_from_button)
    start_button.pack(pady=10)

    stop_button = tk.Button(root, text=f"Stop Autoclicker ({STOP_SHORTCUT})", command=stop_clicker_from_button)
    stop_button.pack(pady=10)

    root.bind(f"<{START_SHORTCUT.upper()}>", lambda event: start_clicker_from_button())
    root.bind(f"<{STOP_SHORTCUT.upper()}>", lambda event: stop_clicker_from_button())

    root.mainloop()
