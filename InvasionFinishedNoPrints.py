import sys

#Gameplay
Turn = 0

#Inventory
flashlight = False
knife = False
gun = False

#Knowledge
RestroomKnowledge = False
StorageKnowledge = False

#Endings

ending1 = "You think nothing of the warning & shrug it off. You go to sleep and... never wake up. The end."
ending2 = "You sit on the couch and watch some television! The power suddenly goes off and you hear the door open, you turn to the door and see a flash and loud bang. *BANG* Your world goes dark. The End."
ending3 = "You hide. You hear the door open. You look at the door and see a flash and loud bang. *BANG* Your world goes dark. The End."
ending4 = "You hide. Gun in hand. You hear the door open and fire towards the direction of the noise. *BANG* *BANG* *BANG* *BANG* You calm down and relax. However, you feel a cold metal barrel on your head. Your world goes dark. The End."
ending5 = "You hide. Gun in hand. Flashlight shining the door. You hear and see the door open. You open fire at the killer. *BANG* *BANG* *BANG* *BANG* The killer is dead. You sit there, adrenaline rushing. You stay up to see the sun rise. You are safe. It's over. The End."
ending6 = "You hide. Knife in hand. You hear the door open and rush towards the direction of the noise. You stab into the darkness hitting something. *THUNK* *THUD* *CRRR* *SHHHK* The knife is taken out of your hands. You feel a cold metal barrel on your head. Your world goes dark. The End."
ending7 = "You hide. Knife in hand. Flashlight shining the door. You hear and see the door open. You rush at the killer and tumble them down. You stab repeatdely. *SPLAT* *SQUELCH* *PLAP* You get shot in the process by the killer. *BANG* But with your adrenaline running through your system you don't feel it. The killer is dead. You sit there, blood stained. Your adrenaline calms down and you start to feel the pain of the gun shot wound. The world goes dark.. ... But it glows again as you open your eyes, you are in a hospital bed.  You are safe. It's over. The End."
ending8 = "You hide. Gun in hand. Knife on belt. You hear the door open and fire towards the direction of the noise. *BANG* *BANG* *BANG* *BANG* You calm down and relax. However, you feel a cold metal barrel on your head. You quickly grab the knife from your belt and stab the killer in the leg. *SPLAT* *SQUELCH* *PLAP* They shoot you while they are struggling to get you off. *BANG* But your adrenaline running through you makes you ignore it and keep stabbing. The killer is dead. You sit there, blood stained. Your adrenaline calms down and you start to feel the pain of the gun shot wound.The world goes dark.. ... But it glows again as you open your eyes, you are in a hospital bed.  You are safe. It's over. The End."
ending9 = "You hide. Gun in hand. Knife on belt. Flashlight shining the door. You hear and see the door open. You open fire at the killer. *BANG* *BANG* *BANG* *BANG* You sit there, adrenaline rushing. However you notice the killer reaching for his gun. You quickly aim your gun and shoot, but you are out of bullets. With no time to waste, you pull your knife out and stab the reaching hand.  Repeatedly stabbing their hand and eventually stabbing their back. *SPLAT* *SQUELCH* *PLAP* The killer is dead. You sit down, blood stained. You stay up to see the sun rise. You are safe. It's over. The End."

#Start of Game
def menu():

    # Title and story

    print("========================")
    print("        INVASION        ")
    print("========================")

    print("You're on vacation in a small rural town Airbnb, home alone, dark night, and are getting ready for bed.")
    print("However, your phone gives out a loud alert warning the town has an armed and dangerous serial killer on the loose.")
    print("Before you can finish reading the message, your phone dies and you remember you lost your charger.")
    print("You are left standing in your room, with said warning in your thoughts.")

