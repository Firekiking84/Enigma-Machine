from Listes import *
import os

letters_number = 0

print("Je vais crypter ton message avec le fonctionnement de la machine Enigma de la Seconde Guerre Mondiale")

file = open(f"{chemin}/count_cryptage.txt", 'r')
informations = file.read()
file.close()
count_message = int(informations) + 1
informations = str(count_message)

file = open(f"{chemin}/count_cryptage.txt", "w+")
file.write(informations)
file.close()

os.mkdir(f"{chemin}/crypted_message/crypted_message_{count_message}")
file = open(f"{chemin}/crypted_message/crypted_message_{count_message}/crypted_message_{count_message}.txt", "w+")
coded_message = str(input("Quel est ton message secret ? --> ")).lower()
SpeCharac = "&'(-_)=][°/\|`#~!?,;.:§*$"
for x in range(len(SpeCharac)):
    coded_message = coded_message.replace(SpeCharac[x], "")
slot1 = str(input("Choisis le rotor du premier emplacement (réponse de 1 à 8)! --> "))
file.write(f"Paramètres : \n   Choix des rotors : \n        Premier rotor : n°{slot1}\n")
slot2 = str(input("Choisis le rotor du deuxième emplacement (réponse de 1 à 8)! --> "))
file.write(f"       Deuxième rotor : n°{slot2}\n")
slot3 = str(input("Choisis le rotor du troisième emplacement (réponse de 1 à 8)! --> "))
file.write(f"       Troisième rotor : n°{slot3}\n")
slot4 = str(input("Choisis le rotor du quatrième emplacement (réponse de 1 à 8)! --> "))
file.write(f"       Quatrième rotor : n°{slot4}\n")
reponse_valide = False
while not reponse_valide:
    reponse = str(input("Souhaites-tu le mode militaire, plus compliqué à décoder mais plus long à mettre en "
                            "place ! --> "))
    standard = False
    if reponse in oui:
        file.write(f"   Mode avancé:\n      Mode militaire : \n")
        already_used = []
        print("Tu vas maintenant devoir associé par chaque lettre de l'alphabet à une autre lettre de "
                  "l'alphabet.")
        test2 = 0
        while len(already_used) < 26:
            reponse_valide = False
            file.write(f"   Réflexions des lettres :\n ")
            while not reponse_valide:
                if alphabet[test2] not in already_used:
                    reponse = str(input(f"La paire de {alphabet[test2]} --> "))
                    if reponse in already_used:
                        print("Déjà utilisé !")
                        reponse_valide = False
                    elif reponse in alphabet:
                        reponse_valide = True
                        already_used.append(alphabet[test2])
                        already_used.append(reponse)
                        file.write(f"       {alphabet[test2]} --> {reponse}\n")
                        file2 = open(f"{chemin}\crypted_message/crypted_message_{count_message}\switch_letters_"
                                     f"{alphabet[test2]}.txt", "w+")
                        file2.write(reponse)
                        file2.close()
                        file2 = open(f"{chemin}\crypted_message/crypted_message_{count_message}\switch_letters_"
                                     f"{reponse}.txt", "w+")
                        file2.write(alphabet[test2])
                        file2.close()
                elif alphabet[test2] in already_used:
                    reponse_valide = True
                else:
                    print("Euh faut juste marquer une lettre de l'alphabet... C'est pas bien compliqué "
                              "pourtant")
            test2 = test2 + 1
    elif reponse in non:
        standard = True
        reponse_valide = True
        file.write(f"  Mode avancé:\n      Mode Standard")
        print("Ton message vas être codé dans le mode standard !")
        file.write(f"   Réflexions des lettres :\n ")
        for test2 in range(26):
            file.write(f"       {alphabet[test2]} --> {alphabet[25 - test2]}\n")
            file2 = open(f"{chemin}\crypted_message/crypted_message_{count_message}\switch_letters_{alphabet[test2]}"
                         f".txt", "w+")
            file2.write(alphabet[test2])
            file2.close()
decalage1 = 0
decalage2 = 0
decalage3 = 0
decalage4 = 0
reponse_valide = False
while not reponse_valide:
    reponse = str(input("Choississez le paramétrage du premier rotor (réponse de 0 à 25)--> "))
    if reponse in nombres:
        reponse_valide = True
        for x in range(27):
            if reponse == nombres[x]:
                decalage1 = x
    else:
        print("Je ne comprends pas ! Assure-toi d'avoir inscrit un nombre entre 0 et 25 inclus")
