#Python K-pop genre searach
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
search = input('Please enter the name of the group/idol:')
if search:
    try:
        from time import sleep
        sleep(1)
        webbrowser.open(f'http://en.wikipedia.org/wiki/{search}')
        sleep(2)
    except:
        print(f"{search} not found on wikipedia")
while True:
  
    print('1. search for another K-pop Group/Idol?')
    print('2. Exit/Quit')
    ans = input("Please select an option: ")
    if ans == "1":
        continue 
    elif ans == "2":
        exit()
        

   
