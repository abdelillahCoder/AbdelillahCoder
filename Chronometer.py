import time

def countdown_timer():
    seconds = int(input("Enter the countdown time in seconds: "))
    
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = f"{mins:02}:{secs:02}"
        print(time_format, end="\r")  # Overwrite previous output
        time.sleep(1)
        seconds -= 1
    
    print("\nTime's up!")

def stopwatch():
    print("Press Enter to start the stopwatch. Press Enter again to stop.")
    input("Press Enter to start...")
    start_time = time.time()
    input("Press Enter to stop...")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    mins, secs = divmod(int(elapsed_time), 60)
    print(f"Elapsed time: {mins:02}:{secs:02}")

def main():
    print("1. Countdown Timer")
    print("2. Stopwatch")
    choice = input("Select a mode (1 or 2): ")

    if choice == "1":
        countdown_timer()
    elif choice == "2":
        stopwatch()
    else:
        print("Invalid choice. Please try again.")

main()


