
import time
import random
# from playsound import playsound

#a way to play a song whilst the game runs
# from playsound import playsound
# playsound("D:\Projects\Game_Dev\Mongol Quest\Game_files\Mongol_quest_theme_original.mp4a")

player_name = ""
player_age = ""

archery_contestant = "Urgtruk"

character_selection = ["(1) Warrior", "(2) Scolar", "(3) Theif"]
character = ""

alive = 1

clans = ["Keraites Clan", "Khamag Mongol Clan", "Naiman Clan", "Mergid Clan", "Tatar Clan"]
clans_joined = 3
clan_selection = random.choice(clans)

#ARCHERY_SHOOTER VARIABLES
target = [1, 2, 3, 4, 5]
arrows_remaining = 5
p1_arrow_1 = random.choice(target)
p1_arrow_2 = random.choice(target)
p1_arrow_3 = random.choice(target)
p1_arrow_4 = random.choice(target)
p1_arrow_5 = random.choice(target)

p1_score = p1_arrow_1

p2_arrow_1 = random.choice(target)
p2_arrow_2 = random.choice(target)
p2_arrow_3 = random.choice(target)
p2_arrow_4 = random.choice(target)
p2_arrow_5 = random.choice(target)

p2_score = p2_arrow_1

shoot = ""

def stage_2():
    print(f"After a couple of hours riding you glance upwards and notice a large bird hovering in the sky.")
    print("")
    time.sleep(7)

    print("You alert Joichi immediatley and he informs you that the bird is a Golden Eagle and tells you that it has been following you both for some time.")
    print("")
    time.sleep(9)

    print(f"Distracted by the presence of the Eagle Joichi then informs you that {clan_selection} village is straight ahead.")
    print("")
    time.sleep(8)

    print(f"You arrive at the village and are suprised to see an elderly short man stood patiently awating your arrival.")
    print("")
    time.sleep(8)

    print(f"Greeting clansmen, I am the {clan_selection} Khan, I have been expecting you.")
    print("")
    time.sleep(7)

    print("Please follow me to my quarters and we can discuss your purpose here at my village.")
    print("")
    time.sleep(5)

    print("Impressed by the Khans presentiment you acknowlegdge his words and dismount your horse.")
    print("")
    time.sleep(8)

    print(f"Before the {clan_selection} Khan turns to lead you he raises up his right arm and emits a high pitch whistle.")
    print("")
    time.sleep(8)

    print("Puzzled by his actions you study the Khans strange behaviour intently...")
    print("")
    time.sleep(6)
        
    print("Suddenly, a huge Golden Eagle glides down from the sky and with precision and grace it lands directly onto the Khans arm.")
    print("")
    time.sleep(8)

    print(f"Amazed by this action you exchange a smile with the {clan_selection} Khan and proceed to follow him to his quarters.")
    print("")
    time.sleep(8)

    print(f"Once Inside the Khan's quarters you are instructed to make yourself comfortable and are offered some hot tea.")
    print("")
    time.sleep(8)

    print(f"You graciously accept your tea and continue to watch with interest as the Eagle swiftly glides from shoulder to perch.")
    print("")
    time.sleep(8)

    print(f"Now everyone is comfortable you begin to educate the Khan on the matter at hand...")
    print("")
    time.sleep(8)

    print(f"{player_name}, You bring distressing news...")
    print("")
    time.sleep(5)

    print("However, doom will not prevail! I have know Temujin since we were children and I belive his wisdom can guide us to victory...")
    print("")
    time.sleep(8)

    print("I will inform my village of the circumstances and will organise my armies at once. We will join you in battle.")
    print("")
    time.sleep(8)

    print(f"{player_name}, you and Joich can rest here for the night. I will send for you at first light there is a spiritual place we must vist.")
    print("")
    time.sleep(10)

    print("After a long day riding, competing, and negotiating you slip off into a deep slumber...")
    print("")
    time.sleep(8)

    print("...")
    print("")
    time.sleep(4)

    print(f"As the sun begins to illuminate the sky true to his words the {clan_selection} Khan is ready and waiting for you to leave.")
    print("")
    time.sleep(10)

    print(f"Good morning {player_name}, I trust that you have slept well. I have prepared you a camel, we should leave immediatley.")
    print("")
    time.sleep(10)

    print(f"Joichi, I would like to take {player_name} alone. Please stay here and relay your farthers orders to my generals, we wont be long.")
    print("")
    time.sleep(10)

    print("You ride out with the Khan across the plains towards the mountains. The jouney is silent, but the views are spectacular...")
    print("")
    time.sleep(8)

    print("At the mountaions the Khan leads you up a steep dirt path until you reach a flat summit.")
    print("")
    time.sleep(8)

    print(f"The {clan_selection} Khan dismounts his camel and walks over to the precipice.")
    print("")
    time.sleep(8)

    print(f"{player_name}, please join me.")
    print("")
    time.sleep(8)

