import time, os
import winsound

def minuteur(minutes):
    secondes = minutes * 60
    while secondes > 0:
        m, s = divmod(secondes, 60)
        temps_restant = f"{m:02d}:{s:02d}"
        print(temps_restant, end="\r")
        time.sleep(1)
        secondes -= 1
    
    print("Temps écoulé !")
    winsound.PlaySound("alarm.wav", winsound.SND_FILENAME)

if __name__ == "__main__":
    duree = int(input("Entrez la durée du minuteur en minutes : "))
    minuteur(duree)


os.system("pause")
