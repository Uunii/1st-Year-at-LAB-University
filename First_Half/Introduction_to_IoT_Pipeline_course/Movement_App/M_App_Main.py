import random
from colorama import init, Fore, Back, Style
import string
from datetime import datetime
import requests
import json
import time
import pandas as pd
import matplotlib.pyplot as plt
def APIurl():
    base_url = "https://api.thingspeak.com/channels/2578404/feeds.json?api_key=XSXF6WH7DAECB6S1&results="
    while True:    
        try:
            countAPI = int(input("How many result you want to see?: "))
            url = f"{base_url}{countAPI}"
            return countAPI, url
        except ValueError:
            print("Please enter number of how many results you want to see.")   
def APICgraph():
    countAPI, url=APIurl()
    response = requests.get(url)
    data = response.json()
    print("\nConnecting to API...",Fore.GREEN)
    time.sleep(0.6) 
    print(Fore.GREEN,"Status code:",response.status_code ,Fore.WHITE)
    time.sleep(0.6)
    print("Getting recent",countAPI,"results...")
    time.sleep(0.6)
    tempdata = [entry["field2"] for entry in data['feeds']]
    movedata = [entry["field1"] for entry in data['feeds']]
    entries = []
    for entry in data["feeds"] :
        MDtemp = entry["field2"] 
        MDmove = entry["field1"]
        date= entry["created_at"]
        MDday = date[0:10]
        MDtime= date[11:19]   
        if MDmove == "1":
            Movement = "Movement detected: YES"
        else:
            Movement = "Movement detected: NO"            
        SAPIF = {
            "Date": MDday,
            "Time": MDtime,
            "CPU temp (Fahrenheit)": MDtemp,
            "Status": Movement
        }
        entries.append(SAPIF)
    
    df = pd.DataFrame({
        'Temperature': tempdata,
        'Movement' : movedata
    })
    plt.figure(figsize=(12, 7))
    plt.subplot(2,1,1)
    plt.plot(df['Temperature'], label='Temperature')
    plt.title('Temperature Over Time')
    plt.subplot(2,1,2)
    plt.plot(df['Movement'], label='Movement',color="orange")
    plt.title('Movement Over Time')
    plt.show()
    try:
        with open("History_C.json", "r") as file:
            history_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        history_data = {}

    print("\nDo you want to save the results to the History?\n1 - Yes\n2 - No")
    while True:
        saveFchoose = input("Your choice: ")
        if saveFchoose == "1":
            current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            history_data[current_timestamp] = entries
            with open("History_C.json", "w") as file:
                json.dump(history_data, file, indent=4)
            print("Result saved to History.\nGoing back to API menu...")
            time.sleep(0.5)
            break
        elif saveFchoose == "2":
            print("Skipping save.")
            time.sleep(0.5)
            print("\nGoing back to API menu...")
            time.sleep(0.5)
            break
        else:
            print("Invalid input.")
    return None   
def APIFgraph():
    countAPI, url=APIurl()
    response = requests.get(url)
    data = response.json()
    print("\nConnecting to API...")
    time.sleep(0.6) 
    print(Fore.GREEN,"Status code:",response.status_code,Fore.WHITE)
    time.sleep(0.6)
    print("Getting recent",countAPI,"results...")
    time.sleep(0.6)
    tempdata = [(float(entry["field2"]) * 9/5) + 32 for entry in data['feeds']]
    movedata = [entry["field1"] for entry in data['feeds']]
    entries = []
    for entry in data["feeds"] :
        MDtemp = entry["field2"] 
        MDmove = entry["field1"]
        date= entry["created_at"]
        MDday = date[0:10]
        MDtime= date[11:19]   
        if MDmove == "1":
            Movement = "Movement detected: YES"
        else:
            Movement = "Movement detected: NO"       
        MDtemp = float(entry["field2"]) 
        MDtempF = round(MDtemp * 9/5 + 32, 2) 
        if MDmove == "1":
            Movement = "Movement detected: YES"
        else:
            Movement = "Movement detected: NO"       
        SAPIF = {
            "Date": MDday,
            "Time": MDtime,
            "CPU temp (Fahrenheit)": MDtempF,
            "Status": Movement
        }
        entries.append(SAPIF)
    
    df = pd.DataFrame({
        'Temperature': tempdata,
        'Movement' : movedata
    })
    plt.figure(figsize=(12, 7))
    plt.subplot(2,1,1)
    plt.plot(df['Temperature'], label='Temperature')
    plt.title('Temperature Over Time')
    plt.subplot(2,1,2)
    plt.plot(df['Movement'], label='Movement',color="orange")
    plt.title('Movement Over Time')
    plt.show()
    try:
        with open("History_F.json", "r") as file:
            history_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        history_data = {}

    print("\nDo you want to save the results to the History?\n1 - Yes\n2 - No")
    while True:
        saveFchoose = input("Your choice: ")
        if saveFchoose == "1":
            current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            history_data[current_timestamp] = entries
            with open("History_F.json", "w") as file:
                json.dump(history_data, file, indent=4)
            print(Fore.GREEN,"Result saved to History.\n",Fore.WHITE,"Going back to API menu...")
            time.sleep(0.5)
            break
        elif saveFchoose == "2":
            print(Fore.RED,"Skipping save.",Fore.WHITE)
            time.sleep(0.5)
            print("\nGoing back to API menu...")
            time.sleep(0.5)
            break
        else:
            print(Fore.RED,"Invalid input.",Fore.WHITE)
    return None    
