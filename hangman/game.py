def Mygame(word_save, status_list):
    "this program is use to run the hangman's game"
    import random

    #Word List  
    word_list=['TAXICAR','SMARTPHONE','PUBG','TREADMILL','RICKASTELY','VINDIESEL','GLUCORSE','BROMINE','BANANA','KSI',
               'CEYLON','CUPBOARD','TITANIC','AFTEREFFECTS','KEYBOARD','META','SPIDERMAN','MOUSE','CHRISTMASDAY','UPS']
    #Hint list
    hint_list=['A Vehicle which is used to transport people form one place to another','A small portable device which we use very frequently','A Multiplayer shooting game',
               'Exercise machine we always uesd to run','Artist who sings Never going to give you up','Fast and Furious actor who always says FAMILY','Name of this formula C6 H12 O6',
               'Red brown gas at room temperature which is less denser than air','Pure yellow color fruit','Youtuber Boxer who defeated Logan Paul','Former country name of Sri lanka',
               'a piece of furniture with a door and typically shelves,used for storage','A ship which was knocked by an iceburg','Adobe digital video editing software',
               'A device where you write to the display of the monitor','Facebook''s new name','Red and Blue suit marvel hero',
               'A hand-held pointing device which the pointer moves on the display','Day of december 25th','A device that provides battery backup when the electrical power fails']
    #creating variables
    word = word_list[random.randrange(20)]
    word_save.append(word)
    chances=(len(word))
    bl_list=[]
    gus_list=[]

    #creating blanks by looping
    print("\n\n\n")
    for i in range(len(word)):
        bl_list.append(" _ ")

    #Displays the Hint for the user to understand
    print("Hint : ",hint_list[word_list.index(word)])

    #looping the no of chances  by using blank list
    while chances!=0:
    
        print(''.join(bl_list))
        win=("".join(bl_list))
        if win==word:               #creating a condtion to check wheather the user has won the game
            print("\ncongratulations")
            print("hidden word was",word)
            status_list.append("WON")
            print("MISSION PASSED + RESPECT")
            
            break

        print("\n")
        print("you have",chances,"chances left")#displays the chances left 
        gus=input("\n\nEnter a letter : ")
        gus=gus.upper()
        if gus in gus_list: #as u give the wrong word(gus) it tells to display the correct word again
            print("You have aleady guessed letter",gus,'before ')
            print("Please try again")
            continue
        gus_list.append(gus)
        if gus in word:
            for d in range(len(word)):
                if word[d]==gus:
                    bl_list[d]=gus
            #as u guessed the word correctly it displays the word form the list
            print(''.join(bl_list))
            print("\nWell done!!", gus, "is in the hidden word")
            # as u gueesed the word wrongly and 0 chances it displays as lost 
        else:
            print(' '.join(bl_list))
            print("\nOOOPS!!! letter",gus, "is not in the word")
            chances -= 1
            if chances == 0:
                print("the correct answer is",word)
                print("you have no more chances left")
                status_list.append("LOST")
                print("MISSION FAILED")
                print("Play again")
       #returns the code u wrote

    return word_save, status_list
