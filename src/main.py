import pyautogui
import time
import threading
import tkinter as tk

START_SHORTCUT = "F4"
STOP_SHORTCUT = "F6"
DEFAULT_INTERVAL = 0.5  # lick interval in Seconds
autoclick_thread = None 
stop_event = threading.Event()

def autoclick(click_interval):
    try:
        while not stop_event.is_set():
            pyautogui.click()
            time.sleep(click_interval)
    except KeyboardInterrupt:
        print("Autoclicker terminated.")

def start_clicker_from_button(interval_entry):
    global autoclick_thread
    if autoclick_thread and autoclick_thread.is_alive():
        print("Autoclicker is already running.")
        return

    try:
        click_interval = float(interval_entry.get())
    except ValueError:
        click_interval = DEFAULT_INTERVAL

    global stop_event
    stop_event.clear()
    autoclick_thread = threading.Thread(target=autoclick, args=(click_interval,), daemon=True)
    autoclick_thread.start()

def stop_clicker_from_button():
    global autoclick_thread
    global stop_event
    if autoclick_thread:
        stop_event.set() 
        print("Autoclicker stopped.")
    else:
        print("Autoclicker not running.")

def on_interval_change(event):
    try:
        click_interval = float(interval_entry.get())
    except ValueError:
        print("Invalid input. Using default interval.")
        click_interval = DEFAULT_INTERVAL
    start_clicker_from_button(interval_entry)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Autoclicker GUI - by dipada")
    root.minsize(400, 250)

    interval_label = tk.Label(root, text="Click Interval (in seconds):")
    interval_label.pack(pady=10)

    interval_entry = tk.Entry(root)
    interval_entry.insert(0, str(DEFAULT_INTERVAL))
    interval_entry.pack()

    start_button = tk.Button(root, text=f"Start Autoclicker ({START_SHORTCUT})", command=lambda: start_clicker_from_button(interval_entry))
    start_button.pack(pady=5)

    stop_button = tk.Button(root, text=f"Stop Autoclicker ({STOP_SHORTCUT})", command=stop_clicker_from_button)
    stop_button.pack(pady=5)

    interval_entry.bind("<Return>", on_interval_change)
    interval_entry.bind("<FocusOut>", on_interval_change)

    root.bind(f"<{START_SHORTCUT.upper()}>", lambda event: start_clicker_from_button(interval_entry))
    root.bind(f"<{STOP_SHORTCUT.upper()}>", lambda event: stop_clicker_from_button)

    root.mainloop()
