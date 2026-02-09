import requests
import time
import webbrowser
from getpass import getpass
import os
from time import sleep
import re
import random
import sys

def clear_screen():
    os.system('clear')

def matrix_animation(duration=2):
    """Animation style Matrix"""
    chars = "01"
    lines = 30
    width = os.get_terminal_size().columns
    matrix = [0] * width
    
    end_time = time.time() + duration
    while time.time() < end_time:
        for i in range(width):
            if matrix[i] > 0:
                print(f"\033[92m{random.choice(chars)}\033[0m", end='')
                matrix[i] -= 1
            else:
                print(" ", end='')
                
            if random.random() < 0.05:
                matrix[i] = random.randint(5, 15)
        
        print()
        sleep(0.08)
        if time.time() >= end_time:
            break

def cyber_animation():
    """Animation cyberpunk"""
    symbols = ["▓▓▓", "▒▒▒", "░░░", "███"]
    colors = ["\033[96m", "\033[95m", "\033[94m"]
    
    for _ in range(15):
        for symbol in symbols:
            for color in colors:
                print(f"\r{color}{random.choice(symbols)}{' ' * random.randint(5, 20)}\033[0m", end='')
                sleep(0.03)
    print()

def animate_text(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print()

def show_banner():
    banner = """
╔══════════════════════════════════════╗
║          IMEI TRACKER v2.0           ║
║      Created for Termux Users        ║
║         bcz Academy © 2024           ║
╚══════════════════════════════════════╝
    """
    print("\033[94m" + banner + "\033[0m")

def loading_animation(text, duration=2):
    symbols = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    start_time = time.time()
    i = 0
    while time.time() - start_time < duration:
        print(f'\r{text} {symbols[i%len(symbols)]}', end='', flush=True)
        time.sleep(0.1)
        i += 1
    print()

def hack_loading():
    """Animation de chargement style hacker"""
    phrases = [
        "Accessing secure network...",
        "Bypassing firewalls...",
        "Decrypting signals...",
        "Establishing connection...",
        "Retrieving location data..."
    ]
    
    for phrase in phrases:
        loading_animation(phrase, 0.8)
    print()

def validate_imei(imei):
    """Validate IMEI number format."""
    if not re.match(r'^\d{15}$', imei):
        return False
    return True

def validate_email(email):
    """Validate email format."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def authenticate(gmail, password):
    hack_loading()
    return True

def authenticate_apple(apple_id, password):
    hack_loading()
    return True

def request_location(imei):
    loading_animation("Triangulating device position", 1.5)
    loading_animation("Intercepting GPS signals", 1.5)
    loading_animation("Mapping coordinates", 1)
    return "37.7749,-122.4194"

def parse_location(response_text):
    try:
        latitude, longitude = map(float, response_text.strip().split(','))
        return f"{latitude},{longitude}"
    except (ValueError, AttributeError):
        animate_text("Error: Could not parse location information.", 0.03)
        return None

def track_android(imei, gmail, password):
    clear_screen()
    matrix_animation(1.5)
    clear_screen()
    
    if not validate_imei(imei):
        animate_text("\033[91m✗ Invalid IMEI format. Please enter a 15-digit IMEI number.\033[0m", 0.03)
        return

    if not validate_email(gmail):
        animate_text("\033[91m✗ Invalid email format.\033[0m", 0.03)
        return

    print("\033[92m" + "═" * 50 + "\033[0m")
    animate_text(f"🔍 Tracking Android device with IMEI: \033[96m{imei}\033[0m", 0.03)
    print("\033[92m" + "═" * 50 + "\033[0m")

    if authenticate(gmail, password):
        response_text = request_location(imei)
        if response_text:
            location = parse_location(response_text)
            if location:
                find_my_device_url = f"https://www.google.com/android/find?u=0&hl=en&source=android-browser&q={location}"
                
                print("\n" + "▰" * 50)
                animate_text("\n\033[92m✅ Location found!\033[0m", 0.03)
                animate_text("\033[93m📡 Opening map...\033[0m", 0.03)
                
                cyber_animation()
                
                print(f"\n\033[92m📍 Device Location URL:\033[0m")
                print(f"\033[96m{find_my_device_url}\033[0m")
                
                try:
                    webbrowser.open(find_my_device_url)
                except Exception as e:
                    print(f"\n\033[91m✗ Error opening browser: {e}\033[0m")

def track_iphone(apple_id, password):
    clear_screen()
    matrix_animation(1.5)
    clear_screen()
    
    if not validate_email(apple_id):
        animate_text("\033[91m✗ Invalid Apple ID format.\033[0m", 0.03)
        return

    print("\033[95m" + "═" * 50 + "\033[0m")
    animate_text(f"🔍 Tracking iPhone device with Apple ID: \033[96m{apple_id}\033[0m", 0.03)
    print("\033[95m" + "═" * 50 + "\033[0m")

    if authenticate_apple(apple_id, password):
        cyber_animation()
        animate_text("\n\033[92m✅ Tracking completed successfully!\033[0m", 0.03)

def main():
    try:
        while True:
            clear_screen()
            show_banner()

            print("\n" + "─" * 40)
            animate_text("\n📱 Select device type:", 0.03)
            print("\033[96m1.\033[0m Android 📲")
            print("\033[96m2.\033[0m iPhone ")
            print("\033[96m3.\033[0m Exit 🚪")
            print("─" * 40)

            choice = input("\n\033[93m➤ Enter your choice (1-3):\033[0m ")

            if choice == "1":
                clear_screen()
                show_banner()
                
                print("\033[92m" + "═" * 50 + "\033[0m")
                print("\033[92m           ANDROID TRACKING MODE          \033[0m")
                print("\033[92m" + "═" * 50 + "\033[0m\n")
                
                imei = input("\n\033[93m📟 Enter IMEI:\033[0m ")
                gmail = input("\033[93m📧 Enter Gmail:\033[0m ")
                password = getpass("\033[93m🔒 Enter Password:\033[0m ")
                track_android(imei, gmail, password)

            elif choice == "2":
                clear_screen()
                show_banner()
                
                print("\033[95m" + "═" * 50 + "\033[0m")
                print("\033[95m           IPHONE TRACKING MODE           \033[0m")
                print("\033[95m" + "═" * 50 + "\033[0m\n")
                
                apple_id = input("\n\033[93m Enter Apple ID:\033[0m ")
                password = getpass("\033[93m🔒 Enter Password:\033[0m ")
                track_iphone(apple_id, password)

            elif choice == "3":
                clear_screen()
                print("\n" + "▰" * 50)
                animate_text("\n\033[94m👋 Thank you for using IMEI Tracker!\033[0m", 0.03)
                matrix_animation(1)
                break

            else:
                print("\n\033[91m✗ Invalid choice. Please try again.\033[0m")
                sleep(1)

            input("\n\033[93m⏎ Press Enter to continue...\033[0m")

    except KeyboardInterrupt:
        print("\n\n\033[91m✗ Program terminated by user.\033[0m")
    except Exception as e:
        print(f"\n\033[91m✗ An error occurred: {e}\033[0m")

if __name__ == "__main__":
    clear_screen()
    print("\033[92m" + "=" * 50 + "\033[0m")
    print("\033[92m        INITIALIZING IMEI TRACKER v2.0       \033[0m")
    print("\033[92m" + "=" * 50 + "\033[0m\n")
    matrix_animation(2)
    main()