file.write(f"   Paramétrage :\n         Rotor n°1: {reponse}\n")
reponse_valide = False
while not reponse_valide:
    reponse = str(input("Choississez le paramétrage du deuxième rotor (réponse de 0 à 25)--> "))
    if reponse in nombres:
        reponse_valide = True
        for x in range(27):
            if reponse == nombres[x]:
                decalage2 = x
    else:
        print("Je ne comprends pas ! Assure-toi d'avoir inscrit un nombre entre 0 et 26 inclus")

file.write(f"   Paramétrage :\n         Rotor n°2: {reponse}\n")
reponse = str(input("Choississez le paramétrage du troisième rotor (réponse de 0 à 25) --> "))
reponse_valide = False
while not reponse_valide:
    if reponse in nombres:
        reponse_valide = True
        for x in range(27):
            if reponse == nombres[x]:
                decalage3 = x
    else:
        print("Je ne comprends pas ! Assure-toi d'avoir inscrit un nombre entre 0 et 25 inclus")

file.write(f"   Paramétrage :\n         Rotor n°: {reponse}\n")
reponse_valide = False
while not reponse_valide:
    reponse = str(input("Choississez le paramétrage du quatrième rotor (réponse de 0 à 25)--> "))
    if reponse in nombres:
        reponse_valide = True
        for x in range(27):
            if reponse == nombres[x]:
                decalage4 = x
    else:
        print("Je ne comprends pas ! Assure-toi d'avoir inscrit un nombre entre 0 et 26 inclus")

