import re


characters = {"main": "", "insterest": ""}

def is_name(char, name):

    name_regex = re.compile(r'^[A-Za-z]+$')
    is_alpha = name_regex.search(name)
    while not is_alpha :
        print(is_alpha)
        print("Thats not a name, silly. Try again: ")
        name = input()
        is_alpha = name_regex.search(name)
    characters[char]= name.lower()


def is_choice(choose):
    choice_regex = re.compile(r'(A|B|C|D)')
    is_alpha = choice_regex.search(choose)
    while not is_alpha :
        print(is_alpha)
        print("Thats not a choice. Please choose A, B, C, or D.")
        choose = input().upper()
        is_alpha = choice_regex.search(choose)
    return choose
  
startyear= 2017
startmonth = 10
def addMonths(time,start):
    time = time%12
    left = time
    for i in range(time):
        while start <=12:
            start += 1
            left -=1
    start = 1
    start+=left
    return start


dates = {"start":{"month":10,"year":2017},"proposal":{"month":0,"year":0}}

print("Welcome to LIFE : DERAILED")
print("You're goal is to live a happy life with the person you love. :)\n")
print("\nWhat's your characters name?")
name = str(input())
characters["main"]= name.lower()
is_name("main",name)


print("Whats their love interests name?")
name = str(input())
characters["interest"] = name.lower()
is_name("interest",name)

def next_chapter(chap):
    print("\n----------------------")
    print(f'       CHAPTER {chap}')
    print("----------------------\n")