def APICtext():
    countAPI, url = APIurl()
    response = requests.get(url)
    data= response.json()
    print("\nConnecting to API...")
    time.sleep(0.6) 
    print(Fore.GREEN,"Status code:",response.status_code,Fore.WHITE)
    time.sleep(0.6)
    print("Getting recent",countAPI,"results...\n")
    time.sleep(0.6)
    entries = []
    for entry in data["feeds"] :
        MDtemp = entry["field2"] 
        MDmove = entry["field1"]
        date= entry["created_at"]
        MDday = date[0:10]
        MDtime= date[11:19]   
        if MDmove == "1":
            Movement = "Movement detected: YES"
        else:
            Movement = "Movement detected: NO"       
        if MDtemp >= "90":
            situation= "IT IS ON FIRE!"
        elif MDtemp >= "75":
            situation = "IT is TOO HOT!"
        else:
            situation = "IT is OK"
        SAPIF = {
            "Date": MDday,
            "Time": MDtime,
            "CPU temp (Fahrenheit)": MDtemp,
            "Status": Movement
        }
        entries.append(SAPIF)
        print(f"\nDate: {MDday} Time: {MDtime}\nThe temperature of the CPU is {MDtemp }°C {situation} \n{Movement}")
        time.sleep(0.4)

    try:
        with open("History_C.json", "r") as file:
            history_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        history_data = {}

    print("\nDo you want to save the results to the History?\n1 - Yes\n2 - No")
    while True:
        saveFchoose = input("Your choice: ")
        if saveFchoose == "1":
            current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            history_data[current_timestamp] = entries
            with open("History_C.json", "w") as file:
                json.dump(history_data, file, indent=4)
            print("Result saved to History.")
            break
        elif saveFchoose == "2":
            print("Skipping save.")
            time.sleep(0.5)
            print("\nGoing back to API menu... ")
            time.sleep(0.5)
            break
        else:
            print("Invalid input.")
    return None   
def APIFtext():
    countAPI, url = APIurl()
    response = requests.get(url)
    data= response.json()
    print("\nConnecting to API...")
    time.sleep(0.6) 
    print(Fore.GREEN,"Status code:",response.status_code,Fore.WHITE)
    time.sleep(0.6)
    print("Getting recent",countAPI,"results...\n")
    time.sleep(0.6)
    entries = []
    for entry in data["feeds"] :
        MDtemp = entry["field2"] 
        MDmove = entry["field1"]
        date= entry["created_at"]
        MDday = date[0:10]
        MDtime= date[11:19]   
        MDtemp = float(entry["field2"]) 
        MDtempF = round(MDtemp * 9/5 + 32, 2) 
        if MDmove == "1":
            Movement = "Movement detected: YES"
        else:
            Movement = "Movement detected: NO"       
        if MDtempF  >= 194:
            situation= "IT IS ON FIRE!"
        elif MDtempF  >= 167:
            situation = "IT is TOO HOT!"
        else:
            situation = "IT is OK"
        SAPIF = {
            "Date": MDday,
            "Time": MDtime,
            "CPU temp (Fahrenheit)": MDtempF,
            "Status": Movement
        }
        entries.append(SAPIF)
        print(f"\nDate: {MDday} Time: {MDtime}\nThe temperature of the CPU is {MDtempF }°F {situation} \n{Movement}")
        time.sleep(0.4)

    try:
        with open("History_F.json", "r") as file:
            history_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        history_data = {}

    print("\nDo you want to save the results to the History?\n1 - Yes\n2 - No")
    while True:
        saveFchoose = input("Your choice: ")
        if saveFchoose == "1":
            current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            history_data[current_timestamp] = entries
            with open("History_Fjson", "w") as file:
                json.dump(history_data, file, indent=4)
            print("Result saved to History.")
            break
        elif saveFchoose == "2":
            print("Skipping save.")
            time.sleep(0.5)
            print("\nGoing back to API menu...")
            time.sleep(0.5)
            break
        else:
            print("Invalid input.")
    return None   
def NumberGame():
    scoreboard = {"wins":0, "loses":0}
    playing = True
    while playing:
        print("\nWelcome to the Number Guessing Game!")
        num = random.randint(1,100)
        attempts = 0
        max_attempts = 8

        while attempts<max_attempts:
            print("Guess the number between 1-100")
            guess = input(f"Attempt {attempts+1}/{max_attempts}: ")
            if guess.lower() == "quit":
                playing = False
                break
            elif int(guess) < num:
                print("Too low")
                attempts +=1
            elif int(guess) > num:
                print("Too high")
                attempts +=1
            else:
                print("Congratulations, You guessed the number correctly!")
                scoreboard["wins"] +=1 
                break
        if attempts == max_attempts and guess != num:
            print("Max attempts limit reached, the number was:",num)
            scoreboard["loses"] +=1
        print("\nScoreboard:")
        print("Wins:",scoreboard["wins"], "Losses:", scoreboard["loses"])
        if not playing:
            break
        restart = input("\nDo you want to play again? (yes to continue, quit to exit): ")
        if restart.lower() == "quit":
            playing = False
            break
    print("Thanks for playing")
    return None
