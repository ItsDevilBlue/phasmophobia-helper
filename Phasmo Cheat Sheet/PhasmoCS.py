import os
import random
import webbrowser
import subprocess
maps = ['bleadsdale', 'edgefield', 'grafton', 'ridgeview', 'tanglewood', 'willow', 'brownstone', 'maple', 'prison', 'asylum']
difficultys = ['amateur', 'intermediate', 'professional', 'nightmare']

def main():
    random_map = random.choice(maps)
    random_difficulty = random.choice(difficultys)

    user = input(": ").lower()
    user = user.split(' ')

    for word in user:
        if word == 'r':
            for word in user:
                for Map in maps:
                    if word == Map:
                        maps.remove(Map)
                        print(f"Removed {Map} from Maps")
                for Difficulty in difficultys:
                    if word == Difficulty:
                        difficultys.remove(Difficulty)
                        print(f"Removed {Difficulty} from Difficultys")
            main()
                        
        if word == 'random':
            print(f'\nThe map {random_map.capitalize()} on {random_difficulty.capitalize()} difficulty has been selected\n')
            main()
        if word == 'p' or word == 'phasmo' or word == 'phasmophobia':
            print("\nStarting Phasmophobia...\n")
            os.startfile('E:/SteamLibrary/steamapps/common/Phasmophobia/Phasmophobia.exe')
            main()
        if word == 'cheat' or word == 'doc' or word == 'sheet':
            print("\nStarting Phasmophobia Cheat Sheet...\n")
            os.startfile('PhasmoCheatSheet.txt')
            main()
        if word == 'd' or word == 'discord':
            print("\nStarting Discord...\n")
            os.startfile('C:/Users/jayde/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Discord Inc/Discord.lnk')
            main()
        if word == 't' or word == 'trello':
            print("\nOpening Phasmophobia Tello Page...\n")
            webbrowser.open('https://trello.com/b/9QrnqQ1j/phasmophobia')
            main()
        if word == 'c' or word == 'close':
            print("\nClosing Phasmophobia...\n")
            subprocess.call(["taskkill","/F","/IM","Phasmophobia.exe"])
            main()
        if word == 'j' or word == 'journal':
            print("\nOpening Phasmophobia Journal...\n")
            webbrowser.open('https://sirjimmothy.github.io/phasmo/')
            main()
        if word == 'map' or word == 'm':
            for word in user:
                if word == 'tanglewood':
                    print("\nOpening Tanglewood Layout...\n")
                    os.startfile("C:/Users/jayde/OneDrive/Desktop/Phasmo Cheat Sheet/Maps/tanglewood.png")
                if word == 'ridgeview':
                    print("\nOpening Ridgeview Layout...\n")
                    os.startfile("C:/Users/jayde/OneDrive/Desktop/Phasmo Cheat Sheet/Maps/ridgeview.png")
                if word == 'grafton':
                    print("\nOpening Grafton Layout...\n")
                    os.startfile("C:/Users/jayde/OneDrive/Desktop/Phasmo Cheat Sheet/Maps/ridgeview.png")
                if word == 'edgefield':
                    print("\nOpening Edgefield Layout\n")
                    os.startfile("C:/Users/jayde/OneDrive/Desktop/Phasmo Cheat Sheet/Maps/ridgeview.png")
                if word == 'brownstone':
                    print("\nOpening Brownstone Layout...\n")
                    os.startfile("C:/Users/jayde/OneDrive/Desktop/Phasmo Cheat Sheet/Maps/brownstone.png")
                if word == 'bleasdale':
                    print("\nOpening Bleasdale Layout...\n")
                    os.startfile("C:/Users/jayde/OneDrive/Desktop/Phasmo Cheat Sheet/Maps/bleasdale.png")
                if word == 'asylum':
                    print("\nOpening Asylym Layout...\n")
                    os.startfile("C:/Users/jayde/OneDrive/Desktop/Phasmo Cheat Sheet/Maps/asylum.png")
                if word == 'prison':
                    print("\nOpening Prison Layout...\n")
                    os.startfile("C:/Users/jayde/OneDrive/Desktop/Phasmo Cheat Sheet/Maps/prison.png")
                if word == 'maple':
                    print("\nOpening Maple Layout...\n")
                    os.startfile("C:/Users/jayde/OneDrive/Desktop/Phasmo Cheat Sheet/Maps/maple.png")
                if word == 'w' or word == 'web' or word == 'website':
                    print("\nOpening Phasmophobia Layout Page...\n")
                    webbrowser.open('https://phasmo.karotte.org')
            main()
    print("\nInvalid\n")
    main()
main()
