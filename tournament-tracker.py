def Validate_Input(message, input_type, range_of_values = 1):

    valid_value = False

    if input_type == 'number':
        while valid_value == False:
            try:
                user_input = int(input(message))
                if (user_input < 1 or user_input > range_of_values) and range_of_values != 1:
                    print()
                    print('Error: Out of range!\n')
                elif user_input <= 1 and range_of_values == 1:
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
                print()
                print("Error: Invalid input.\n")

def Start_Up():

    global participant_dict
    global num_participants
    global save_state

    print()
    print("Welcome to Tournaments R Us\n============================")
    message = "Enter number of participants: "

    num_participants = Validate_Input(message, 'number')

    print(f"There are {num_participants} participant slots ready for sign-ups.\n")

    participant_dict = {}
    for i in range(1,num_participants+1):
        participant_dict.update({i:None}) 

    save_state = 0


def Sign_Up(run_number = 1):

    global participant_name
    global save_state
    global counter

    if run_number == 1:
        counter = 0
        for key in participant_dict.keys():
            if participant_dict[key] is None:
                counter+=1
        if counter != 0:
            print("Participant Sign Up\n====================")
            participant_name = input("Participant Name: ")

    if run_number == 3:
        counter = 0
        for key in participant_dict.keys():
            if participant_dict[key] is None:
                counter+=1
        if counter != 0:
            participant_name = input("Participant Name: ")


    if counter == 0:
        print("Participant List is full!\n")
        Main_Menu()
    else:
        slot_message = f"Desired starting slot #[1-{num_participants}]: "
        starting_slot = Validate_Input(slot_message, 'number', num_participants)

        if participant_dict[starting_slot] != None:
            print()
            print(f"Error:\nSlot #{starting_slot} is filled. Please try again.\n")  
            Sign_Up(2)
        else:
            print()
            print(f"Success:\n{participant_name} is signed up in starting slot #{starting_slot}.")
            participant_dict[starting_slot] = participant_name

    if counter != 0:
        repeat_message = "Would you like to sign up another person? (y/n): "
        sign_up_another = Validate_Input(repeat_message, 'string')
        if sign_up_another == 'y':
            print()
            Sign_Up(3)
        else: 
            Main_Menu()
    

    print()
    save_state = 0


def Cancel_Sign_Up(run_number = 1):

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
            Cancel_Sign_Up(2)
        else:
            print(f"Success:\n{cancel_name} has been cancelled from starting slot #{cancel_slot}.")
            participant_dict[cancel_slot] = None
            print()

        save_state = 0

    else:
        print("Participant slots are empty. There is nothing to cancel!\n\n")
    
    Main_Menu()

def View_Participants():

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
    Main_Menu()


def Save_Changes():
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
    Main_Menu()

    
def Exit():
    global save_state
    global end_input

    print()
    print("Exit\n=====")
    if save_state == 0:
        print('Any unsaved changes will be lost.')
    end_message = ("Are you sure you want to exit? [y/n]: ")
    end_input = Validate_Input(end_message, 'string')

    if end_input == 'n':
        Main_Menu()
    elif end_input == 'y':
        print()
        print("Goodbye!")



def Main_Menu():
    print()
    print("Participant Menu\n================")
    print("1. Sign Up\n2. Cancel Sign Up\n3. View Participants\n4. Save Changes\n5. Exit\n")
    menu_message = ("Select an option to continue: ")
    menu_selection = Validate_Input(menu_message, 'number', 5)
    print()

    if menu_selection == 1:
        Sign_Up()
    elif menu_selection == 2:
        Cancel_Sign_Up()
    elif menu_selection == 3:
        View_Participants()
    elif menu_selection == 4:
        Save_Changes()
    else:
        Exit()

Start_Up()
Main_Menu()