file.write(f"   Paramétrage :\n         Rotor n°1: {reponse}\n")
letter_choice = 0
crypted_letter = []
file.write(f"\nMessage à crypter : {coded_message}\n")
for test2 in range(len(coded_message)):
    if coded_message[test2] == " ":
        crypted_letter.append(" ")
        continue
    else:
        # Début du cryptage des lettres
        traited_letter = coded_message[test2]
        # Switch lettre selon ce qui a été déterminé avant
        file2 = open(f"{chemin}\crypted_message/crypted_message_{count_message}\switch_letters_{coded_message[test2]}"
                     f".txt", "r")
        traited_letter = file2.read()
        file2.close()
        ok = False
        if standard:
            for test3 in range(26):  # Tableau de réflection, switch lettre
                if traited_letter == alphabet[test3] and not ok:
                    traited_letter = connect_board[test3]
                    ok = True
        # Recherche position correspondante sur rotor fixe
        # C'est à dire de la position où il y a la même lettre que celle traitée
        for test3 in range(26):
            test_rotor = rotor_fixe1[test3]
            if traited_letter == test_rotor:
                break
        # Définition du décalage brut
        letter_choice = test3
        # Addition du décalage défini précédemment
        for x in range(decalage1):
            letter_choice = letter_choice - 1
            if letter_choice == -1:  # Remise à zéro à 26, nombre d'emplacement (0 compris) du rotor
                letter_choice = 25
        if slot1 == "1":  # Recherche du rotor choisi
            traited_letter = rotor1[letter_choice]  # Changement de la lettre traitée par celle du rotor
            # à l'emplacement souhaitée
        elif slot1 == "2":
            traited_letter = rotor2[letter_choice]
        elif slot1 == "3":
            traited_letter = rotor3[letter_choice]
        elif slot1 == "4":
            traited_letter = rotor4[letter_choice]
        elif slot1 == "5":
            traited_letter = rotor5[letter_choice]
        elif slot1 == "6":
            traited_letter = rotor6[letter_choice]
        elif slot1 == "7":
            traited_letter = rotor7[letter_choice]
        elif slot1 == "8":
            traited_letter = rotor8[letter_choice]
        # Recherche position correspondante sur rotor fixe
        # C'est à dire de la position où il y a la même lettre que celle traitée
        for test3 in range(26):
            test_rotor = rotor_fixe2[test3]
            if traited_letter == test_rotor:
                break
        letter_choice = test3
        # Addition des décalages défini
        for x in range(decalage2):
            letter_choice = letter_choice - 1
            if letter_choice == -1:
                letter_choice = 25
        if slot2 == "1":  # Recherche du rotor défini pour cet emplacement
            traited_letter = rotor1[letter_choice]  # Définition de la lettre correspondante
        elif slot2 == "2":
            traited_letter = rotor2[letter_choice]
        elif slot2 == "3":
            traited_letter = rotor3[letter_choice]
        elif slot2 == "4":
            traited_letter = rotor4[letter_choice]
        elif slot2 == "5":
            traited_letter = rotor5[letter_choice]
        elif slot2 == "6":
            traited_letter = rotor6[letter_choice]
        elif slot2 == "7":
            traited_letter = rotor7[letter_choice]
        elif slot2 == "8":
            traited_letter = rotor8[letter_choice]
        # Recherche de l'emplacement correspondant
        for test3 in range(26):
            test_rotor = rotor_fixe3[test3]
            if traited_letter == test_rotor:
                break
        letter_choice = test3
        # Addition des décalages défini
        for x in range(decalage3):
            letter_choice = letter_choice - 1
            if letter_choice == -1:
                letter_choice = 25
        if slot3 == "1":  # Recherche du rotor présent à cet emplacement
            traited_letter = rotor1[letter_choice]  # Définition de la lettre correspondante
        elif slot3 == "2":
            traited_letter = rotor2[letter_choice]
        elif slot3 == "3":
            traited_letter = rotor3[letter_choice]
        elif slot3 == "4":
            traited_letter = rotor4[letter_choice]
        elif slot3 == "5":
            traited_letter = rotor5[letter_choice]
        elif slot3 == "6":
            traited_letter = rotor6[letter_choice]
        elif slot3 == "7":
            traited_letter = rotor7[letter_choice]
        elif slot3 == "8":
            traited_letter = rotor8[letter_choice]
        # Recherche du bon emplacement
        for test3 in range(26):
            test_rotor = rotor_fixe4[test3]
            if traited_letter == test_rotor:
                break
        letter_choice = test3
        # Addition décalage défini
        for x in range(decalage4):
            letter_choice = letter_choice - 1
            if letter_choice == -1:
                letter_choice = 25
        if slot4 == "1":  # Recherche du rotor présent à l'emplacement
            traited_letter = rotor1[letter_choice]  # Définition de la lettre correspondante
        elif slot4 == "2":
            traited_letter = rotor2[letter_choice]
        elif slot4 == "3":
            traited_letter = rotor3[letter_choice]
        elif slot4 == "4":
            traited_letter = rotor4[letter_choice]
        elif slot4 == "5":
            traited_letter = rotor5[letter_choice]
        elif slot4 == "6":
            traited_letter = rotor6[letter_choice]
        elif slot4 == "7":
            traited_letter = rotor7[letter_choice]
        elif slot4 == "8":
            traited_letter = rotor8[letter_choice]
        # Fin du tour aller, début du tour retour
        # Réflecteur :
        ok = False
        for test3 in range(26):  # Réflecteur, switch lettre
            if traited_letter == alphabet[test3] and not ok:
                traited_letter = reflector[test3]
                ok = True
        if slot4 == "1":  # Recherche du rotor présent sur cet emplacement
            for test3 in range(26):
                test_rotor = rotor1[test3]
                if traited_letter == test_rotor:  # Recherche de la lettre correspondante sur le rotor movible
                    letter_choice = test3  # Définition de l'emplacement sur le rotor
                    for x in range(decalage4):  # Addition du décalage
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    # Définition de la lettre traitée par rapport au paramètre défini précédemment
                    traited_letter = rotor_fixe4[letter_choice]
                    break
        elif slot4 == "2":  # Recherche du rotor présent sur cet emplacement
            for test3 in range(26):
                test_rotor = rotor2[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage4):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe4[letter_choice]
                    break
        elif slot4 == "3":  # Recherche du rotor présent sur cet emplacement
            for test3 in range(26):
                test_rotor = rotor3[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage4):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe4[letter_choice]
                    break
        elif slot4 == "4":  # Recherche du rotor présent sur cet emplacement
            for test3 in range(26):
                test_rotor = rotor4[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage4):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe4[letter_choice]
                    break
        elif slot4 == "5":  # Recherche du rotor présent sur cet emplacement
            for test3 in range(26):
                test_rotor = rotor5[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage4):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe4[letter_choice]
                    break
        elif slot4 == "6":  # Recherche du rotor présent sur cet emplacement
            for test3 in range(26):
                test_rotor = rotor6[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage4):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe4[letter_choice]
                    break
        elif slot4 == "7":  # Recherche du rotor présent sur cet emplacement
            for test3 in range(26):
                test_rotor = rotor7[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage4):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe4[letter_choice]
                    break
        elif slot4 == "8":  # Recherche du rotor présent sur cet emplacement
            for test3 in range(26):
                test_rotor = rotor8[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage4):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe4[letter_choice]
                    break

        # Check du 3ème emplacement
        if slot3 == "1":
            for test3 in range(26):
                test_rotor = rotor1[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage3):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe3[letter_choice]
                    break
        elif slot3 == "2":
            for test3 in range(26):
                test_rotor = rotor2[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage3):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe3[letter_choice]
                    break
        elif slot3 == "3":
            for test3 in range(26):
                test_rotor = rotor3[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage3):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe3[letter_choice]
                    break
        elif slot3 == "4":
            for test3 in range(26):
                test_rotor = rotor4[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage3):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe3[letter_choice]
                    break
        elif slot3 == "5":
            for test3 in range(26):
                test_rotor = rotor5[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage3):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe3[letter_choice]
                    break
        elif slot3 == "6":
            for test3 in range(26):
                test_rotor = rotor6[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage3):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe3[letter_choice]
                    break
        elif slot3 == "7":
            for test3 in range(26):
                test_rotor = rotor7[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage3):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe3[letter_choice]
                    break
        elif slot3 == "8":
            for test3 in range(26):
                test_rotor = rotor8[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage3):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe3[letter_choice]
                    break

        # Check du 2ème emplacement
        if slot2 == "1":
            for test3 in range(26):
                test_rotor = rotor1[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage2):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe2[letter_choice]
                    break
        elif slot2 == "2":
            for test3 in range(26):
                test_rotor = rotor2[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage2):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe2[letter_choice]
                    break
        elif slot2 == "3":
            for test3 in range(26):
                test_rotor = rotor3[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage2):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe2[letter_choice]
                    break
        elif slot2 == "4":
            for test3 in range(26):
                test_rotor = rotor4[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage2):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe2[letter_choice]
                    break
        elif slot2 == "5":
            for test3 in range(26):
                test_rotor = rotor5[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage2):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe2[letter_choice]
                    break
        elif slot2 == "6":
            for test3 in range(26):
                test_rotor = rotor6[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage2):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe2[letter_choice]
                    break
        elif slot2 == "7":
            for test3 in range(26):
                test_rotor = rotor7[test3]
                if traited_letter == test_rotor:
                    print("Check 2.2!")
                    letter_choice = test3
                    for x in range(decalage2):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe2[letter_choice]
                    break
        elif slot2 == "8":
            for test3 in range(26):
                test_rotor = rotor8[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage2):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe2[letter_choice]
                    break

        # Check du premier emplacement
        if slot1 == "1":
            for test3 in range(26):
                test_rotor = rotor1[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage1):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe1[letter_choice]
                    break
        elif slot1 == "2":
            for test3 in range(26):
                test_rotor = rotor2[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage1):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe1[letter_choice]
                    break
        elif slot1 == "3":
            for test3 in range(26):
                test_rotor = rotor3[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage1):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe1[letter_choice]
                    break
        elif slot1 == "4":
            for test3 in range(26):
                test_rotor = rotor4[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage1):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe1[letter_choice]
                    break
        elif slot1 == "5":
            for test3 in range(26):
                test_rotor = rotor5[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage1):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe1[letter_choice]
                    break
        elif slot1 == "6":
            for test3 in range(26):
                test_rotor = rotor6[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage1):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe1[letter_choice]
                    break
        elif slot1 == "7":
            for test3 in range(26):
                test_rotor = rotor7[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage1):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe1[letter_choice]
                    break
        elif slot1 == "8":
            for test3 in range(26):
                test_rotor = rotor8[test3]
                if traited_letter == test_rotor:
                    letter_choice = test3
                    for x in range(decalage1):
                        letter_choice = letter_choice + 1
                        if letter_choice == 26:
                            letter_choice = 0
                    traited_letter = rotor_fixe1[letter_choice]
                    break
        # tableau de réflection dans l'autre sens
        ok = False
        if standard:
            for test3 in range(26):  # Tableau de réflection, switch lettre
                if traited_letter == alphabet[test3] and not ok:
                    traited_letter = connect_board[test3]
                    ok = True
        elif not standard:
            file2 = open(f"{chemin}\crypted_message/crypted_message_{count_message}\switch_letters_{traited_letter}"
                         f".txt", "r")
            traited_letter = file2.read()
            file2.close()
        # Passage à la lettre suivante
        letters_number = letters_number + 1
        # On avance le rotor de 1 emplacement et si il a finit...
        decalage1 = decalage1 + 1
        if decalage1 == 26:
            decalage1 = 0
            decalage2 = decalage2 + 1
            if decalage2 == 26:
                decalage2 = 0
                decalage3 = decalage3 + 1
                if decalage3 == 26:
                    decalage3 = 0
                    decalage4 = decalage4 + 1
                    if decalage4 == 26:
                        decalage4 = 0
        crypted_letter.append(traited_letter)
print("Cryptage terminé !")
file.write(f"Message codé : ")
for test in range(len(crypted_letter)):
    file.write(crypted_letter[test].strip())
file.close()