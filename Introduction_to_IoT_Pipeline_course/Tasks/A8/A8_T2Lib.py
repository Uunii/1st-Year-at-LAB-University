########################################################
# Task A8_T2
# Developer Unubold Luvsandagva
# Date 2024.12.10
########################################################
def showOptions(first_run):
    if first_run:
        print("Options:\n1 - Add\n2 - Subtract\n3 - Multiply\n3 - Divide\n0 - Exit")
    else:
        print("\nOptions:\n1 - Add\n2 - Subtract\n3 - Multiply\n3 - Divide\n0 - Exit")
    return None
def askChoice():
    try:
        choice = float(input("Your choice: "))
        return choice
    except ValueError:
        return 5