#Area 1 - Bedroom
def bedroom():
    global Turn, gun, flashlight, knife, RestroomKnowledge, StorageKnowledge

    while True:

        if Turn >= 7:
            blackout()
            return
        
        print("What do you do?")
        print("")
        print("[1] Check Closet")
        print("[2] Check Night Stand")
        print("[3] Walk Into Hallway")
        print("[4] Go To Sleep")
        print("")
                
        choice = input("> ")

        if choice == "1":

            print("You check your closet and see clothes/boxes. Look closer?")
            print("[Y] Yes")
            print("[N] No")

            closestChoice = input("> ").lower()

            if  closestChoice == "y":
                print("You find your gunbox, open it & take your hand gun.")
                Turn += 3 
                gun = True
        
            elif closestChoice == "n":
                print("You close the closet.")
                Turn += 1
        

        elif choice == "2":
            print("You open your night stand drawers and find nothing of use in them")
            Turn += 1


        elif choice == "3":
            print("You walk out the door")
            Turn +=1
            hallway()
            return

        elif choice == "4":
            print(ending1)
            sys.exit()

#Area 2 - Hallway
def hallway():
    global Turn, gun, flashlight, knife, RestroomKnowledge, StorageKnowledge
    print ("You walk into the hallway, kitchen, living room, & closed doors are in view.")
    print ("")

    while True:

        if Turn >= 7:
            blackout()
            return

        print ("What do you do?")
        print("")
        if RestroomKnowledge:
            print("[1] Check Restroom")
        else:
            print("[1] Check Door 1")
        
        if StorageKnowledge:
            print("[2] Check Storage Room")
        else:
           print("[1] Check Door 2") 

        print("[3] Check Kitchen")
        print("[4] Check Living Room")       
        print("[5] Sit on couch")
        print("")

        choice = input("> ")

        if choice == "1":

            print("You open the door and it is the restroom. Look closer?")
            print("[Y] Yes")
            print("[N] No")

            closestChoice = input("> ").lower()

            if  closestChoice == "y":
                print("You search around, but there is nothing of use.")
                Turn += 2 
                RestroomKnowledge = True
        
            elif closestChoice == "n":
                print("You close the door.")
                Turn += 1
                RestroomKnowledge = True

        elif choice == "2":
            print("You open the door and it is the storage room. Look closer?")
            print("[Y] Yes")
            print("[N] No")

            closestChoice = input("> ").lower()

            if  closestChoice == "y":
                print("You search around, and find a flashlight!")
                Turn += 2 
                StorageKnowledge = True
        
            elif closestChoice == "n":
                print("You close the door.")
                Turn += 1
                StorageKnowledge = True

        elif choice == "3":
            print("You look around the kitchen and pick up the sharpest knife you see.")
            Turn += 2
            knife = True

        elif choice == "4":
            print("You look around the living room, but find nothing of use.")    
            Turn += 1

        elif choice == "5":
            print(ending2)
            sys.exit()

#Area 3 - Blackout
def blackout():
    global Turn, gun, flashlight, knife, RestroomKnowledge, StorageKnowledge
    print ("You hear ruffling and a snap. The lights flicker and there's a total black out. You need to hide, FAST! Where are you hiding?")
    print ("")

    while True:
               
        print ("What do you do?")
        print("")
        if flashlight and RestroomKnowledge:
            print("[1] Hide in Restroom")
        elif RestroomKnowledge:
            print("[1] Hide in Restroom")
        elif flashlight:
            print("[1] Hide behind Door 1")       
        else:
            print("[1] Hide in ???")
        
        if flashlight and StorageKnowledge:
            print("[2] Hide in Storage Room")
        elif flashlight:
            print("[2] Hide behind Door 2")
        elif StorageKnowledge:
            print("[2] Hide in Storage Room")    
        else:
            print("[2] Hide in ???") 

        print("[3] Hide in bedroom")
        print("")

        choice = input("> ")

        if choice == "1":
            print("You open the door and hide inside.")
            endings()
            return
        
        if choice == "2":
            print("You open the door and hide inside.")
            endings()
            return
        
        if choice == "3":
            print("You open the door and hide inside.")
            endings()
            return
#Area 4 - Endings

def endings():
    if flashlight and gun and knife:
        print(ending9)
        sys.exit

    elif gun and knife:    
        print(ending8)
        sys.exit

    elif flashlight and knife:
        print(ending7)
        sys.exit

    elif knife:
        print(ending6)
        sys.exit

    elif flashlight and gun:
        print(ending5)
        sys.exit

    elif gun:
        print(ending4)
        sys.exit

    else:
        print(ending3)
        sys.exit                
menu()
bedroom()
        



    

    
