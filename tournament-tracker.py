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

    if input_type == 'string':
        while valid_value == False:
            user_input = input(message)
            if user_input == 'y' or user_input == 'n':
                valid_value == True
                return user_input
            else:
                print("Error: Invalid input.\n")

def StartUp():

    global participant_dict
    global num_participants
    global save_state

    print()
    print("Welcome to Tournaments R Us\n============================")
    message = "Enter number of participants: "

    num_participants = Validate_Input(message, 'number')

    print(f"There are {num_participants} participant slots ready for sign-ups.\n\n")

    participant_dict = {}
    for i in range(1,num_participants+1):
        participant_dict.update({i:None}) 

    save_state = 0


def SignUp(run_number = 1):

    global participant_name
    global save_state

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

    save_state = 0

def CancelSignUp(run_number = 1):

    global save_state

    print()

    counter = 0
    for key in participant_dict.keys():
        if participant_dict[key] is not None:
            counter+=1

    if run_number == 1:
        print("Participant Cancellation\n========================")

    if counter != 0:
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
            print()

        save_state = 0

    else:
        print("Participant slots are empty. There is nothing to cancel!\n")

def ViewParticipants():

    global save_state

    print()
    print("View Participants\n=================")
    view_message = f"Starting slot #[1-{num_participants}]: "
    view_slot = Validate_Input(view_message, 'number', num_participants) - 1  # Subtract 1 because dictionary indexing starts from 0
    print()
    print("Starting Slot: Participant")
    dictionary = list(participant_dict)

    if view_slot < 5:
        participants_list = dictionary[0:view_slot+6]
    elif num_participants - view_slot < 5:
        participants_list = dictionary[view_slot-5: num_participants]
    else:
        participants_list = dictionary[view_slot-5:view_slot+6]
    
    for item in participants_list:
        if participant_dict[item] == None:
            print(f"{item}: [empty]")
        else:
            print(f"{item}: {participant_dict[item]}")
    
    save_state = 0

def SaveChanges():
    global save_state

    print()
    print("Save Changes\n============")
    save_message = ("Save your changes to CSV? [y/n]: ")
    save_input = Validate_Input(save_message, 'string')
    dict_copy = participant_dict
    
    if save_input == 'y':
        for key in dict_copy:
            if dict_copy[key] is None:
                dict_copy[key] = "[empty]"

        participants_list = [str(key) + "," + dict_copy[key] for key in dict_copy.keys()]
        with open('tournament-tracker.csv','w') as file:
            file.write("Slot, Participant Name\n")
            file.write("\n".join(participants_list))
            file.close()
        save_state = 1
    else:
        save_state = 0
    print()

    
def Exit():
    global save_state

    print()
    print("Exit\n=====")
    if save_state == 0:
        print('Any unsaved changes will be lost.')
    end_message = ("Are you sure you want to exit? [y/n]: ")
    end_input = Validate_Input(end_message, 'string')

    if end_input == 'y':
        print()
        print("Goodbye!")

StartUp()
SignUp()
CancelSignUp()
ViewParticipants()
SaveChanges()
Exit()