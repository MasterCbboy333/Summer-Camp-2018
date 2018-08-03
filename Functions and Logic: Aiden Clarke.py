def main():
    gender=input("Male or Female (m/f)")
    if (gender == "m" or gender == "f"):
        pass
        
    if gender== "m":
        malestory()
    elif gender == "f":            
        femalestory()
    else:
        print("Invalid Selection")
        
        
def malestory():
    #Code for male story
    print("The guy walked to the candy store")
def femalestory():
    #Code for female story
    print("The girl walked to the candy store")

main()