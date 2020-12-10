import random
kutije = [100, 20, 20, 5, 5, 5, 5, 5, "Extra Life", "Game Over","Game Over","Game Over"]
secondChance = [5, 10 ,20, "Druga Prilika"]
extralife = 0
cash = 0
drugihSansi = 0
random.shuffle(kutije)
random.shuffle(secondChance)


for i in range(len(kutije)):
    if kutije[i]== "Game Over":
        if extralife>0:
            print("Izgubio si ali imas ekstra zivot, nastavljam dalje otvarat kutije")
            extralife -= 1
            continue
        else:
            if drugihSansi > 0:
                print("Izgubio si sve svoje sanse! Igra za tebe je gotova!")
                break
            else :    
                print("Izgubio si! Ali tu nije kraj! Za tebe imam jos jednu nagradu!")
                drugihSansi +=1
                drugaNagrada = random.choice(secondChance)
                if drugaNagrada == 5 or drugaNagrada == 10 or drugaNagrada == 20:
                    print("Osvojio si ", drugaNagrada,"$. I tu je kraj ove igre!")
                    cash = cash + drugaNagrada
                    break
                else:
                    print("Osvojio si jos jednu sansu!!! Pokrecem opet igru")
                    continue
    elif kutije[i]== 100 or kutije[i]== 20 or kutije[i]== 5:
        cash = cash + kutije[i]
        print("Osvojio si: ",kutije[i],"$\nTrenutno imaš: ",cash)
    elif kutije[i]== "Extra Life":
        print("Osvojio si extra zivot! Nakon Game Overa igra ce se nastaviti..")
        extralife += 1
