import pywhatkit.whats
import pywhatkit
from IPython.display import clear_output

#phone_numer = 'XXXXXXX'
#group_id = 'XXXXXXX'
message = 'This is a default message in case I forgot to add it'
time_hour = 19
time_minute = 22
waiting_time_to_send = 15
close_tab = True
waiting_time_to_close = 3

mode = "group"

def ask(question, options):
    choice = 'wrong'
    
    while choice not in options:
        
        choice = input(f"{question}: ")

        if choice not in options:
            print(f"You selected incorrectly, please select {options}")
    
    return choice

def defineReciever():
    recieverOptions = {}
    # Ask if its a contact or a group
    reciever = ask("Do you wish to send a message to [C=contact or G=group]", ['G', 'C'])
    if reciever == 'C':
        recieverOptions['mode'] = 'contact'
    else:
        recieverOptions['mode'] = 'group'

    if reciever == 'C':
        phone = input("Please, provide the phone number: ")
        recieverOptions['phone_number'] = phone
    else:
        group = input("Please, provide the Group ID: ")
        recieverOptions['group_id'] = group

    # Ask if you want to change the default values
    default_values = ask("Do you wish to change the default values [Yes, No]? ", ['Yes', 'No'])
    if default_values == 'Yes':
        pass
    else: 
        recieverOptions['waiting_time_to_send'] = waiting_time_to_send
        recieverOptions['close_tab'] = close_tab
        recieverOptions['waiting_time_to_close'] = waiting_time_to_close

    message = input("Please provide the message to send: ")
    recieverOptions['message'] = message

    clear_output()

    return recieverOptions


def sendMessage(recieverOptions):

    clear_output()

    print("\nThese are the configuration options:")
    print(f"  - Wait time to send the message: {recieverOptions['waiting_time_to_send']}")
    print(f"  - Close tab after finish: {recieverOptions['close_tab']}")
    print(f"  - Wait time to close the tab: {recieverOptions['waiting_time_to_close']}")

    if recieverOptions['mode'] == "contact":

        print (f"\nYou are going to send the following message to {recieverOptions['phone_number']}")
        print (f"{'#'*len(recieverOptions['message'])}")
        print (recieverOptions['message'])
        print (f"{'#'*len(recieverOptions['message'])}")

        pywhatkit.whats.sendwhatmsg_instantly(recieverOptions['phone_number'], recieverOptions['message'], recieverOptions['waiting_time_to_send'], recieverOptions['close_tab'], recieverOptions['waiting_time_to_close'])
    elif recieverOptions['mode'] == "group":
        print (f"\nYou are going to send the following message to {recieverOptions['group_id']}")
        print (f"{'#'*len(recieverOptions['message'])}")
        print (recieverOptions['message'])
        print (f"{'#'*len(recieverOptions['message'])}")

        pywhatkit.whats.sendwhatmsg_to_group_instantly(recieverOptions['group_id'], recieverOptions['message'], recieverOptions['waiting_time_to_send'], recieverOptions['close_tab'], recieverOptions['waiting_time_to_close'])
    else:
        print("Error code: 97654")
        print("Error Message: Please select a mode to send your message.")

if __name__ == "__main__":
    recieverOptions = defineReciever()
    sendMessage(recieverOptions)