def StartUp():
    print("Welcome to Tournaments R Us\n============================")
    valid_value = False
    while valid_value == False:
        try:
            global num_participants
            num_participants = int(input("Enter number of participants: "))
            valid_value = True
        except ValueError:
            print("Invalid input.")
            continue
    print()
    print(f"There are {num_participants} participant slots ready for sign-ups.")

    participant_dict = {}
    for i in range(1,num_participants+1):
        participant_dict.update({i:None}) 



def SignUp():

    print("Participant Sign Up\n====================")
    participant_name = input("Participant Name: ")
    starting_slot = input(f"Desired starting slot #[1-{num_participants}]: ")


StartUp()
SignUp()