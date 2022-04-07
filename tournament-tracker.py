def Validate_Input(message, input_type, num_participants = 1):

    valid_value = False

    if input_type == 'number':
        while valid_value == False:
            try:
                user_input = int(input(message))
                if (user_input < 1 or user_input > num_participants) and num_participants != 1:
                    print()
                    print('Error: Out of range!\n')
                elif user_input <= 1 and num_participants == 1:
                    print()
                    print('Error: The number of participants must be more than 1!\n')
                else:
                    valid_value = True
                    return user_input
            except ValueError:
                print()
                print("Error: Invalid input.\n")
                continue
    

def StartUp():

    global participant_dict
    global num_participants

    print()
    print("Welcome to Tournaments R Us\n============================")
    message = "Enter number of participants: "

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
    starting_slot = Validate_Input(slot_message, 'number', num_participants)

    if participant_dict[starting_slot] != None:
        print()
        print(f"Error:\nSlot #{starting_slot} is filled. Please try again.\n")  
        SignUp(2)
    else:
        print()
        print(f"Success:\n{participant_name} is signed up in starting slot #{starting_slot}.")
        participant_dict[starting_slot] = participant_name
    print()


def CancelSignUp(run_number = 1):

    print()
    if run_number == 1:
        print("Participant Cancellation\n========================")

    cancel_message = f"Starting slot #[1-{num_participants}]: "
    cancel_slot = Validate_Input(cancel_message, 'number', num_participants)
    cancel_name = input("Participant Name: ")
    print()

    if participant_dict[cancel_slot] != cancel_name:
        print(f"Error:\n{cancel_name} is not in that starting slot.")  
        CancelSignUp(2)
    else:
        print(f"Success:\n{cancel_name} has been cancelled from starting slot #{cancel_slot}.")
        participant_dict[cancel_slot] = None


StartUp()
SignUp()
CancelSignUp()
