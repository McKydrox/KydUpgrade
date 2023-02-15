from pystyle import Colorate, Colors, System, Center, Anime
from colorama import init, Fore
import os

init(),

logo = '''
        
$$\   $$\                $$\ $$\   $$\                                              $$\           
$$ | $$  |               $$ |$$ |  $$ |                                             $$ |          
$$ |$$  /$$\   $$\  $$$$$$$ |$$ |  $$ | $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$\   $$$$$$$ | $$$$$$\  
$$$$$  / $$ |  $$ |$$  __$$ |$$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\ \____$$\ $$  __$$ |$$  __$$\ 
$$  $$<  $$ |  $$ |$$ /  $$ |$$ |  $$ |$$ /  $$ |$$ /  $$ |$$ |  \__|$$$$$$$ |$$ /  $$ |$$$$$$$$ |
$$ |\$$\ $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |     $$  __$$ |$$ |  $$ |$$   ____|
$$ | \$$\\$$$$$$$ |\$$$$$$$ |\$$$$$$  |$$$$$$$  |\$$$$$$$ |$$ |     \$$$$$$$ |\$$$$$$$ |\$$$$$$$\ 
\__|  \__|\____$$ | \_______| \______/ $$  ____/  \____$$ |\__|      \_______| \_______| \_______|
         $$\   $$ |                    $$ |      $$\   $$ |                                       
         \$$$$$$  |                    $$ |      \$$$$$$  |                                       
          \______/                     \__|       \______/                                        

Please press Enter ...                                            
                                                                                                                                
'''[1:]

System.Size(100, 30)
System.Title('KydroxTools')
Anime.Fade(Center.Center(logo), Colors.blue_to_cyan, Colorate.Vertical, enter=True)

print(Fore.BLUE + "Chargement de la liste des applications ... ")
os.system("winget upgrade --")
a = input(Fore.BLUE + "Quel application voulez-vous mettre a jour : ")
os.system("winget upgrade -- {a}")

print(Fore.RED + "Vous pouvez maintenant fermer l'application.")

    



 