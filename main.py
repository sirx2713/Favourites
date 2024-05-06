stopped = False
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Already started moving!")
        else:
            started = True
            print("Started moving")
    elif command == "stop":
        if stopped:
            print("Already stopped!")
        else:
            stopped = True
            print("Stopped moving.")
    elif command == "status":
        if started and not stopped:
            print("Moving!")
        elif stopped:
            print("Stopped!")
        else:
            print("Parked!")
