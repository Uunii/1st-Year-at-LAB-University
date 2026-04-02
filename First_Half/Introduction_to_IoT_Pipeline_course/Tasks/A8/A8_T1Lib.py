########################################################
# Task A8_T1
# Developer Unubold Luvsandagva
# Date 2024.12.10
########################################################
import time
def showOptions(first_run):
    if first_run:
        print("Options:\n1 - Set pause duration\n2 - Activate pause\n0 - Exit")
    else:
        print("\nOptions:\n1 - Set pause duration\n2 - Activate pause\n0 - Exit")
    return None
def askChoice():
    try:
        choice = float(input("Your choice: "))
        return choice
    except ValueError:
        return 4
def setPause():
    try:
        pause = float(input("Insert pause duration (s): "))
        return pause
    except ValueError:
        return "A"  
def main():
    pausedur = 0
    print("Program starting.")
    first_run = True
    while True:
        showOptions(first_run)
        first_run = False
        choice = askChoice()
        if choice == 1:
            pause = setPause()
            pausedur = pause
        elif choice == 2:
            if pausedur > 0:
                print(f"Pausing for {pausedur} seconds.")
                time.sleep(pause)
                print("Unpaused")
            else:
                print("Set pause first.")
        elif choice == 0:
            print("Exiting program.")
            print("\nProgram ending")
            break 
        else:
            print("Unknown option")
    return None 
main()