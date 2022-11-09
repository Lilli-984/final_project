import re



dates = {"start":{"month":10,"year":2017},"proposal":{"month":0,"year":0}}

def addTime(time):
    this_time = time.lower()
    timeRegex = re.compile(r'[0-9]+ month(s)?')
    isTime = timeRegex.search(this_time)
    while not isTime:
        print("\nThats not a valid input. Please enter an integer followed by \"months\" or \"years\". Examples: \'18 months\' , \'2 years\':")
        this_time = input()
        isTime = timeRegex.search(this_time)
    num, sect = this_time.split()
    num = int(num)
    is_months = False
    monthRegex = re.compile(r'month(s)?', re.I)
    yearRegex = re.compile(r'year(s)?',re.I)
    ismonth = monthRegex.search(sect)
    isyear = yearRegex.search(sect)
    if ismonth:
        dates["proposal"]["month"] = addMonths(time, dates["start"]["month"])
        is_months = True
    elif isyear:
        dates["proposal"]["year"] = dates["start"]["year"]+num
    return is_months












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

""" print("What's your characters name?")
name = str(input())
characters["main"]= name.lower()
is_name("main",name)
 """

def is_choice(choose):
    is_alpha= False
    choose = choose.upper()
    match choose:
        case 'A'|'B'|'C'|'D':
            is_alpha = True
        case _:
            while not is_alpha :
        #print(is_alpha)
                print("Thats not a choice. Please choose A, B, C, or D.")
                choose = input().upper()
                match choose:
                    case 'A'|'B'|'C'|'D':
                        is_alpha = True
    # choice_regex = re.compile(r'(A|B|C|D)')
    # is_alpha = choice_regex.search(choose)
    
        #is_alpha = choice_regex.search(choose)
    return choose

    # choice = False
    # if choose == "A" or  "B" or "C" or "D":
    #     choice = True
    # while choice == False:
    #     print("Thats not a choice. Please choose A, B, C, or D.")
    #     choose = input().upper()      


# print("choice: ")
# choose = input()
# print(is_choice(choose))

def ch1():
    print('ch1')
    print("keep going?")
    keepgoing = input()
    if keepgoing == "yes":
        print("ch1 stuff")
        print("keep going?")
        thischoice = input()
        if thischoice == "no":
            return




def game():
    print("choose")
    choose = input().upper()
    is_choice(choose)
    a = "not end"
    if a != "end":
        print("play game")
        ch1()
        print("choose")
        choose = input().upper()
        is_choice(choose)
        print("a little more ")
    elif a == "end":
        print ("end game")
        return
    print("more game")

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

# time = 9
# start = 10
# addMonths(time, start)
# newtime = addMonths(time, start)
# print(newtime)

dates = {"start":{"month":10,"year":2017},"proposal":{"month":0,"year":0}}
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
def this():
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

this()