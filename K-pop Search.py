#Python K-pop search
import webbrowser


print('''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.-..-.                                                         .-.              
: :' ;                                                         : :              
:   '  _____ .---.  .--. .---.    .--.  .--.  .--.  .--.  .--. : `-.  .--. .--. 
: :.`.:_____:: .; `' .; :: .; `  `._-.'' '_.'' .; ; : ..''  ..': .. :' '_.': ..'
:_;:_;       : ._.'`.__.': ._.'  `.__.'`.__.'`.__,_;:_;  `.__.':_;:_;`.__.':_;  
             : :         : :                                                    
             :_;         :_;                                                    
    
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''')
#Welcome text!
from time import sleep
sleep(2)
print("Welcome!")
#asking for user input
from time import sleep
sleep(1)
search = input('Please enter the name of the group/idol:')
from time import sleep
sleep(1)
#opening wiki pages
webbrowser.open(f'http://en.wikipedia.org/wiki/{search}')
from time import sleep
sleep(2)
print("...")

#User exiting or more searching:
while True:
    print('1. Search for another K-pop Group/Idol?')
    print('2. Exit/Quit')
    ans = input("Please select an option: ")
    if ans == "1":
        search = input('Please enter the name of the group/idol:')
        try:
            webbrowser.open(f'http://en.wikipedia.org/wiki/{search}')
        except:
            print(f"{search} not found on wikipedia")
    elif ans == "2":
        exit()
