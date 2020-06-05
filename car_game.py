command = ""

started = False

while True:
    command = input("What do you want to do ? :").lower()

    if command == "start":
        if started:
            print("Car is already started.")
        else:
            started = True
            print("Car Starts")

    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stops")

    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to finish the game
        """)
    elif command == "quit":
        print("bye~~~")
        break
    else:
        print("I don't understand that !!")