def archery_shooter():
    global player_name
    global archery_contestant
    global clans_joined
    
    global target
    global arrows_remaining

    global p1_arrow_1
    global p1_arrow_2
    global p1_arrow_3
    global p1_arrow_4
    global p1_arrow_5

    global p2_arrow_1
    global p2_arrow_2
    global p2_arrow_3
    global p2_arrow_4
    global p2_arrow_5

    global p1_score
    global p2_score
    
    global shoot

    print("...................ARROW SHOOTING CONTEST...................")
    print("""@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@#@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@###@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%######@@@@@@@@@@@@@
@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#########&,,,,@@@@@@@@
@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#########,,,,,,@@@@@@@@@
@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%###%%%%%%%%%%%%%########,,,,,##########@@
@@@@@@@%%%%%%%%%%%%%%%%%%%%%%#(((((((((((((((((((((%%%%#####,,,,,/#########@@@@@
@@@@@@%%%%%%%%%%%%%%%%%%%#(((((((((((((((((((((((((((((%##,,,,,##########%%@@@@@
@@@@%%%%%%%%%%%%%%%%%%%((((((((#@@@@@@@@@@@@@@@@@((((((,,,,,/#########%%%%%%&@@@
@@@%%%%%%%%%%%%%%%%%#(((((((@@@@@@@@@@@@@@@@@@@@@@@@@,,,,,((%%%#####%%%%%%%%%%@@
@@%%%%%%%%%%%%%%%%%((((((@@@@@@@#(((((((((((((((&@,,,,,(((((((%%%%%%%%%%%%%%%%%@
@@%%%%%%%%%%%%%%%#(((((#@@@@@%((((((((((((((((((,,,,,@@@@((((((%%%%%%%%%%%%%%%%@
@%%%%%%%%%%%%%%%%(((((@@@@@@(((((((@@@@@@@@@@,,,,,/((@@@@@&(((((%%%%%%%%%%%%%%%%
@%%%%%%%%%%%%%%%(((((%@@@@%((((((@@@@@@@@@@,,,,,((((((@@@@@((((((%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%(((((@@@@@(((((#@@@@@(((,,,,,#@@@((((((@@@@@(((((%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%#(((((@@@@@(((((@@@@@#(/,,,,(&@@@@&(((((@@@@@(((((%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%(((((@@@@@((((((@@@@@#(((((%@@@@@((((((@@@@@(((((%%%%%%%%%%%%%%%
@%%%%%%%%%%%%%%%(((((#@@@@&((((((@@@@@@@@@@@@@@@((((((@@@@@((((((%%%%%%%%%%%%%%%
@%%%%%%%%%%%%%%%%(((((@@@@@@(((((((@@@@@@@@@@&(((((((@@@@@#(((((%%%%%%%%%%%%%%%%
@@%%%%%%%%%%%%%%%%((((((@@@@@@(((((((((((((((((((((@@@@@@((((((%%%%%%%%%%%%%%%%@
@@%%%%%%%%%%%%%%%%%((((((&@@@@@@@(((((((((((((((@@@@@@@#((((((%%%%%%%%%%%%%%%%%@
@@@%%%%%%%%%%%%%%%%%%(((((((@@@@@@@@@@@@@@@@@@@@@@@@@(((((((%%%%%%%%%%%%%%%%%%@@
@@@@%%%%%%%%%%%%%%%%%%%(((((((((@@@@@@@@@@@@@@@@@(((((((((%%%%%%%%%%%%%%%%%%&@@@
@@@@@@%%%%%%%%%%%%%%%%%%%%(((((((((((((((((((((((((((((%%%%%%%%%%%%%%%%%%%%@@@@@
@@@@@@@%%%%%%%%%%%%%%%%%%%*,,,(((((((((((((((((((((,,,#%%%%%%%%%%%%%%%%%%%@@@@@@
@@@@@@@@@%%%%%%%%%%%%%%%%,,,,,%%%%%%%%%%%%%%%%%%%%%,,,,,%%%%%%%%%%%%%%%%@@@@@@@@
@@@@@@@@@@@%%%%%%%%%%%%%,,,,,%%%%%%%%%%%%%%%%%%%%%%%,,,,,%%%%%%%%%%%%&@@@@@@@@@@
@@@@@@@@@@@@@@%%%%%%%%#,,,,(%%%%%%%%%%%%%%%%%%%%%%%%%,,,,,%%%%%%%%%@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@%%%%,,,,,%%%%%%%%%%%%%%%%%%%%%%%%%%%%%,,,,/%%%%@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@,,,,%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%,,,*@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@
""")
   
    print("Contestants will alternate each shooting 5 arrows into a target. After all 10 arrows have been fired the contestant with the higest score will win.")
    print("")
    time.sleep(8)
    print("..........SCOREBOARD..........")
    print("")
    print("Bullseye = 5 points, innercircle = 4 points, middlecircle = 3 points, outercircle = 2 points, perimetercircle = 1 point")
    print("")
    time.sleep(8) 
    while arrows_remaining >= 1:
        
        #ARROW_1 - PLAYER_1
        print("You step up, draw your bow and take aim...")
        shoot = input("Type (z) to shoot arrow:")
        print("")
        time.sleep(2)

        if shoot == "z":
            p1_arrow_1
            print("")
            time.sleep(2)

            if p1_arrow_1 == 5:
                print(p1_arrow_1)
                print("")
                print("Bullseye!")
                print("")
                time.sleep(2)

            elif p1_arrow_1 == 4:
                print(p1_arrow_1)
                print("")
                print("Inner circle, good shot.")
                print("")
                time.sleep(2)

            else:
                p1_arrow_1 <= 3
                print(p1_arrow_1)
                print("")
                print(f"{player_name}, you must do better.")
                print("")
                time.sleep(2)

        elif shoot != "z":
            print("Please type 'z' to release your arrow.")
            print("")
            time.sleep(2)

        #ARROW_1 - PLAYER_2
        print(f"{archery_contestant} steps up with confidence, draws his bow and shoots...")
        p2_arrow_1
        print("")
        time.sleep(2)

        if p2_arrow_1 == 5:
            print(p2_arrow_1)
            print("")
            print("Bullseye!")
            print("")
            time.sleep(2)

        print(f"{player_name} score = {p1_score}")
        print(f"{archery_contestant} score = {p2_score}")
        arrows_remaining -=1
        print(f"Arrows remaining = {arrows_remaining}")
        print("")
        time.sleep(5)

        #ARROW_2 - PLAYER_1
        print("You step up, draw your bow and take aim...")
        shoot = input("Type (z) to shoot arrow:")
        print("")
        time.sleep(2)

        if shoot == "z":
            p1_arrow_2
            print("")
            time.sleep(2)

            if p1_arrow_2 == 5:
                print(p1_arrow_2)
                print("")
                print("Bullseye!")
                print("")
                time.sleep(2)

            elif p1_arrow_2 == 4:
                print(p1_arrow_2)
                print("")
                print("Inner circle, good shot.")
                print("")
                time.sleep(2)

            else:
                p1_arrow_2 <= 3
                print(p1_arrow_2)
                print("")
                print(f"{player_name} you must do better.")
                print("")
                time.sleep(2)

        elif shoot != "z":
            print("Please type 'z' to release your arrow.")
            print("")
            time.sleep(2)

        #ARROW_2 - PLAYER_2
        print(f"{archery_contestant} steps up with confidence, draws his bow and shoots...")
        p2_arrow_2
        print("")
        time.sleep(2)

        if p2_arrow_2 == 5:
            print(p2_arrow_2)
            print("")
            print("Bullseye!")
            print("")
            time.sleep(2)

        p1_score = p1_arrow_1 + p1_arrow_2
        p2_score = p2_arrow_1 + p2_arrow_2
        print(f"{player_name} score = {p1_score}")
        print(f"{archery_contestant} score = {p2_score}")
        arrows_remaining -=1
        print(f"Arrows remaining = {arrows_remaining}")
        print("")
        time.sleep(5)

        #ARROW_3 - PLAYER_1
        print("You step up, draw your bow and take aim...")
        shoot = input("Type (z) to shoot arrow:")
        print("")
        time.sleep(2)

        if shoot == "z":
            p1_arrow_3
            print("")
            time.sleep(2)

            if p1_arrow_3 == 5:
                print(p1_arrow_3)
                print("")
                print("Bullseye!")
                print("")
                time.sleep(2)

            elif p1_arrow_3 == 4:
                print(p1_arrow_3)
                print("")
                print("Inner circle, good shot.")
                print("")
                time.sleep(2)

            else:
                p1_arrow_3 <= 3
                print(p1_arrow_3)
                print("")
                print(f"{player_name}, you must do better.")
                print("")
                time.sleep(2)

        elif shoot != "z":
            print("Please type 'z' to release your arrow.")
            print("")
            time.sleep(2)

        #ARROW_3 - PLAYER_2
        print(f"{archery_contestant} steps up with confidence, draws his bow and shoots...")
        p2_arrow_3
        print("")
        time.sleep(2)

        if p2_arrow_3 == 5:
            print(p2_arrow_3)
            print("")
            print("Bullseye!")
            print("")
            time.sleep(2)

        p1_score = p1_arrow_1 + p1_arrow_2 + p1_arrow_3
        p2_score = p2_arrow_1 + p2_arrow_2 + p2_arrow_3

        print(f"{player_name} score = {p1_score}")
        print(f"{archery_contestant} score = {p2_score}")
        arrows_remaining -=1
        print(f"Arrows remaining = {arrows_remaining}")
        print("")
        time.sleep(5)

        #ARROW_4 - PLAYER_1
        print("You step up, draw your bow and take aim...")
        shoot = input("Type (z) to shoot arrow:")
        print("")
        time.sleep(2)

        if shoot == "z":
            p1_arrow_4
            print("")
            time.sleep(2)

            if p1_arrow_4 == 5:
                print(p1_arrow_4)
                print("")
                print("Bullseye!")
                print("")
                time.sleep(2)

            elif p1_arrow_4 == 4:
                print(p1_arrow_4)
                print("")
                print("Inner circle, good shot.")
                print("")
                time.sleep(2)

            else:
                p1_arrow_4 <= 3
                print(p1_arrow_4)
                print("")
                print(f"{player_name}, you must do better.")
                print("")
                time.sleep(2)

        elif shoot != "z":
            print("Please type 'z' to release your arrow.")
            print("")
            time.sleep(2)

        #ARROW_4 - PLAYER_2
        print(f"{archery_contestant} steps up with confidence, draws his bow and shoots...")
        print("")
        time.sleep(2)
        print("")

        if p2_arrow_4 == 5:
            print(p2_arrow_4)
            print("")
            print("Bullseye!")
            print("")
            time.sleep(2)

        p1_score = p1_arrow_1 + p1_arrow_2 + p1_arrow_3 + p1_arrow_4
        p2_score = p2_arrow_1 + p2_arrow_2 + p2_arrow_3 + p2_arrow_4

        print(f"{player_name} score = {p1_score}")
        print(f"{archery_contestant} score = {p2_score}")
        arrows_remaining -=1
        print(f"Arrows remaining = {arrows_remaining}")
        print("")
        time.sleep(5)

        #ARROW_5 - PLAYER_1
        print("You step up, draw your bow and take aim...")
        shoot = input("Type (z) to shoot arrow:")
        print("")
        time.sleep(2)

        if shoot == "z":
            p1_arrow_5
            print("")
            time.sleep(2)

            if p1_arrow_5 == 5:
                print(p1_arrow_5)
                print("")
                print("Bullseye!")
                print("")
                time.sleep(2)

            elif p1_arrow_5 == 4:
                print(p1_arrow_5)
                print("")
                print("Inner circle, good shot.")
                print("")
                time.sleep(2)

            else:
                p1_arrow_5 <= 3
                print(p1_arrow_5)
                print("")
                print(f"{player_name}, you must do better.")
                print("")
                time.sleep(2)

        elif shoot != "z":
            print("Please type 'z' to release your arrow.")
            print("")
            time.sleep(2)

        #ARROW_5 - PLAYER_2
        print(f"{archery_contestant} steps up with confidence, draws his bow and shoots...")
        print("")
        time.sleep(2)

        if p2_arrow_5 == 5:
            print(p2_arrow_5)
            print("")
            print("Bullseye!")
            print("")
            time.sleep(2)

        p1_score = p1_arrow_1 + p1_arrow_2 + p1_arrow_3 + p1_arrow_4 + p1_arrow_5
        p2_score = p2_arrow_1 + p2_arrow_2 + p2_arrow_3 + p2_arrow_4 + p2_arrow_5

        print(f"{player_name} score = {p1_score}")
        print(f"{archery_contestant} score = {p2_score}")
        arrows_remaining -=1
        print(f"Arrows remaining = {arrows_remaining}")
        print("")
        time.sleep(5)

    if p1_score > p2_score:
        print(f"Congratulations {player_name}, you have demonstrated your skill and have claimed victory.")
        print("")
        time.sleep(5)

        print(f"As promised the {clan_selection} will now join Temujin: our armies will fight as one.")
        print("")
        time.sleep(2)
        clans_joined += 1

    elif p1_score == p2_score:
        print(f"{player_name}, even though the contest has been declared a draw I must say your skill has impressed me.")
        print("")
        time.sleep(7)

        print(f"Because of this I have decided that you are worthy, and that the {clan_selection} will join Temujin in battle: we will prepare at once.")
        print("")
        time.sleep(6)
        clans_joined +=1

    else:
        p1_score < p2_score
        print(f"Unfortunatley, {player_name}, you have lost the contest and have proved yourself unworthy of {clan_selection} alligence. Please leave our village...")
        print("")
        time.sleep(8)
        clans_joined -= 1