def RockPaperScissors():
    def rockandrock():
        print("============================================\n\n   Player                        Sulugass")
        print("     _______                    _______    \n----'   ____)                  (____   '----")
        print("       (_____)                (_____)      \n       (_____)                (_____)      ")
        print("       (____)                  (____)      \n----.__(___)        DRAW        (___)__.----\n\n============================================")
    def paperandpaper():
        print("============================================\n\n    Player                      Sulugass")
        print("     _______                    _______     \n---'    ____)____          ____(____    '---")
        print("           ______)        (______           \n          _______)        (_______         ")
        print("         _______)          (_______         \n---.__________)     DRAW     (__________.---\n\n============================================")
    def scissorsandscissors():
        print("============================================\n\n    Player                      Sulugass")
        print("    _______                      _______    \n---'   ____)___              ___(____   '---   ")
        print("          ______)          (______          \n       __________)        (__________       ")
        print("      (____)                    (____)      \n---.__(___)         DRAW         (___)__.---\n\n============================================")
    def rockandpaper():
        print("============================================\n\n   Player                        Sulugass")
        print("    _______                      _______\n---'   ____)                ____(____   '---\n      (_____)              (______           ")
        print("      (_____)             (_______           \n       (____)              (_______          \n---.__(___)                 (__________.----\n                You lost!\n\n============================================")
    def rockandscissors():
        print("============================================\n\n    Player                      Sulugass")
        print("    _______                       _______\n---'   ____)                 ___(____   '---")
        print("      (_____)               (______           \n      (_____)              (__________        ")
        print("       (____)                    (____)       \n---.__(___)                       (___)__.--\n                  You won!\n\n============================================")    
    def paperandrock():
        print("============================================\n\n    Player                      Sulugass")
        print("    _______                     _______\n---'   ____)____               (____    '---")
        print("           ______)            (_____)       \n          _______)            (_____)       ")
        print("         _______)              (____)       \n---.__________)                  (___)__.---\n                    You won!\n\n============================================")
    def paperandscissors():
        print("============================================\n\n    Player                      Sulugass")
        print("     _______                       ______")
        print("---'    ____)____             ___(____   '---")
        print("           ______)          (______          ")
        print("          _______)         (_________       ")
        print("         _______)               (____)       ")
        print("---.__________)                  (___)__.---\n                    You lost!\n\n============================================")
    def scissorsandrock():
        print("============================================\n\n    Player                      Sulugass")
        print("    _______                      _______\n---'   ____)___                (____    '---")
        print("          ______)             (_____)        \n       __________)            (_____)        ")
        print("      (____)                   (____)        \n---.__(___)                     (___)__.----\n                 You lost!\n\n============================================")
    def scissorsandpaper():
        print("============================================\n\n    Player                      Sulugass")
        print("    _______                       _______\n---'   ____)___             ____(____   '---")
        print("          ______)          (______           \n       __________)         (_______          ")
        print("      (____)                (_______         \n---.__(___)                  (__________.---\n                 You won!\n\n============================================")

    player_scoreboard = {"wins":0, "losses":0, "draws":0}

    PC = "Sulugass"
    RPS = random.randint(1,3)
    time.sleep(0.6)
    print("\nWelcome to the rock-paper-scissors game")
    time.sleep(0.6)
    print(f"Your opponent is '{PC}'")
    time.sleep(0.6)
    print("Game starts...")
    time.sleep(0.6)
    playing = True

    while playing:
        print("\nOptions:")
        print("1 - Rock\n2 - Paper\n3 - Scissors\n0 - Quit game")
        move = input("\nYour move: ")
        RPS = random.randint(1, 3)

        if move == "1":
            if RPS == 1:
                print("\nRock! Paper! Scissors! Shoot!")
                rockandrock()
                player_scoreboard["draws"] +=1
            elif RPS == 2:
                print("\nRock! Paper! Scissors! Shoot!")
                rockandpaper()
                player_scoreboard["losses"] +=1
            elif RPS == 3:
                print("\nRock! Paper! Scissors! Shoot!")
                rockandscissors()
                player_scoreboard["wins"] +=1
        elif move == "2":
            if RPS == 1:
                print("\nRock! Paper! Scissors! Shoot!")
                paperandrock()
                player_scoreboard["wins"] +=1
            elif RPS == 2:
                print("\nRock! Paper! Scissors! Shoot!")
                paperandpaper()
                player_scoreboard["draws"] +=1
            elif RPS == 3:
                print("\nRock! Paper! Scissors! Shoot!")
                paperandscissors()
                player_scoreboard["losses"] +=1
        elif move == "3":
            if RPS == 1:
                print("\nRock! Paper! Scissors! Shoot!")
                scissorsandrock()
                player_scoreboard["losses"] +=1
            elif RPS == 2:
                print("\nRock! Paper! Scissors! Shoot!")
                scissorsandpaper()
                player_scoreboard["wins"] +=1
            elif RPS == 3:
                print("\nRock! Paper! Scissors! Shoot!")
                scissorsandscissors()
                player_scoreboard["draws"] +=1
        elif move == "0":
            playing = False
        else:
            print("Invalid choice!")
    print(f"\nPlayer - wins ({player_scoreboard['wins']}), losses ({player_scoreboard['losses']}), draws ({player_scoreboard['draws']})")
    print("Thanks for playing.")
