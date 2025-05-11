import keyboard
import time
import sys

def check_requirements():
    try:
        import keyboard
    except ImportError:
        print("Error: keyboard library is not installed")
        print("Install it using command: pip install keyboard")
        sys.exit(1)

def spam_message():
    print("You have 5 seconds to switch to the desired window...")
    print("Press Ctrl + C to stop")
    time.sleep(5)
    
    try:
        while True:
            # Type the message
            keyboard.write("your message")
            # Press Enter
            keyboard.press_and_release('enter')
            # Delay between messages
            time.sleep(0.01)
            
    except KeyboardInterrupt:
        print("\nSpam stopped!")

if __name__ == "__main__":
    check_requirements()
    spam_message() 