def choose_skill():
    global character_selection
    global character

    print(character_selection)
    print("")
    character = int(input("Please choose a number:"))
    print("")
    time.sleep(2)

    if character == 1:

        print(character_selection[0])
        print("")
        print("I had you figured for a warrior may you turn the tide on the battlefield.")
        print("")
        time.sleep(5)

        print(f"{player_name}, this is my son Ogedei, he will show you to the armoury where you can equipt yourself before you begin your quest.")
        print("")
        time.sleep(8)

        print("Please come back to me when you are ready to begin...")
        print("")
        time.sleep(5)
            
    elif character == 2:

        print(character_selection[1])
        print("")
        print("A Scolar!, how fantastic, it will be of great benefit to have a person of study among my ranks.")
        print("")
        time.sleep(5)

        print(f"{player_name}, this is my sister Temulen, she will take you to meet the clan Shaman Tengri, if he likes you he may reveal to you the ways of the Sky God.")
        print("")
        time.sleep(8)

        print("Please come back to me when you are ready to begin...")
        print("")
        time.sleep(5)
            
    else:
        character == 3

        print(character_selection[2])
        print("")
        print(f"I must admit {player_name}, I am disappointed to learn this about you...")
        print("")
        time.sleep(6)

        print("However, I do belive in second chances and the Gods must have brought you to me for a reason.")
        print("")
        time.sleep(6)

        print("Please gather what supplies you can from my village and then come back to me when you are ready to begin.")
        print("")
        time.sleep(6)