def LoginMenu():
    print(Fore.BLUE,Style.BRIGHT,"\n_______________________________________________")
    print("______",Fore.YELLOW,"[ Welcome to Motion Detector ]",Fore.BLUE,"_______\n",Fore.GREEN,Style.BRIGHT)
    print("  1 - Sign in","                    ",Fore.RED,                       "0 - Exit",Fore.GREEN)
    print("  2 - Sign up",Fore.BLUE,Style.BRIGHT)
    print("_______________________________________________\n———————————————————————————————————————————————\n",Fore.WHITE,Style.NORMAL)
    LogOrSign = input("Your choice: ")
    return LogOrSign
def Mainmenu():
    print(Fore.BLUE,Style.BRIGHT,"\n_______________________________________________")
    print("______________",Fore.YELLOW,"[ Main menu ]",Fore.BLUE,"________________\n",Fore.GREEN,Style.NORMAL)
    print("  1 - Unit convertor",Fore.YELLOW,"         ",             "3 - Admin page",Fore.GREEN, "\n  2 - Motion Detector           4 - Games\n",Fore.RED,  "0 - Log out",Fore.BLUE,Style.BRIGHT)
    print("_______________________________________________\n———————————————————————————————————————————————\n",Fore.WHITE,Style.NORMAL)
    mmenuchoose = input("Your choice: ")
    return mmenuchoose
def Convertmenu():
    print(Fore.BLUE,Style.BRIGHT,"\n_______________________________________________")
    print("____________",Fore.YELLOW, "[ Unit convertor ]",Fore.BLUE, "_____________\n",Fore.GREEN)
    print("  1 - Temperature                3 - Weight\n  2 - Length","                  ",Fore.RED,                      "0 - Go back",Fore.BLUE)
    print("_______________________________________________\n———————————————————————————————————————————————\n",Fore.WHITE,Style.NORMAL)
    cchoose = input("Your choice: ")
    return cchoose
def TempCMenu():
    time.sleep(0.5)
    print(Fore.BLUE,Style.BRIGHT,"\n_______________________________________________")
    print("_________",Fore.YELLOW,"[ Temperature convertor ]",Fore.BLUE, "_________\n",Fore.GREEN)
    print("  1 - Celsius(°C)        =>     Fahrenheit(°F) \n  2 - Fahrenheit(°F)     =>     Celsius(°C) \n",Fore.RED,"0 - Go back",Fore.BLUE)
    print("_______________________________________________\n———————————————————————————————————————————————\n",Fore.WHITE,Style.NORMAL)
    tchoose = input("Your choice: ")
    return tchoose
def WeightCMenu():
    time.sleep(0.5)
    print(Fore.BLUE,Style.BRIGHT,"\n_______________________________________________")
    print("___________",Fore.YELLOW, "[ Weight convertor ]",Fore.BLUE, "____________\n",Fore.GREEN)
    print("  1 - Kilogramm(kg)     =>       Pound(lbs)\n  2 - Pound(lbs)        =>       Kilogramm(kg)",Fore.CYAN)
    print("\n  3 - Gramm(gr)         =>       Ounce(oz)\n  4 - Ounces(oz)        =>       Gramm(gr)\n",Fore.RED,"\n  0 - Go back",Fore.BLUE)
    print("_______________________________________________\n———————————————————————————————————————————————\n",Fore.WHITE,Style.NORMAL)
    wchoice = input("Your choice: ")
    return wchoice
def LengthCMenu():
    time.sleep(0.5)
    print(Fore.BLUE,Style.BRIGHT,"\n_______________________________________________")
    print("___________",Fore.YELLOW, "[ Length convertor ]",Fore.BLUE, "____________\n",Fore.GREEN)
    print("  1 - Centimeter(cm)    =>     Inch(in)\n  2 - Inch(in)          =>     Centimeter(cm)\n",Style.NORMAL)
    print("  3 - Meter(m)          =>     Yard(yd)\n  4 - Yard(yd)          =>     Meter(m)\n",Style.BRIGHT)
    print("  5 - Kilometer(km)     =>     Mile(mi)\n  6 - Mile(mi)          =>     Kilometer(km)\n\n",Fore.RED,"0 - Go back",Fore.BLUE)
    print("_______________________________________________\n———————————————————————————————————————————————\n",Fore.WHITE,Style.NORMAL)
    lchoice = input("Your choice: ")
    return lchoice
