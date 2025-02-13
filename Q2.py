"""
Q2: Write a Python script to monitor the CPU usage of a local machine and display an alert message if the usage exceeds a predefined threshold. The script should continuously monitor the CPU usage and provide real-time alerts when the usage exceeds the threshold. Include appropriate error handling to handle exceptions that may arise during the monitoring process.

"""
import psutil
import time
from os import system, name

def clear_screen():
    # cls for windows, clear for mac/linux
    system('cls' if name == 'nt' else 'clear')

def show_usage(usage, limit):
    # Simple visual meter using hashtags
    meter = '#' * int(usage/5)  # each # = 5%
    spaces = ' ' * (20 - len(meter))  # pad to 20 chars
    return f"[{meter}{spaces}] {usage:.1f}%"

def monitor():
    # Set limit at 80% - common threshold for most systems
    limit = 80
    
    print("CPU Monitor - Press Ctrl+C to exit")
    print("-" * 40)
    
    while True:
        try:
            clear_screen()
            
            # Get CPU % - interval=1 means average over 1 sec
            cpu = psutil.cpu_percent(interval=1)
            
            # Show current usage with visual meter
            print(f"\nCurrent CPU: {show_usage(cpu, limit)}")
            
            # Simple alert if we're running hot
            if cpu >= limit:
                print("! High CPU usage detected !")
            
            time.sleep(1)  # don't hammer the CPU
            
        except KeyboardInterrupt:
            print("\nMonitor stopped")
            break
        except:
            print("\nSomething went wrong - retrying...")
            time.sleep(2)

# Standard Python idiom for script vs import
if __name__ == "__main__":
    monitor() 