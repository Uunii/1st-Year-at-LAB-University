filename = 'player_progress.txt'

def Text_cipher(text):
    result = []
    for characters in text:
        for char in characters:
            if 'a' <= char <= 'z':
                result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
            elif 'A' <= char <= 'Z':
                result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
            else:
                result.append(char)
    return ''.join(result)

def Pass_cipher(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            newchar = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            newchar = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            newchar = char
        result += newchar
    if result:
        result = result[0].upper() + result[1:]
    return result

def read_progress():
    with open(filename, 'r') as f:
        splitLines = f.readlines()
        parts = splitLines[-2].strip().split(';')
        current_location = parts[0]
        NextLocationId = parts[1]
        passphrase = parts[2]
        return int(current_location), int(NextLocationId), passphrase
       

def save_progress(current_location, NextLocationId, passphrase):
    with open(filename, 'a') as f:
        f.write(f"\n{current_location};{NextLocationId};{passphrase}\n")

def travel(current_location, NextLocationId, passphrase):
    location_list = {
        0: "home", 1: "Galba's palace", 2: "Otho's palace", 3: "Vitellius' palace", 4: "Vespasian's palace"
    }
    print("Travel starting.")
    print(f"Currently at {location_list[current_location]}.")
    print(f"Travelling to {location_list[NextLocationId]}...")
    print(f"...Arriving to the {location_list[NextLocationId]}.")
    print("Passing the guard at the entrance.")

    Passphrase = Pass_cipher(passphrase)
    print(f"\"{Passphrase}!\"")

    message_file = f"{NextLocationId}_{passphrase}.gkg"
    with open(message_file, 'r') as f:
        message = f.readlines()
        ciphered_message = message[1:]
        
    print("Looking for the message in the palace...")
    print("Ah, there it is! Seems cryptic.")

    plain_message = Text_cipher(ciphered_message)
    text = Text_cipher(passphrase)
    filename2 = f"{NextLocationId}-{text}.txt"
    with open(filename2, 'w') as f:
        f.write(plain_message)

    print("[Game] Progress autosaved!")
    print("Deciphering Emperor's message...")
    print("Looks like I've got now the plain version copy of the Emperor's message.")
    print("Time to leave...")
    print("Travel ending.")
    return True

def main() -> None:
    progress = read_progress()

    current_location, NextLocationId, passphrase = progress

    if travel(current_location, NextLocationId, passphrase):
        if NextLocationId < 5:
            New_location = NextLocationId + 1
            clocation = f"{NextLocationId}_{passphrase}.gkg"
            with open(clocation, 'r')as f:
                f = f.readlines()
                first_line = f[0].split(";")
                newPass = first_line[2]
            save_progress(NextLocationId, New_location, newPass)
        else:
            exit()
main()