def random_choice():
    global clan_selection
    clan_selection = random.choice(clans)

def random_clan_selection():
    global clans
    global clan_selection
    print(".....MAP.....")
    print("")
    print(clans)
    print("")
    random_choice()
    print(f"You study your map and decide to visit the {clan_selection}...")
    clans.remove(clan_selection)
    print("")
    time.sleep(6)

def end_game():
    print("You have failed to unite the clans and were defeted on the battlefied by the foreign invaders.")
    print("")
    time.sleep(8)
    
    print("You have brought dishonour to our people. As a result history will forever forget us.")
    print("")
    restart_game()
    time.sleep(2)

def restart_game():
    name()

def name():
    global player_name
    global player_age
    global character_selection
    global character
    
    while True:
        print("---UNEMPLOYED STUDIOS PRESENTS---")
        print("")
        time.sleep(3)

        print("---------MONGOL QUEST-------")
        print("")
        time.sleep(2)

        print("""@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@% /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    .#@@@@*    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@ &@@@@@@@@@@@@@@@@@@@@  @@@@.@@@@@@@@@@# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@# @@@@@@@@@@@@@@@@@ @%@@@@@(@@@(@@ @.@@,@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@ (, @@@@@@@@@@@@@@ @&@/             @@@# @@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@
@@@@@@@@# @@@* @@@@@@@@@@@    /              /   @@@@@@@@@@@@@@@    @@@@@@@@@@@@
@@@@@@@@@  @@@@@/ @@@@@@@@    &             *.   @@@@@@@@@   @(  @@@@@@@@@@@@@@@
@@@@@@@@@@  @@@@@@@( &@@@@    @   ,@&.#@%   @    &@@@@@@@   &*@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@  @@@@@@@@@# &@    .@..@     @# @#    @@@@@ & %,&@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@& %@@@@@@@# #@     .#%@@@@@@@@,(     @%.      @@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@  @@@@% @@@@ @@@@, @@@@@@@@@ %@#@@@@@@@@. @@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@  ,(@@(@@@@@%*@@ @@@@@@@@@ @(@@@@&@@/@&@ @@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@//@@@@,@@@@@@@@@@@ %@@@@ @@@ @@@@@@&@(@@@% @@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@      /@@@%@@@@%@%@ %@@@@@%@@&&@/*     @@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@     &(        %&@@@(&*#@* ,       @     @@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@,     @                             &/     @@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@     @.                              @     @@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@%%&@@                               @@@%%&@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@       @                               @       @@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@        @                             &#       @@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@        ,@                           @(        @@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@,        @%@                       @@#         @  @@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@        %   *@@/             *@@(   ,/       #@@@@  @@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@.  &@      (#               ,&      &@   @@@@@@@@@@  @@@@@@@@@@
@@@@@@@@@@@@@@@@@& #(       @                 @       .@ ,@@@&            &@@@@@
@@@@@@@@@@@@@@@@@  @       *%                 ,&       @  %@@@@@@@@@@@@@@@@@( @@
@@@@@@@@@@@@@@@@   @       @                   @       @.  @@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@& /@@      *&     *   @   .     /&      (@@ %@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@*              *&@@@@/               @@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@%,&@@@(         ,@#         /&@@@*.@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@*             @@@@@@@              @@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@             #@@@@@@@@             @@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@            *@@@@@@@@@%            &@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@.           @@@@@@@@@@@            @@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@/@@@@@@(   @@@@@@@@@@@   *@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@        &@@@@@@@@@@@@@@@@@@@@@@@@@@
""")

        print("")
        time.sleep(3)

        print("North east Asia, 1200 AD.")
        print("")
        time.sleep(4)

        print("You are lost and have been wondering the Mongolian step for what has seemed like weeks...")
        print("")
        time.sleep(6)

        print("You are tired, hungry, and sore: but above all else you desperately need a drink.")
        print("")
        time.sleep(6)

        print("Whilst trekking across a steep mountain incline you notice a structure through the trees: it looks like a tent.")
        print("")
        time.sleep(8)

        print("Elevated, you then begin to see smoke and smell food. This must be the mountain village that you have heard about.")
        print("")
        time.sleep(8)

        print("You enter into the village discreetly and immediately see a market.")
        print("")
        time.sleep(6)

        print("As you approach the market the people who notice you stop their trading and stare.")
        print("")
        time.sleep(7)

        print("A woman, shocked by your desperation, approaches you holding a water hide...")
        print("")
        time.sleep(6)

        print("'Would you like a drink' the kind woman asks.")
        print("")
        time.sleep(6)

        print("Gulp... Gulp... Gulp...")
        print("")
        time.sleep(6)

        print("After taking a long drink from the hide your thirst is quenched. Finally, you now begin to feel a little better.")
        print("")
        time.sleep(9)

        print("You hand the woman back her water hide and express your gratitude for her kindness.")
        print("")
        time.sleep(7)

        print("Then, before another word is spoken you feel a powerful presence approaching...")
        print("")
        time.sleep(7)

        print("Carefully, you turn around and notice a calm, modestly dressed man walking towards you. Still vulnerable from your journey you brace yourself for confrontation.")
        print("")
        time.sleep(10)

        #PLAYER MEETS TEMUJIN
        print("Greetings clansman, My name is Temujin. I am the Burkan Mountain Village Cheiftain, I haven't seen you around here before...")
        print("")
        time.sleep(8)

        player_name = (input("What is your name:"))
        print("")
        time.sleep(2)

        player_age = int(input(f"Hello {player_name}, please enter your age:"))
        print("")
        time.sleep(2)
        
        if player_age >= 21:
            pass

        else:
            player_age < 21
            print("")
            time.sleep(2)
            print(f"Sorry {player_name}... You are to young to undertake this quest. Please return when you are of age.")
            print("")
            time.sleep(3)
            restart_game()
        
        print(f"Unfortunatly {player_name} you have arrived during dangerous times. With each passing day our clans are being pillaged and plundered by foreign invaders.")
        print("")
        time.sleep(10)

        print("They seek to destroy our peaceful way of life, and are killing our people to claim these ancestral lands for themselves.")
        print("")
        time.sleep(8)
        
        play_game = input(f"I see that you have fire in your eyes {player_name}, and you appear to be very stong. Will you consider joining our cause and help my clan to defeat the invaders (Y/N)?")
        print("")
        time.sleep(10)

        if play_game.upper().lower().strip() == ("yes") or play_game.upper().lower().strip() == ("y"):
            pass
                    
        else:
            play_game.upper().lower().strip() == ("no") or play_game.upper().lower().strip() == ("n")
            restart_game()
        
        print(f"You are very brave {player_name}, quickly! Follow me to my quarters we need to get you fed and healthy: there is no time to loose...")
        print("")
        time.sleep(9)

        print("After a short break and a wholesome meal your strength returns...")
        print("")
        time.sleep(8)

        print(f"{player_name}, now that you are healed please tell me what skill best describes you.")
        print("")
        time.sleep(6)

        choose_skill()

        print("After spending some time in the village you decide its time to return to Temujin.")
        print("")
        time.sleep(8)

        print(f"{player_name}, where have you been... Come quickly!... A rider from the next village has brought word...")
        print("")
        time.sleep(8)

        print("Cheiftain!...")
        print("")
        time.sleep(3)

        print("Invaders have attacked my village... They have killed and enslaved my people... No one was spared... I ran... I feel ashamed... I admit, I am weak...")
        print("")
        time.sleep(10)

        print("There were too many of them... We could not win... Our only chance of survival is to unite the rival clans.")
        print("")
        time.sleep(9)

        print("Cheif Temujin: I agree with you clansman, I will send a detachment of soldiers to your village immediately. I am very sorry for your loss.")
        print("")
        time.sleep(10)

        print("Please come inside and we can help you overcome your greif.")
        print("")
        time.sleep(6)

        print(f"{player_name}, this is my youngest son Joichi. He will accompany you on your quest and will act as your guide/advisor.")
        print("")
        time.sleep(9)

        print("We have loaded your horses up with supplies. You should go now...")
        print("")
        time.sleep(6)

        print(f"{player_name}, take this map. Ride out and visit the five clans. You must tell the elders of our struggle.")
        print("")
        time.sleep(8)

        print("Tell them our survival hangs in the balance.")
        print("")
        time.sleep(6)

        #CLAN VISIT NUMBER 1
        random_clan_selection()

        print(f"After riding for several long hours Joichi informs you that you are now about to arrive at the {clan_selection} Village.")
        print("")
        time.sleep(9)

        print("Upon arrival you dismount your horse and are now on foot.")
        print("")
        time.sleep(4)

        print("At the village entrance you inform the guard of your urgent quest and are immediatly escorted to the 'Khan' residence.")
        print("")
        time.sleep(8)

        print(f"Taking a moment to compose yourself you then enter into the {clan_selection} Khans humble quarters.")
        print("")
        time.sleep(8)

        print("Once inside you are greeted by a large man equipt with a thick beard, and a long, immaculate moustache.")
        print("")
        time.sleep(8)

        print(f"Hello, and welcome to my village {player_name}, I am the {clan_selection} Khan.")
        print("")
        time.sleep(7)

        print("Can you explain this emergency or 'quest' that I have been informed about.")
        print("")
        time.sleep(7)

        print("With Joichi's help you tell the Khan all that has happened and then you explain to him Temujin's proposal.")
        print("")
        time.sleep(8)

        print("Shocked and horrified from recieving the news the Khan is silent...")
        print("")
        time.sleep(7)

        print("...")
        print("")
        time.sleep(7)

        print(f"Forgive my delayed response {player_name}. Its just... I thought the war was over...")
        print("")
        time.sleep(8)

        print(f"Guard! send for {archery_contestant} immediatley... Clansmen, excuse my behaviour, I must take council for this meeting.")
        print("")
        time.sleep(9)

        print("Within moments the tent entrance is flung wide open and a thin obscure looking man enteres into the scence.")
        print("")
        time.sleep(9)

        print(f"{archery_contestant}:'Farther, Farther what is the meaning of this, you know I hate to be disturbed'.")
        print("")
        time.sleep(8)

        print(f"Clansmen, allow me to introduce my eldest son and cheif counsellor {archery_contestant}.")
        print("")
        time.sleep(7)

        print(f"{archery_contestant}:'Yes, yes. As you were'.")
        print("")
        time.sleep(5)

        print(f"{player_name}, I am now going to breif {archery_contestant}, please enjoy a drink while we retire.")
        print("")
        time.sleep(10)

        print(f"Some time later the {clan_selection} Khan appears and is ready to speak...")
        print("")
        time.sleep(7)

        print(f"{player_name}, I have decided that you will need to prove your skill before the {clan_selection} will join Temujin's call.")
        print("")
        time.sleep(9)

        print(f"If you can beat {archery_contestant} in an arrow shooting contest the {clan_selection} Army will be Temujin's to command.")
        print("")
        time.sleep(10)

        print("However, if you lose the contest we will consider you to be unworthy and will take our chances fighting alone.")
        print("")
        time.sleep(9)
        
        archery_shooter()
        print("")
        time.sleep(4)

        print(f"With no time to waste you thank the {clan_selection} Khan for his time, mount your horse and prepare to visit another clan before nightfall.")
        print("")
        time.sleep(10)

        #CLAN VISIT NUMBER 2
        random_clan_selection()

        stage_2()
       

name()
restart_game()
