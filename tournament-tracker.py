def Validate_Input(message, input_type):
    valid_value = False
    if input_type == 'num':
        while valid_value == False:
            try:
                user_input = int(input(message))
                valid_value = True
                return user_input
            except ValueError:
                print()
                print("Invalid input.\n")
                continue
    

def StartUp():
    print()
    print("Welcome to Tournaments R Us\n============================")
    message = "Enter number of participants: "
    global num_participants

    input_type = 'num'
    num_participants = Validate_Input(message, input_type)
    while num_participants == 1:
        print()
        print('The number of participants must be more than 1!\n')
        num_participants = Validate_Input(message, input_type)

    print(f"There are {num_participants} participant slots ready for sign-ups.\n\n")

    participant_dict = {}
    for i in range(1,num_participants+1):
        participant_dict.update({i:None}) 



def SignUp():

    print("Participant Sign Up\n====================")
    participant_name = input("Participant Name: ")
    starting_slot = input(f"Desired starting slot #[1-{num_participants}]: ")


StartUp()
SignUp()