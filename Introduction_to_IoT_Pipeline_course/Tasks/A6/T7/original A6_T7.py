def ROT13():
    convertedtext = ""
    for char in passphrase:
        if 'a' <= char <= 'z':
            newchar = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            newchar = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            newchar = char
        convertedtext += newchar
    if convertedtext:
        convertedtext = convertedtext[0].upper() + convertedtext[1:]
    return convertedtext

with open("player_progress.txt", "r")as file:
    lines = file.readlines()
    journey = lines[-2].strip().split(';')
    clocation = int(journey[0])
    nlocation = int(journey[1])
    passphrase = journey[2]

if clocation == 0:
    c_l_name = "home."
    n_l_name = "Galba's palace."
elif clocation == 1:
    c_l_name = "Galba's palace."
    n_l_name = "Otho's palace."
elif clocation == 2:
    c_l_name = "Otho's palace."
    n_l_name = "Vitellius' palace."
elif clocation == 3:
    c_l_name = "Vitellius' palace."
    n_l_name = "Vespasian's palace."
elif clocation == 4:
    c_l_name = "Vespasian's palace."
    n_l_name = "home."
def main():
    convertedtext = ROT13()
    print("Travel starting.")
    print("Currently at", c_l_name)
    print("Travelling to ", n_l_name, "..", sep='')
    print("...Arriving to the", n_l_name)
    print("Passing the guard at the entrance.")
    print('"', convertedtext, '!"', sep='')
    print("Looking for the message in the palace...")
    print("Ah, there it is! Seems cryptic.")
    return None
main()
if clocation == 0:
    txtname = "1-discipline.txt"
    gkg_name = "1_qvfpvcyvar.gkg"
    nphrase = "nzovgvba"
elif clocation == 1:
    txtname = "2-ambition.txt"
    gkg_name = "2_nzovgvba.gkg"
    nphrase = "vaqhytrapr"
elif clocation == 2:
    txtname = "3-indulgence.txt"
    gkg_name = "3_vaqhytrapr.gkg"
    nphrase = "fgnovyvgl"
elif clocation == 3:
    txtname = "4-stability.txt"
    gkg_name = "4_fgnovyvgl.gkg"
    nphrase = "None"
with open(gkg_name, "r") as file:
    lines = file.readlines()
    fline = lines[0]
    content = lines[1:]

Savedata = f"\n{clocation + 1};{nlocation + 1};{nphrase}\n "
with open("player_progress.txt", "a") as file:
    file.write(Savedata)

print("[Game] Progress autosaved!")

ct = []
for line in content:
    for char in line:
        if 'a' <= char <= 'z':
            ct.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            ct.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        else:
            ct.append(char)
with open(txtname, 'w')as file:
    file.writelines(ct)

print("Deciphering Emperor's message...")
print("Looks like I've got now ", sep=' ', end='')
print("the plain version copy of the Emperor's message.")
print("Time to leave...")
print("Travel ending.")