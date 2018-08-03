def main():
    #code here
    looping = True
    while looping:
        usrInput = input("Type exit to quit program/n>")
        if (usrInput == "exit"):
            looping = False
            print ("program exiting")      

main()