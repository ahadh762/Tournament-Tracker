def Validate_Input(message, input_type):
    valid_value = False
    if input_type == 'number':
        while valid_value == False:
            try:
                user_input = int(input(message))
                valid_value = True
                return user_input
            except ValueError:
                print()
                print("Error: Invalid input.\n")
                continue
    

def StartUp():
    print()
    print("Welcome to Tournaments R Us\n============================")
    message = "Enter number of participants: "
    global num_participants
    global participant_dict

    num_participants = Validate_Input(message, 'number')
    while num_participants <= 1:
        print()
        print('Error: The number of participants must be more than 1!\n')
        num_participants = Validate_Input(message, 'number')

    print(f"There are {num_participants} participant slots ready for sign-ups.\n\n")

    participant_dict = {}
    for i in range(1,num_participants+1):
        participant_dict.update({i:None}) 


def SignUp(run_number = 1):
    global participant_name
    if run_number == 1:
        print("Participant Sign Up\n====================")
        participant_name = input("Participant Name: ")
    slot_message = f"Desired starting slot #[1-{num_participants}]: "
    starting_slot = Validate_Input(slot_message, 'number')

    while starting_slot < 1 or starting_slot > num_participants:
        print()
        print('Error: Out of range!\n')
        starting_slot = Validate_Input(slot_message, 'number')
    print()
    if participant_dict[starting_slot] != None:
        print(f"Error:\nSlot #{starting_slot} is filled. Please try again.\n")
        SignUp(2)
    else:
        participant_dict[starting_slot] = participant_name

StartUp()
SignUp()