def MDmenu():
    time.sleep(0.8)
    print(Fore.BLUE,Style.BRIGHT,"\n_______________________________________________")
    print("________________",Fore.YELLOW,"[ IoT_LaB ]",Fore.BLUE,"________________\n",Fore.YELLOW)
    print("Choose your temperature unit",Fore.GREEN,"\n\n  1 - Celsius(°C)         2 - Fahrenheit(°F) \n",Fore.RED,"\n  0 - Go back",Fore.BLUE)
    print("_______________________________________________\n———————————————————————————————————————————————\n",Fore.WHITE,Style.NORMAL)
    mdmenu = input("Your choice: ")
    return mdmenu
def Celsiusmenu():
    time.sleep(0.8)
    print(Fore.BLUE,Style.BRIGHT,"\n_______________________________________________")
    print("__________",Fore.YELLOW, "[ IoT_LaB ] (Celsius)",Fore.BLUE, "____________\n",Fore.YELLOW)
    print("Choose your preferred way to see the results",Fore.GREEN,"\n\n  1 - Text                       2 - Graph\n\n",Fore.RED,"0 - Go back",Fore.BLUE)
    print("_______________________________________________\n———————————————————————————————————————————————\n",Fore.WHITE,Style.NORMAL)
    cmenu = input("Your choice: ")
    return cmenu
def Fahrenheitmenu():
    time.sleep(0.8)
    print(Fore.BLUE,Style.BRIGHT,"\n_______________________________________________")
    print("__________",Fore.YELLOW, "[ IoT_LaB ] (Fahrenheit)",Fore.BLUE, "_________\n",Fore.YELLOW)
    print("Choose your preferred way to see the results.",Fore.GREEN,"\n\n  1 - Text                        2 - Graph\n\n",Fore.RED,"0 - Go back",Fore.BLUE)
    print("_______________________________________________\n———————————————————————————————————————————————\n",Fore.WHITE,Style.NORMAL)
    fmenu = input("Your choice: ")
    return fmenu
def Gamemenu():
    time.sleep(0.8)
    print(Fore.BLUE,Style.BRIGHT,"\n_______________________________________________")
    print("_________________",Fore.YELLOW, "[ Games ]",Fore.BLUE,"_________________\n")
    print("  1 - Number Guessing game\n  2 - Rock Paper Scissors\n\n",Fore.RED,"0 - Go back",Fore.BLUE)
    print("_______________________________________________\n———————————————————————————————————————————————\n",Fore.WHITE,Style.NORMAL)
    gchoice = input("Your choice: ")
    return gchoice
