def StartUp():
    print("Welcome to Tournaments R Us\n============================")
    valid_value = False
    while valid_value == False:
        try:
            num_participants = int(input("Enter number of participants: "))
            valid_value = True
        except ValueError:
            print("Invalid input.", end = " ")
            continue
    print()
    print(f"There are {num_participants} participant slots ready for sign-ups.")