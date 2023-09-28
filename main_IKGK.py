# Final Project Game - Blackfoot
# Isabelle Kwan and Gurleen Kang
# December 5, 2022

import pygame
import draw
import random
import cmpt120image

###############################################################
# Keep this block at the beginning of your code. Do not modify.
def initEnv():
    print("\nWelcome! Before we start...")
    env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    while env not in "mri":
        print("Environment not recognized, type again.")
        env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    print("Great! Have fun!\n")
    return env

# Use the playSound() function below to play sounds. 
# soundfilename does not include the .wav extension, 
# e.g. playSound(apples,ENV) plays apples.wav
def playSound(soundfilename,env):
    if env == "m":
        exec("sounds." + soundfilename + ".play()")
    elif env == "r":
        from replit import audio
        audio.play_file("sounds/"+soundfilename+".wav")
    elif env == "i":
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/"+soundfilename+".wav")
        pygame.mixer.music.play()

ENV = initEnv()
###############################################################
numItems = 3
n = True
while n is True:
    print("\nMAIN MENU\n1. Learn - Word Flashcards\n2. Play - Seek and Find Game\
          \n3. Settings - Change Difficulty\n4. Exit")

    choice = input("\nChoose an option: ").strip(" ,.?!")
    file = open("blackfoot.csv")
    items = []
    for line in file:
        item = line.split("\n")
        items.append(item[0])
        
    # Settings
    if choice == "3":
        print("You are current learning",numItems,"words.")
        num = int(input("How many would you like to learn(3-12)? "))
        if num in list(range(3,13)):
            numItems = num
        else:
            print("Sorry, that's not a valid number. Resetting to 3 words.")
            numItems = 3

    # Initialize learn statements
    learnItems = items[:numItems]
    
    # Learn
    if choice == "1":
        print("\nLEARN")
        for i in range(len(learnItems)):
            img = cmpt120image.getImage("images/"+learnItems[i]+".png")
            canvas = cmpt120image.getWhiteImage(400,300)
            playSound(learnItems[i],"i")
            cmpt120image.showImage(draw.distributeItems(canvas,img,1))
            input(str(i+1)+". Press enter to continue...")

    # Play
    if choice == "2":
        print("""PLAY
This is a seek and find game. You will hear a word.
Count how many of that word you find!
""")
        rounds = int(input("How many rounds would you like to play? "))
        # Create Challenge List and Shuffle List
        challenge_list = random.sample(learnItems,3)
        
        while rounds > 0:
            correct_index = random.randint(0,2)
            canvas = cmpt120image.getWhiteImage(400,300)
            num_n = 0
            
            # Distribute Items
            for i in range(3):
                img = cmpt120image.getImage("images/"+challenge_list[i]+".png")
                
                # Recolor Image
                red_component = random.randint(0,255)
                green_component = random.randint(0,255)
                blue_component = random.randint(0,255)
                colour = (red_component, green_component, blue_component)

                img = draw.recolorImage(img,colour)
                
                # Randomly Minify
                min_choice = random.randint(0,1)
                if min_choice == 0:
                    img = draw.minify(img)
                    
                # Randomly Mirror
                mirror_choice = random.randint(0,1)
                if mirror_choice == 0:
                    img = draw.mirror(img)
                
                # Set correct guess and distribute items
                num_items = random.randint(1,4)
                if challenge_list[i] == challenge_list[correct_index]:
                    num_n = num_items
     
                distribute = draw.distributeItems(canvas,img,num_items)
                cmpt120image.showImage(distribute)
                
            # Play sound, evaluate guess    
            playSound(challenge_list[correct_index],"i")
            try: 
                guess = int(input("Listen to the word. How many of them can you find? "))
                if guess == num_n:
                    input("Right! Press Enter to continue.")
                else:
                    input("Sorry, there were {}. Press Enter to continue. ".format(num_n))
                # Move to next round
                rounds -= 1
            except:
                print("Sorry, invalid answer. Try Again.")

    # Exit
    if choice =="4":
        n = False
        print("Goodbye!")

    

