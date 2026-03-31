import random
random.seed(1234)

player_scoreboard = {"wins": 0, "losses": 0, "draws": 0}
RPS_scoreboard = {"wins": 0, "losses": 0, "draws": 0}

def rock():
    print("    _______\n---'   ____)")
    print("      (_____)\n      (_____)")
    print("      (____)\n---.__(___)\n\n#########################")
    return None
def paper():
    print("     _______\n---'    ____)____")
    print("           ______)\n          _______)")
    print("         _______)\n---.__________)\n\n#########################")
    return None
def scissors():
    print("    _______\n---'   ____)____")
    print("          ______)\n       __________)")
    print("      (____)\n---.__(___)\n\n#########################")
def Options():
    print("\nOptions:\n1 - Rock\n2 - Paper")
    print("3 - Scissors\n0 - Quit game")
    move = input("Your choice: ")
    return move
def start():
    print("Rock! Paper! Scissors! Shoot!\n\n#########################")
    return None
PC = "RPS-3PO"
def main():
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    name = input("Insert player name: ")
    print(f"Welcome {name}!")
    print(f"Your opponent is {PC}.")
    print("Game starts...")
    playing = True
    while playing:
        RPS = random.randint(1, 3)
        move = Options()
        if move == "1":
            if RPS == 1:
                start()
                print(name, "chose rock.\n")
                rock()
                print(PC, "chose rock.\n")
                rock()
                print("")
                print("Draw! Both players chose rock.")
                player_scoreboard["draws"] += 1
                RPS_scoreboard["draws"] += 1
            elif RPS == 2:
                start()
                print(name, "chose rock.\n")
                rock()
                print(PC, "chose paper.\n")
                paper()
                print("")
                print(PC, "paper beats", name, "rock.")
                player_scoreboard["losses"] += 1
                RPS_scoreboard["wins"] += 1
            elif RPS == 3:
                start()
                print(name, "chose rock.\n")
                rock()
                print(PC, "chose scissors.\n")
                scissors()
                print("")
                print(name, "rock beats", PC, "scissors.")
                player_scoreboard["wins"] += 1
                RPS_scoreboard["losses"] += 1
        elif move == "2":
            if RPS == 1:
                start()
                print(name, "chose paper.\n")
                paper()
                print(f"{PC} chose rock.\n")
                rock()
                print("")
                print(name, "paper beats", PC, "rock.")
                player_scoreboard["wins"] += 1
                RPS_scoreboard["losses"] += 1
            elif RPS == 2:
                start()
                print(name, "chose paper.\n")
                paper()
                print(PC, "chose paper.\n")
                paper()
                print("")
                print("Draw! Both players chose paper.")
                player_scoreboard["draws"] += 1
                RPS_scoreboard["draws"] += 1
            elif RPS == 3:
                start()
                print(name, "chose paper.\n")
                paper()
                print(PC, "chose scissors.\n")
                scissors()
                print("")
                print(PC, "scissors beats", name, "rock.")
                player_scoreboard["losses"] += 1
                RPS_scoreboard["wins"] += 1
        elif move == "3":
            if RPS == 1:
                start()
                print(name, "chose scissors.\n")
                scissors()
                print(PC, "chose rock.\n")
                rock()
                print("")
                print(PC, "rock beats", name, "scissors.")
                player_scoreboard["losses"] += 1
                RPS_scoreboard["wins"] += 1
            elif RPS == 2:
                start()
                print(name, "chose scissors.\n")
                scissors()
                print(PC, "chose paper.\n")
                paper()
                print("")
                print(name, "scissors beats", PC, "paper.")
                player_scoreboard["wins"] += 1
                RPS_scoreboard["losses"] += 1
            elif RPS == 3:
                start()
                print(name, "chose scissors.\n")
                scissors()
                print(PC, "chose scissors.\n")
                scissors()
                print("")
                print("Draw! Both players chose scissors.")
                player_scoreboard["losses"] += 1
                RPS_scoreboard["wins"] += 1
        elif move == "0":
            playing = False
        else:
            print("Unknown command.")
    print("\nResults:")
    print(f"{name} - wins ({player_scoreboard["wins"]}), ", end='')
    print(f"losses ({player_scoreboard["losses"]}), ", end='')
    print(f"draws ({player_scoreboard["draws"]})")
    print(f"{PC} - wins ({RPS_scoreboard["wins"]}), ", end='')
    print(f"losses ({RPS_scoreboard["losses"]}), ", end='')
    print(f"draws ({RPS_scoreboard["draws"]})")
    print("\nProgram ending.")
    return None
main()