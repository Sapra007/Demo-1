import time

def countdown_timer(seconds):
    while seconds > 0:
        mins,secs = divmod(seconds, 60)
        timer = (f"{mins:02}:{secs:02}")
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

# Example usage
countdown_timer(10) # Countdown from 10 seconds