def SignUp():
    print(Fore.BLUE,"\n_______________________________________________")
    print("_______________",Fore.YELLOW, "[ Sign Up ]",Fore.BLUE,"_________________\n",Fore.WHITE,Style.NORMAL)
    fname = input("Enter your first name: ").strip().capitalize()
    lname = input("Enter your last name: ").strip().capitalize()

    while True:
        bday = input("Enter your birthday (dd/mm/yyyy): ")
        bday = bday.replace('.', '/')
        try:
            day, month, year = bday.split('/')
            bday = datetime.strptime(bday, "%d/%m/%Y")
            break
        except ValueError:
            print("Invalid format! Please use dd/mm/yyyy.")

    today = datetime.today()
    age = today.year - bday.year - ((today.month, today.day) < (bday.month, bday.day))
    userid = fname[0:2] + lname[0:3] + year + month + day

    with open("user-data.json", "r") as file:
        olddata = json.load(file)

    if any(user['User ID'] == userid for user in olddata):
        time.sleep(0.5)
        print(f"\nAccount already exists for User ID: {userid}. Going back to login menu...")
        time.sleep(1)
    else:
        if age > 18:
            while True:
                time.sleep(0.5)
                print("\nYour user ID is:", userid)
                time.sleep(0.5)
                print("Do you want to use your user ID as your username? \n1 - Yes \n2 - No")
                useit = input("Your choice: ")
                if useit == "1":
                    username = userid
                    break
                elif useit == "2":
                    username = input("\nEnter user name you want to use: ")
                    break
                else:
                    print("invalid input.")
            time.sleep(0.4)
            print("\nHello", fname, lname, end=", welcome to the Motion Detector! Let's start.")
            time.sleep(0.5)
            print("\nYour user name is:", username)

            rights = "viewer"
            if userid == "UnLuv19990611":
                rights = "admin"
            elif userid[0:5] == "MiVor":
                rights = "super-user"
            time.sleep(0.8)
            print(f"You have {rights} rights.")
            time.sleep(0.8)
            print("\nLet's create a password.")
            while True:
                print("\nPassword creating options:")
                print("1 - Create your own password.")
                print("2 - Generate password using number of characters of your choice.")
                choice = input("Choose your password creating method: ")
                if choice == "1":
                    while True:
                        Password = input("Create your password: ")
                        print("\nAre you happy with this password? \n1 - Yes \n2 - No")
                        satisfied = input("Your choice: ")
                        if satisfied == "2":
                            print("\nLet's start over")
                            continue
                        elif satisfied == "1":
                            time.sleep(0.8)
                            print("\nGreat, Password has been created.")
                            break
                        else:
                            print("Invalid input.")
                    if satisfied == "1":
                        break
                elif choice == "2":
                    while True:
                        print("\nAutomatic password generator")
                        cletters = int(input("Enter the number of uppercase letters: "))
                        sletters = int(input("Enter the number of lowercase letters: "))
                        numbers = int(input("Enter the number of numbers: "))
                        schars = int(input("Enter the number of special characters: "))

                        if cletters + sletters + numbers + schars > 0:
                            break
                        else:
                            print("You must specify at least one character in total.")

                    pcletters = string.ascii_uppercase
                    psletters = string.ascii_lowercase
                    pnumbers = string.digits
                    pschars = string.punctuation

                    while True:
                        PASScletters = random.choices(pcletters, k=cletters)
                        PASSsletters = random.choices(psletters, k=sletters)
                        PASSnumbers = random.choices(pnumbers, k=numbers)
                        PASSschars = random.choices(pschars, k=schars)

                        Pass = PASScletters + PASSsletters + PASSnumbers + PASSschars
                        random.shuffle(Pass)
                        Password = ''.join(Pass)

                        print("Your generated password is:", Password)

                        print("Are you happy with this password?\n1 - Yes \n2 - No ")
                        satisfied = input("Your choice: ")
                        if satisfied == "2":
                            print("\nLet's start over.")
                            continue
                        elif satisfied == "1":
                            print("\nGreat, Password has been created.")
                            break
                        else:
                            print("Invalid input.")
                    if satisfied == 1:
                        break
                else:
                    print("Invalid input.")
            data = {
                "First name": fname,
                "Last name": lname,
                "User ID": userid,
                "username": username,
                "password": Password,
                "User rights": rights
            }
            olddata.append(data)

            with open("user-data.json", "w") as file:
                json.dump(olddata, file, indent=4)
            time.sleep(0.5)
            print("Account created successfully.")
            print("Sign in at the following page.")
        else:
            time.sleep(1)
            print(f"\nGreetings {fname}, you are too young to operate this program.")
            print("Program shutting down...")
            return None         
def SignIn():
    with open("user-data.json", "r") as f:
        users = json.load(f)
    correct = False
    print(Fore.BLUE,"\n_______________________________________________")
    print("_______________",Fore.YELLOW, "[ Sign In ]",Fore.BLUE,"_________________\n",Fore.WHITE,Style.NORMAL)

    while not correct:
        Logname = input("Enter your Username: ")
        user = next((user for user in users if user["username"] == Logname), None)
        if user:
            wrongpass = 0
            while wrongpass < 3:
                Logpass = input("Enter your Password: ")
                if Logpass == user["password"]:
                    correct = True
                else:
                    wrongpass += 1
                    print(Fore.RED,"Incorrect password",Fore.WHITE)
                if correct:
                    fname = user["First name"]
                    lname = user["Last name"]
                    userid = user["User ID"]
                    rights = user["User rights"]
                    time.sleep(0.8)  
                    print(Fore.GREEN,"\nLogin successful.",Fore.WHITE)
                    time.sleep(0.8)
                    print(f"\nHello {fname} {lname}, welcome back to the Motion Detector!")
                    time.sleep(0.8)
                    print(f"Your username is: {Logname}")
                    time.sleep(0.8)
                    print(f'You have "{rights}" rights.')
                    time.sleep(1)
                    return fname, lname, userid, rights, Logname  
                elif wrongpass == 3:
                    print(Fore.RED,"\nToo many wrong password attempts, please try again later.",Fore.WHITE)
                    pikachu()
                    print("\nLets try again...\n")
                    correct = False
                    break
            else:
                print(Fore.RED,"Username not found. Please try again.",Fore.WHITE)
def ConvertorC():
    temp = float(input("Enter temperature in °C: "))    
    fheit = round(temp * 9/5 + 32, 2)
    print("\nThe given temperature", temp, "°C is", fheit, "°F.")
    return None
def ConvertorF():
    fheit = float(input("Enter temperature in °F: "))
    temp = round((fheit - 32) * 5/9, 2)
    print("\nThe given temperature", fheit, "°F is", temp, "°C.")
    return None
