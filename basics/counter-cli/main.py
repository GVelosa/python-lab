import time

def main():
    def counter():
        while True:
            try:
                seconds = int(input("Enter the number of seconds for the countdown: "))
                while seconds > 0:
                    print(f"Time remaining: {seconds} seconds", end='\r')
                    time.sleep(1)
                    seconds -= 1
                print("\nTime's up!")
                break
            except ValueError:
                print("Please enter a valid number.")
                return

    counter()

if __name__ == "__main__":
    main()