def game():
    next_chapter(1)
    meet_place = {
        "A": "At the Library", 
        "B": "At a cafe", 
        "C": "At a campus event",
        "D":"On a dating app"
        }
    print("In the interest of meeting new people,",characters["main"],
        "decides to get out into the world. How do they meet their future partner?")

    print("A: At the Library\n"+"B: At a cafe\n"+"C: At a campus event\n"+"D: On a dating app")
    place_choice = input().upper()
    place_choice = is_choice(place_choice)
    here = meet_place[place_choice.upper()]
    print("\nYou chose: "+ here)

    if place_choice == "A":
        print("\nYou go to the library, and hang out a couple days in a row.\n"
        "When you eventually find someone you're interested in, you try to bump into them more often.\n"
        "After a bit of social media stalking, you realize",characters["interest"],"is a dangerously beautiful soul.\n")
        "......You can't help but be mezmerized by their energy. "
            
    elif place_choice == "B":
        print("\nYou begin to go study at your favorite cafe. Eventually, you stop constantly people watching, " 
        "it's not like you'll suddenly gain the courage to ask a stranger for their number... ")
        print("But you keep going back. At least you are always greeted with "+characters["interest"]+"'s sweet smile. After a couple of times of fun banter,",
         characters["interest"],"invited you for coffee, but without the coffee and cream splashed apron.")

    elif place_choice == "D":
        print("\nYou decide to follow the masses. But you become a victim to the lonliness of hookup culture."
         "You're left emotionally burnt out and just delete every dating app on your phone.\n"
            "Maybe you can try again after college?")
        return
    elif place_choice == "C":
        print("\nYou try to get more involved on campus: Going to more events and starting to recognize more people!\n")
        print("Some time passes, but you still haven't gotten close to anyone you're attracted to.\n ")
        print("You decide to give up on romance in college, and work on enjoying your own company first.\n")
        print("Maybe you can try to find what you want again after finding who you want to be. ")
        print("\nL o v e   Y o u r s e l f <3")
        return

    print("\nHanging around",characters["interest"]+" makes you're days feel fuller, keeps your mind occupied, and makes time go by fast!\n")
    print("\n.....enter any character to continue:....")
    any = input()

    print("\nYou've already gone on a couple dates here and there, and things are starting to get serious!")
    print("You've been filled to the brim with feelings, and you just HAVE to let them know...\n")
    print("\n.....enter any character to continue:....")
    any = input()

    print("\nIts been two weeks since you met",characters["interest"]+". You can't help but to be infatuated. You've been waiting for this moment. Do you tell "+
    characters["interest"], "that you love them? (yes or no) ")

    confess = input()

    yesRegex = re.compile(r'y|yes', re.I)
    noRegex = re.compile(r'n|no', re.I)
    while not (re.search(yesRegex, confess) or re.search(noRegex, confess)):
        print("Thats not a valid input. Please enter yes or no.")
        confess = input()
    if re.search(yesRegex, confess):
        print(f'{characters["interest"]}: "You love me?" \n{characters["main"]}:"I do" \n')
        print(f'{characters["interest"]}: "No, you don\'t. You\'re just in love with how I made you feel."\n \n " Just go home."')
        print(f'\n Great. Now look what you did. ~ {characters["main"]} the Romantic ~  '
         '\nYou\'ve managed to scare them off before even figuring out what kind of love they are willing to accept. You don\'t know anything.')
        print("Learn your lesson and try again. ")
        return
    elif re.search(noRegex, confess):
        print("\nGood point. \nAt this point, dropping that weight on the relationship might only turn out to be a burden. "
        "\nProve that its real, and watch your feelings continue to grow. Your confession can wait. ") 

    next_chapter(2)

    print(f'{characters["main"]} and {characters["interest"]} are official college grads. There have been talks of children, moving in together, and ...marraige')
    print("You never thought the time would come when you would be so certain about how you wanted to spend the rest of your life. ")
    print("And now you can't wait to tell the world of your discovery. You want to propose before you move in together. \nHow long would you have been dating before the engagement?")
    print("Please enter \'_ months\' or \'_ years\'")
    time, sect = input().split()
    time = int(time)
    monthRegex = re.compile(r'month(s)?', re.I)
    yearRegex = re.compile(r'year(s)?',re.I)
    ismonth = re.search(monthRegex, sect)
    isyear = re.search(yearRegex, sect)
    while not (ismonth or isyear):
        print("\nThats not a valid input. Please enter \'_ months\' or \'_ years\':")
        time, sect = input.split()
        time = int(time)
    if re.search(monthRegex, sect):
        if time < 12:
            print("\nHave you learned nothing?? Why do you feel the need to rush so much?? I mean, less than a year?? \nJust start over . ")
            return
        newmonth=addMonths(time, startmonth)
        dates["proposal"]["month"]= newmonth
    elif re.search(yearRegex, sect):
        newyear= startyear+time
        dates["proposal"]["year"]= newyear

    print("\nCongratulations! I hope you and your fiance are very happy together! Remember to prioritize those you love.")

    next_chapter(3)

    print("You're really doing amazing! I hope there is much happiness and love in your marraige and family. \n")
    print("\nWhat's that? You're focusing on your career right now? I love that for you!\n")
    print(f'{characters["interest"]} has grown a bit restless. It feels like {characters["main"]} is always at work,'
     'the bright spark of their initial honeymoon love is fizzling. What could be going wrong?') 
    print("\n.....enter any character to continue:....")
    any = input()
    print(f'\n{characters["main"]} has become very career driven, with the support of their partner, they\'re more confident than ever.')
    print("\nOthers must notice too, since "+characters["main"]+"'s coworkers always make sure to invite their favorite work buddy to after-work drinks!")
    print("One of your coworkers, Sam, invited you to drinks tonight! But it seems no one has been talking about it. Is it just going to be you two?")
    print("\n.....enter any character to continue:....")
    any = input()
    print("Feeling the mix of after-work exhaustion, and the couple of drinks already in your system, you and sam decide to call it a night.")
    print("After splitting the check and wrapping up the final laughs of the night, you feel relaxed and replenished.")
    print("There's something familiar about this feeling. Walking next to Sam in the cool, dark night makes you forget about the pressures of a proffessional career.")
    print("Reminds you of the freedom of college life. ")
    print("Lost in thought, you don't realize you've already arrived at Sam's apartment.")
    print("Sam thanks you for walking them home and invites you in from some more drinks!")
    print("Sam: 'No reason to end the night now! Wanna come in?' \n(yes or no)")
    cheat = input()
    while not (re.search(yesRegex, cheat) or re.search(noRegex, cheat)):
        print("Thats not a valid input. Please enter yes or no.")
        cheat = input()
    if re.search(yesRegex, cheat):
        print(" Damn, just like that?? You lose, obviously.")
        return
    elif re.search(noRegex, cheat):
        print("\nSam:  \'Oh, are you sure? It might be dangerous for you to go home like this. You can just go home tomorrow. You don\'t want to?\' \n (yes or no)")
        cheat = input()
        if re.search(yesRegex, cheat):
            print("\nAw man, you were so close to doing the right thing. They really didn't even have to work that hard to convince you. ")
            print("\nYou leave ",characters["interest"], "waiting for you at home. Eager to rekindle the spark you just finished putting out. \nYou lose.")
            return
        print("\nSam: Alright. Have a goodnight :)")

    print("\nYou go home to your wonderfully supportive and loving partner. But "+characters["interest"],"is confused as to why you went out today, "
    "its not the usual day you drink with all your coworkers. \nDo you choose to tell her the truth about who you went out with? \n(yes or no)")
    communicate = input()
    while not (re.search(yesRegex, communicate) or re.search(noRegex, communicate)):
        print("Thats not a valid input. Please enter yes or no.")
        communicate = input()
    if re.search(yesRegex, communicate):
        print("\n You decided to tell "+characters["interest"]+" the truth. Theres a hint of betrayal that flashes across their face, but it fades into a dark, thoughtful expression.")
        print("The next couple hours are spent by the two of you playing emotional-catch-up." 
        "You realize you shouldn't have even accepted your coworkers invitation when you found out it was just for you, and you promise to be more considerate. ")
        print("You both realize you've been a bit disconnected lately, but the rest of the night only strengthens and confirms the love you started from. ")
        print("\nCommunication can be powerful.")
        print("\n.....enter any character to continue:....")
        any = input()
        end = "one"
    elif re.search(noRegex, cheat):
        print("You decide not to mention you one on one drinks, and say that it was a spontaneous decision. ")
        print(characters["interest"]+" doesn't seem fully satisfied, but they don't push for more. ")
        print("\n.....enter any character to continue:....")
        any = input()
        end = "two"
        
    next_chapter(4)

    if end == "one":
        print(f'The beautiful couple, {characters["main"]} and {characters["interest"]} are the community\'s favorite family.')
        print("\nFull of love and life, you both continue to live the rest of your lives together. \nNo one knows you better than",characters["interest"]," does, "
        "and there's nothing you wouldn't do for their happiness.\n You did it. \n  You found happiness together.")
    elif end == "two":
        print("Life is bright, and your future seems so certain. Nothing could ever come between your love for "+characters["interest"])
        print("You get to come home to a loving spouse, who looks at you with all the love anyone could ever need. \n")
        print("Until one day that love feels cold. \n Trying to convince yourself you're imagining it, you ask about it, needing to make sure.")
        print("\n.....enter any character to continue:....")
        any = input()
        print(f'{characters["interest"]} confesses they found out about that night with Sam. You don\'t need to know how she found out,'
        'just that she knows you lied to her. Why would you lie if there wasn\'t anything deeper going on?? ')
        print("\n.....enter any character to continue:....")
        any = input()
        print("A lot of work gets put into your marriage to make sure ",characters["interest"],"feels good about putting their trust in you again.")
        print("But you can't help but miss the blinding comfort of all the trust and love that disappeared when you chose to lie.")
        print("It's not lost forever. But it will take more than a night and a couple of drinks to heal.")
        print("Continue to show your love for what matters to you. No one can read your mind. Only your actions are percieved.")
        print("You found love. Now value it. ")

    print("\nE N D  O F  L I F E\n ")

    print("\nThank you for playing!")
    
game()

