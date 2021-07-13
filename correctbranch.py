from models import *


def CorrectedBranch(enteredBranch):
    enteredBranch = enteredBranch.lower()
    enteredBranch = str(enteredBranch)
    print("current EnteredBranch is " + enteredBranch)

    if(enteredBranch in [x.lower() for x in aeroWords]):
        enteredBranch = "Aeronautical"

    elif(enteredBranch in [x.lower() for x in autoWords]):
        print("Word mila array me")
        enteredBranch = "Automobile"

    elif(enteredBranch in [x.lower() for x in biomedWords]):
        print("Word mila array me")
        enteredBranch = "Biomedical"

    elif(enteredBranch in [x.lower() for x in biotechWords]):
        print("Word mila array me")
        enteredBranch = "Biotechnology"

    elif(enteredBranch in [x.lower() for x in chemWords]):
        print("Word mila array me")
        enteredBranch = "Chemical"

    elif(enteredBranch in [x.lower() for x in civilWords]):
        print("Word mila array me")
        enteredBranch = "Civil"

    elif(enteredBranch in [x.lower() for x in cceWords]):
        print("Word mila array me")
        enteredBranch = "CCE"

    elif(enteredBranch in [x.lower() for x in cseWords]):
        enteredBranch = "CSE"

    elif(enteredBranch in [x.lower() for x in dseWords]):
        enteredBranch = "DSE"

    elif(enteredBranch in [x.lower() for x in eeWords]):
        enteredBranch = "EEE"

    elif(enteredBranch in [x.lower() for x in eceWords]):
        enteredBranch = "ECE"

    elif(enteredBranch in [x.lower() for x in eieWords]):
        enteredBranch = "EIE"

    elif(enteredBranch in [x.lower() for x in ipWords]):
        enteredBranch = "Industrial Production"

    elif(enteredBranch in [x.lower() for x in itWords]):
        enteredBranch = "IT"

    elif(enteredBranch in [x.lower() for x in mechWords]):
        enteredBranch = "Mechanical"

    elif(enteredBranch in [x.lower() for x in mechxWords]):
        enteredBranch = "Mechatronics"

    elif(enteredBranch in [x.lower() for x in mediaWords]):
        enteredBranch = "Media Technology"

    elif(enteredBranch in [x.lower() for x in aiWords]):
        enteredBranch = "AI"
    print("The corrected is " + enteredBranch)
    return enteredBranch