def main():
    while True:
        LogOrSign = LoginMenu()
        if LogOrSign == "1":
            fname, lname, userid, rights, Logname = SignIn()
            while True:
                mmenuchoose = Mainmenu()
                if mmenuchoose == "1":
                    while True:
                        cchoose = Convertmenu()
                        if cchoose == "1":
                            while True:
                                tchoose = TempCMenu()
                                if tchoose == "1":
                                    Ce = float(input("Insert the amount of celsius: "))
                                    Fa = (Ce * 9/5) + 32
                                    print(Ce,"°C equals to", Fa, "°F")
                                elif tchoose == "2":
                                    F = float(input("Insert the amount of fahrenheit: "))
                                    C = round((F-32) * 5/9 ,1)
                                    print(F,"°F equals to", C, "°C")
                                elif tchoose == "0":
                                    print("Going back to Unit Convertor menu...")
                                    time.sleep(1)
                                    break
                                else:
                                    print(Fore.RED,"Invalid input.",Fore.WHITE)
                        elif cchoose == "2":
                            while True:
                                lchoice = LengthCMenu()
                                if lchoice == "1":
                                    Cent = float(input("Insert the amount of centimeter: "))
                                    In = round(Cent/2.54 ,2)
                                    print(Cent,"cm equals to", In,"in")
                                elif lchoice == "2":
                                    In = float(input("Insert the amount of inch: "))
                                    Cent = round(In*2.54 ,2)
                                    print(In,"in equals to", Cent,"cm")
                                elif lchoice == "3":
                                    M = float(input("Insert the amount of meter: "))
                                    Yard = round(M * 1.094 ,2)
                                    print(M,"m is equal to", Yard,"yd")
                                elif lchoice == "4":
                                    Yard = float(input("Insert the amount of yard: "))
                                    M = round(Yard / 1.094 ,2),
                                    print(Yard,"yd is equal to", M,"m") 
                                elif lchoice == "5":
                                    KM = float(input("Insert amount of kilometer: "))
                                    Mi = round(KM / 1.609 ,2)
                                    print(KM,"km equal to", Mi,"mi")
                                elif lchoice == "6":
                                    Mi = float(input("Insert amount of mile: "))
                                    KM = round(Mi * 1.609 ,2)
                                    print(Mi,"mi equal to", KM,"km")
                                elif lchoice == "0":
                                    print("Going back to Convertor menu...")
                                    time.sleep(0.8)
                                    break
                                else:
                                    print(Fore.RED,"Invalid input.",Fore.WHITE)   
                        elif cchoose == "3":
                            while True:
                                wchoice = WeightCMenu()
                                if wchoice == "1":
                                    kg = float(input("Input amount of kilogramm: "))
                                    Po = round(kg * 2.205 ,2)
                                    print(kg,"kg is equal to",Po,"lbs")
                                elif wchoice == "2":
                                    Po = float(input("Input amount of pound: "))
                                    kg = round(Po / 2.205 ,2)
                                    print(Po,"lbs is equal to",kg,"kg")
                                elif wchoice == "3":
                                    gr = float(input("Input amount of gramm: "))
                                    onc = round(gr / 28.35 ,2)
                                    print(gr,"gr equal to",onc,"oz")
                                elif wchoice == "4":
                                    onc = float(input("Input amount of ounce: "))
                                    gr = round(onc * 28.35 ,2)
                                    print(onc,"oz equal to",gr,"gr")
                                elif wchoice == "0":
                                    print("Going back to Convertor menu...")
                                    time.sleep(0.8)
                                    break   
                                else:
                                    print(Fore.RED,"Invalid input.",Fore.WHITE)                               
                        elif cchoose == "0":
                            print("Going back to main menu...")
                            time.sleep(0.8)
                            break
                        else:
                            print(Fore.RED,"Invalid input.",Fore.WHITE)                                                
                elif mmenuchoose == "2":
                    while True:
                        mdmenu = MDmenu()
                        if mdmenu == "1":
                            while True:
                                cmenu = Celsiusmenu()
                                if cmenu == "1":
                                    APICtext()
                                    break
                                elif cmenu == "2":
                                    APICgraph()
                                    break
                                elif cmenu == "0":
                                    print("Going back to Iot_LaB menu...")
                                    time.sleep(0.8)
                                    break
                                else:
                                    print(Fore.RED,"Invalid input.",Fore.WHITE)
                        elif mdmenu == "2":
                            while True:
                                fmenu = Fahrenheitmenu()
                                if fmenu == "1":
                                    APIFtext()
                                    break
                                elif fmenu == "2":
                                    APIFgraph()
                                    break
                                elif fmenu == "0":
                                    print("Going back to Iot_LaB menu...")
                                    time.sleep(0.8)
                                    break
                                else:
                                    print(Fore.RED,"Invalid input.",Fore.WHITE)
                        elif mdmenu == "0":
                            print("Going back to main menu...")
                            time.sleep(0.8)
                            break
                        else:
                            print(Fore.RED,"Invalid input.",Fore.WHITE)
                elif mmenuchoose == "4":
                    while True:
                        gchoice = Gamemenu()
                        if gchoice == "1":
                            NumberGame()
                        elif gchoice == "2":
                            RockPaperScissors()
                        elif gchoice == "0":
                            print("Going back to main menu...")
                            time.sleep(0.8)
                            break
                elif mmenuchoose == "3":
                    if rights == "Admin":
                        while True:
                            adminchoice = adminmenu()
                            if adminchoice == "1":
                                with open("user-data.json", 'r') as file:
                                    users = json.load(file)
                                print("\nList of Users:")
                                for i, user in enumerate(users, start=1):
                                    time.sleep(0.4)
                                    print(f"[{i}] {user['username']} - {user['User rights']}") 
                            elif adminchoice == "2":
                                with open("user-data.json", 'r') as file:
                                    users = json.load(file)
                                print("Select user.")
                                for i, user in enumerate(users, start=1):
                                    time.sleep(0.4)
                                    print(f"[{i}] {user['username']} - {user['User rights']}")
                                choiceuser = int(input("Select user: ")) - 1
                                print(f"Selected user: {users[choiceuser]['username']}")
                                print('\nSelect "right" to give the selected user: ')
                                print("1 - Admin\n2 - Super-user\n3 - Viewer\n0 - Go back")
                                changeright = input('Your choice: ')
                                while True:
                                    if changeright == "1":
                                        newright = "Admin"
                                        users[choiceuser]['User rights'] = newright
                                        with open("user-data.json", 'w') as file:
                                            json.dump(users, file, indent=4)
                                        print(Fore.GREEN,"Rights updated successfully",Fore.WHITE)
                                        break
                                    elif changeright == "2":
                                        newright = "Super-user"
                                        users[choiceuser]['User rights'] = newright
                                        with open("user-data.json", 'w') as file:
                                            json.dump(users, file, indent=4)
                                        print(Fore.GREEN,"Rights updated successfully",Fore.WHITE)
                                        break
                                    elif changeright == "3":
                                        newright = "viewer"
                                        users[choiceuser]['User rights'] = newright
                                        with open("user-data.json", 'w') as file:
                                            json.dump(users, file, indent=4)
                                        print(Fore.GREEN,"Rights updated successfully",Fore.WHITE)
                                        break
                                    elif changeright == "0":
                                        print("Going back...")
                                        break
                                    else:
                                        print(Fore.RED,"Invalid input.",Fore.WHITE)
                            elif adminchoice == "0":
                                print("Going back to Main menu.")
                                time.sleep(0.8)
                                break
                            else:
                                print(Fore.RED,"Invalid input.",Fore.WHITE)
                    else:
                        time.sleep(1)
                        print(Fore.RED,"Access Denied!",Fore.WHITE,"\nOnly Admins can access this page.")
                        time.sleep(1)
                elif mmenuchoose == "0":
                    print("Logging out...")
                    time.sleep(0.5)
                    break
                else:
                    print(Fore.RED,"Invalid input.",Fore.WHITE)      
        elif LogOrSign == "2":
            SignUp()
        elif LogOrSign == "0":
            print("Programm shutting down... See you soon.")
            break
        else:
            print(Fore.RED,"Invalid input.",Fore.WHITE)
def pikachu():
    print(Fore.YELLOW,"\n\n    ⢻⣿⡗⢶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣄")
    print("    ⠀⢻⣇⠀⠈⠙⠳⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠶⠛⠋⣹⣿⡿")
    print("    ⠀⠀⠹⣆⠀⠀⠀⠀⠙⢷⣄⣀⣀⣀⣤⣤⣤⣄⣀⣴⠞⠋⠉⠀⠀⠀⢀⣿⡟")
    print("    ⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋")
    print("    ⠀⠀⠀⠀⠈⠻⡶⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣠⡾⠋")
    print("    ⠀⠀⠀⠀⠀⣼",Fore.WHITE,"⢠⠒⣆⠀⠀⠀⠀⠀⠀⢠⢲⣄",Fore.YELLOW,"⠀⢻⣆")
    print("    ⠀⠀⠀⠀⢰⡏",Fore.WHITE,"⠈⠛⠋⠀⢀⣀⡀⠀⠀⠘⠛⠃",Fore.YELLOW,"⠀⠈⣿⡀")
    print(f"    ⠀⠀⠀⠀⣾{Fore.RED}⡟⠛⢳⠀⠀⠀  ⣉⣀⠀⠀⠀⠀⣰⢛⠙⣶{Fore.YELLOW}  ⣇")
    print(f"    ⠀⠀⠀⠀⢿{Fore.RED} ⠛⠋⠀⠀  ⣾⠋⠀⢱⠀⠀⠀⠘⠲⠗⠋{Fore.YELLOW}  ⣿")
    print("    ⠀⠀⠀⠀⠘⢷⡀",Fore.RED,"⠀⠀ ⠈⠓⠒⠋",Fore.YELLOW,"⠀⠀⠀⠀⠀⠀⠀⢻⡇")
    print("    ⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀")
    print("    ⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁",Fore.WHITE)
    return None
def adminmenu():
    time.sleep(1)
    print(Fore.BLUE,Style.BRIGHT,"\n_______________________________________________")
    print("_________________",Fore.MAGENTA,"[ Admin ]",Fore.BLUE,"_________________\n",Fore.GREEN)
    print("  1 - See list of users.\n  2 - Change user rights.\n",Fore.RED,"0 - Go back",Fore.BLUE)
    print("_______________________________________________\n———————————————————————————————————————————————\n",Fore.WHITE,Style.NORMAL)
    adminchoice = input("Your choice: ")
    return adminchoice
main()