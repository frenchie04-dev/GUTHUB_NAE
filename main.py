def show_loading_screen():
    term_name = "{frenchie04-dev NAE}"
    print(Fore.GREEN + Style.BRIGHT +
          f"Welcome [ {Fore.MAGENTA}{USER}{Fore.GREEN} ] to {term_name}")
    width = 40
    total = 100
    interval = total / width
    for i in range(width + 1):
        progress = int(i * interval)
        bar = '█' * i
        stars = '=' * (width - i)
        loading_text = f"[{bar}{stars}] {progress}%"
        print(Fore.CYAN + loading_text, end='\r')
        time.sleep(0.1)
    print(Style.RESET_ALL)

import os, time
from colorama import Fore as col
from time import sleep
from playsound import playsound
from discord.ext import tasks

@tasks.loop(minutes=2, seconds=40)
def track_loop():
  playsound("okmusi-mac.mp3")

def clear():
  os.system("clear")

class Player():
  moral = 100
  health = 100

  class StatsManager():
    @classmethod
    def get_stat(self, stat: str = "health"):
      if stat == "health":
        return Player.health
      elif stat == "moral":
        return Player.moral
          
  @classmethod
  def update_stat(self, stat: str, edit_by: int):
      if stat == "health":
        Player.health += edit_by
      elif stat == "moral":
        Player.moral += edit_by

  @classmethod
  def damage_player(difficulty: int, atk):
      if difficulty == 1:
        Player.StatsManager.update_stat("health", atk*5)
      elif difficulty == 2:
        Player.StatsManager.update_stat("health", (atk*4))
      elif difficulty == 3:
        Player.StatsManager.update_stat("health", (atk*3))
      elif difficulty == 8:
        Player.StatsManager.update_stat("health", (atk*2))
      elif difficulty == 9:
        Player.StatsManager.update_stat("health", (atk))



health = 100000
moral = 100      
print("your health is now", Player.StatsManager.get_stat("health"))
print (" your moral is now", Player.StatsManager.get_stat("moral"))

if Player.satsmanager.get_stat("health") <1:
  print(col.RED + "I am affraid you have died to restarty just click the stop button in the middle of the screen and then the green run button. thank you for playing!")
exit()
if Player.statsmanager.get_stat("moral") < 1:
   print(col.RED + "I am affraid you have died to restarty just click the stop button in the middle of the screen and then the green run button. thank you for playing!")
exit()

White = "\033[0;37m"  
Orange = "\033[0;33m"

username = input("What would you like your username to be? Please avoid capital letters: ").lower()
print("Your username is" ,username)

  #make text orange

def loading(username):
  for i in range(4):
    print(f"{col.orange}Hello, {username}! Please wait while the game finishes loading.")
    print("Loading   |")
    time.sleep(0.60)
    clear()
    print(f"{col.orange}Hello, {username}! Please wait while the game finishes loading.")
    print("Loading   /")
    time.sleep(0.60)
    clear()
    print(f"{col.orange}Hello, {username}! Please wait while the game finishes loading.")
    print("Loading   -")
    time.sleep(0.60)
    clear()
    print(f"{col.orange}Hello, {username}! Please wait while the game finishes loading.")
    print("Loading   \\")
    time.sleep(0.60)
    clear()

loading(username)

clear()

# make text white

print({col.white}, "Hello", username, "! Welcome to the game!," ,{col.white})
print("Welcome to my text-based adventure game.")
print("You're the last human left after John Connor was unable to stop Judgment Day! you are now being hunted by an efficant killing machine se world from jugment day")
difficulty = input("""
Please select your difficulty:
1. Too easy
2. Not so easy
3. Mid difficulty
8. Mildly difficult
9. VERY DIFFICULT!
""")

if difficulty == '1':
  print("Okay then, you have chosen the most difficult difficulty.")
elif difficulty == '2':
  print("You have chosen the penultimate level of difficulty.")
elif difficulty == '3':
  print("You have chosen the semi-safe option, but in truth, there is no safe option.")
elif difficulty == '8':
  print("The easy one!")
elif difficulty == '9':
  print("I'm sorry you fancied a challenge but that's not how this game works.")


sleep(2)
clear()

start = input("Would you like to start the game? (y/n)")
if start.lower() == "yes" or start.lower() == "y":
  print("Okay, no worries. Game beginning!")
else:
  print("Interesting.")
print("your health is",health)
spawn = input("""
Where would you like to spawn? Choose a location:
1. Airport
2. Some random kid's house
3. Hospital
4. The end of the game\n""")

if spawn[0] == "1" or spawn.lower() == "airport":
  print("Okay, you are at this deactivated airport. There are many planes surrounding you!")
  time.sleep(2)
elif spawn == "2" or spawn.lower() == "some random kid's house":
  print("You wake up after what felt like the best night's sleep you have ever had. You realize that it's not your bed and you can tell by the fact that it has a hammock opposite it and is full of soft toys.")
  time.sleep(2)
elif spawn == "3" or spawn.lower() == "hospital":
  print("You spawn in a hospital waste room. You make your way out miraculously with a few mere scratches - missing limbs. ?")
  time.sleep(5)
elif spawn == "4" or spawn.lower() == "the end of the game":
  print("yeah not gonna work")  
  Player.StatsManager.damage_player("health", -90)
time.sleep(2)
print("your health is now", Player.StatsManager.get_stat("health"))
clear()
time.sleep(2)
print("you see a bright light you have been blinded for a few seconds ")
time.sleep(2)
clear()
time.sleep(2)

print("you see a strange humonoide shape kneeling down")
choice_1 = input("""
1.) do you go and greet them 
2.) do you search arround and look for a weapon 
3.) do you try and run away\n""")

if choice_1 == "1":
  print("you go up to meet them, im affraid it doesnt end well")
  Player.StatsManager.damage_player("health", -10)
  print(Player.StatsManager.get_stat("health"))
  time.sleep(2)
elif choice_1 == "2":
  print("the only weapon you find is a bent rusty shovel")
  attack = input("do you go and hit them with the ruty bent shovel? y/n")
  if attack == "y":
    print("i mean what did you exspect that you where going to own them with a shovel, no it crumbles as soon as you hit him ill stop there it didnt end well")
    time.sleep(2)
    clear()
    Player.StatsManager.damage_player("health", -15)
    print(Player.StatsManager.get_stat("health"))
  else:
      print("good option")
elif choice_1 == "3":
  print("you escape safely well done")
time.sleep(2)
clear()

backstory_2 = ("you have managed to escape your first encounter with THE TERMINATOR congratulations but im afraid he has broken into a strangers house and stolen there phone book and is finding out where you live")
print(backstory_2)

time.sleep(2)
clear()

choice_2 = input("""
what do you want to do ?
1.) try your luck and see if THE TERMINATOR will actualy go to your house
2.) set a trap for him 
3.)take him on in a 1v1\n""")

if choice_2 == 1:
  print("yeah once again it doesnt end well for you i shal save you the time")
  Player.StatsManager.damage_player("health", -10)
  print(Player.StatsManager.get_stat("health"))  
  clear()
  time.sleep(2)
elif choice_2 == 2: 
  print("well done", username, "you have chosen the correct option")
  time.sleep(2)
  clear()
elif choice_2 == 3:
  print("still doesnt end well I will finnish there for your sanity")
Player.StatsManager.damage_player("health", -15)
print(Player.StatsManager.get_stat("health"))  
clear()
clear()

trap = input("""
what kind of trap do you want to set up?
1.) exsplode the living day lights out of him
2.) make him fall into a hole 
3.) make him fall into some molten metal""")

if trap == 1:
  print(
   "well done you removed an arm and then he throws the arm at you pentrating your skull")

  Player.StatsManager.damage_player("health", -10)
  print(Player.StatsManager.get_stat("health"))  

  clear()

elif trap == 2:
  print("he just jumps out of the hole as it was not deep enought you die")
  Player.StatsManager.damage_player("health", -18)
  print(Player.StatsManager.get_stat("health"))
  clear()
elif trap == 3:
  print("well done you survived level one")
clear()

print("time for level 2")
lvl2_backstory = ("they people form the futer have sent down a nother terminator but this time it is more advansed and upgraded.")
print(lvl2_backstory)
print ("your current health is", health )
start = input("Would you like to start level 2? (y/n)")
if start[0].lower() == "y": 
  print("Okay, no worries. Game beginning!")
else:
  print("Interesting.")
clear()

#make text orange again 

def loading(username):
  for i in range(4):
    print(f"{col.LIGHTYELLOW_EX}Hello, {username}! Please wait while the game finishes loading.")
    print("Loading   |")
    time.sleep(0.60)
    clear()
    print(f"{col.LIGHTYELLOW_EX}Hello, {username}! Please wait while the game finishes loading.")
    print("Loading   /")
    time.sleep(0.60)
    clear()
    print(f"{col.LIGHTYELLOW_EX}Hello, {username}! Please wait while the game finishes loading.")
    print("Loading   -")
    time.sleep(0.60)
    clear()
    print(f"{col.LIGHTYELLOW_EX}Hello, {username}! Please wait while the game finishes loading.")
    print("Loading   \\")
    time.sleep(0.60)
    clear()

loading(username)

# you have loading defined and run twice?!

#make text white again 

lvl2_choice = input("""
what would ytou like to do ?
1.) go hunting for the new veriant of the terminators
2.) wait for the terminator to find you
3.) run as far as you can
""")
if lvl2_choice == 1:
  print("yeah, you find him and you get sent back home to mum in a jam jar")
  Player.StatsManager.damage_player("health", -25.5)
  print(Player.StatsManager.get_stat("health"))
  clear()
elif lvl2_choice == 2:
  print("yeah still not gonna end well")
  Player.StatsManager.damage_player("health", -20)
  print(Player.StatsManager.get_stat("health"))
  clear()
elif lvl2_choice == 3:
  print("welldone",username,"you go to your secret hideout.")
  Player.StatsManager.update_stat("health", +5)
  print(Player.StatsManager.get_stat("health"))
print("you have made it to your secret hide out you meet up with a few peopple who agree to help you")
clear()

ybot = input("""
what would you like to do now as you are safe for a short period of time petanshaly
would you like to :
1.) band togeather and try to make a plan to take down the terminator 
2.) stay there and hope for the best
3.) check your supplies
""")
if ybot == 1:
  print("welldone",username,"you have chosen the best option")
elif ybot == 2:
  print("yeah not the best option as he finds you and ends you and your team")
  Player.StatsManager.damage_player("health", -26)
  print(Player.StatsManager.get_stat("health"))
  clear()
elif ybot == 3:
  print("your supplies are full and perfect!")
clear()
print("""
you have gathered a team who all want the same as you and you gather your suplies and make for the chopper
""")
clear()
erm = input("""you have gatherd your supplies and headed to previouse terminator strikes to see what kind of machine you are up against what would you like to do ?
1.) record all the data and then plan an attack from this information 
2.) record the information and try and intercept his next attack
3.) record how he attcks and try and find his weaknesess 
""")
if erm == "1":
  print("good choice",username,)
elif erm == "2":
  print("yeah thats not gonna work he interceps your attack on his attack")
  Player.StatsManager.damage_player("health", -15)
  print(Player.StatsManager.get_stat("health"))
elif erm == "3":
  print("yeah you find no weakneses")
Player.statsmanager.update_stats("moral", - 10)
print(Player.statsmanager.get_stat("moral"))
clear()

next_32 = input("""so you have recorded some information on the new generation of terminator you find that he is in a arcade what would you like to do ?
1.) bring the old genration of terminator who has been sent back in time to protect you
2.) go there and confrount him try and take him on a 1V1
3.) kiss your arse goodbye !

""")
if next_32 == "1":
  print("im affraid tht you find he is a polymorphic one ")

  Player.statsmanager.update_stats("moral", - 23)
  print(Player.statsmanager.get_stat("moral"))

elif next_32 == "2":
  print("yh you might as well kiss your arse goodbye at this point there no coming back!")
  Player.StatsManager.damage_player("health", -26)
  print(Player.statsmanager.get_stat("moral"))
elif next_32 == "3":
  print("I like your thinking you may survive this round ")
  Player.StatsManager.update_stat("health", + 26)
print(Player.StatsManager.get_stat("health"))
clear()
tbyo = input("""
so you have found out that the new veriant is polymorthic and your terminator is not as efficant as the new one you see the t-800 terminator get uppercutted half way accros the parcking lot by the t-1000 what would ypu like to do ?
1.) use the shotgun to try and take it down 
2.) hop back into the truck that you got here in and drive away 
""")
if tbyo == "1":
  print(" you first shoot it in the sholder and allthought you hit and you are able to see staright through the t-1000 remorfs its self to be complete ")
  Player.statsmanager.update_stats("moral", - 32)
  print(Player.statsmanager.get_stat("moral"))

else: 
  print(" you drive away but you see the t-1000 runnig after you")
print("you run and hide in an storm drain the t-1000 after being chased by the police he crashes his cop bike into the helicopter as he is impersinating a cop")
#define player
Player.statmanager.update_stats("moral", - 12 - 54)
print(Player.statmanager.get_stat("moral"))
clear ()
sleep(10)
print("HAND OVER OF TEACHERS MAY BE DIRECTLY LINKED TO DETERIATION OF WORK")
sleep(20)
print("if you are still hear good on ya it may get worse fyi ")
Player.StatsManager.update_stat("health", +0.3)
print(Player.StatsManager.get_stat("health"))
clear()
feedback = input("""
the T-1000 is now chasing you in a stolen helicopter would you like to 
1.) try and drive away
2.) lose him by chucking a few uie's
3.) other
""")
if feedback == "1":
  print("you satrt to drive away but you find thata the T-1000 is right on your tail")
  Player.statmanager.update_stats("moral", -36)
  print(Player.statmanager.get_stat("moral"))
elif feedback == "2":
  print("you chuck a few uie's you magange to lose him but for how long")
Player.statmanager.update_stats("moral", +12)
print(Player.statmanager.get_stat("moral"))

clear()
sleep(10)
print("you have managed to shake the T-1000 off of your tail tempararaley, you do not have enought fule to go you will hav e to make a vital decigion that will determin you survival.")
sleep(10)
clear()

fule_crisis = input("""
You do not have enogut fule to last ypou the journey ahead of you. You can either:
1.) hijack another vechile 
2.) get some petrol 
""")
if fule_crisis == "1":
  print("well done you have hijack a different veichle yuou have checked it over and chosen this one precisedly for its blending in ability, but you feel a little guilty about stealing the veichle evenought its a life or death situation so you leave you veichle where your new vechle was just parked")
  Player.statsmanager.update_stats("moral", - 12)
  print(Player.statsmanager.get_stat("moral")) 
  sleep(12)
  clear()
elif fule_crisis == "2":
  print("you have a dilema ahead of you.")
  sleep(10)
fule_crisis_part2=input("""
  now you have decided to go and get some petrol witch seems like the better sulution but are yuou going to pay for your fule or are you going top steal the fule ?
  1.) steal
  2.) pay
  3.) pay a subsadised amount. 
  """)
if fule_crisis_part2 == "1":
  print("you have stolen the fule and drive off but you are feeling a little guilty about stealing all that fule especialy in such an econimical crisis.")
  Player.statsmanager.update_stats("moral", - 20)
  print(Player.statsmanager.get_stat("moral"))
elif fule_crisis_part2 == "2": 
  print("you have decided to the moraly correct decicion and pay for your fule.")
  Player.statsmanager.update_stats("moral",+3)
  print(Player.statsmanager.get_stat("moral"))
elif fule_crisis_part2 == "2":
  print("you have decided to pay a subsadised amount for your fule you didnt want to steal the fule but also you didnt realy want to waste that much money on fule.")
Player.statsmanager.update_stats("moral",-13)
print(Player.statsmanager.get_stat("moral"))
sleep(10)
clear()
variable_name = input("""
so you now you have sorted out the minor life or death crisis you are now needing a place to sleep what would you like to do
1.) stay at the nearest hotel
2.) sleep in the car 
3.) bunk at the nearest hotel
""")
if variable_name == "1":
  print("you have decided to stay at the nearest hotel and sleep there for the night.")
elif variable_name == "2":
  print("you have chosen to save money and sleep in the car and take shifts watching out fo the T-1000")
  Player.satmanager.update_stats("moral", - 13)
  print(Player.statsmanager.get_stat("moral"))
elif variable_name == "3":
  print("you have decided to use a hotel room and not pay")
  Player.statsmanager.update_stats("moral", -25)
  print(Player.statsmanager.get_stat("moral"))
  sleep(10)
  clear()
print("you have woken up to the sound of the T-100 shouting at you to get your backside out of bed as he wants to get moving again")
sleep(10)
clear()
Mr_Arthur = input("""
you have been awoken, you have now gotten up and dresd as well as done all the nesasary things that you do in the morning. you have had breakfast you hav eto make another decigon do you
1.) edge your bets and stay here and gather resorses.
2.) hop in the car and get going 
3.) head to the nearest town and grab some supplies 
""")
if Mr_Arthur == "1":
  print("you decide to edge your bets and stay here im affraid the T-1000 finds you and it doesnt end well")
  Player.statsmanager.update_stats("health -12") 
  print(Player.statsmanager.get_stat("health"))
elif Mr_Arthur == "2":
  print("you have decided to hop in a car  and get going to see where the jerney would take you next you have escaped the T-1000 for now")
  Player.statsmanager.update_stats("moral", +5)
  print(Player.statsmanager.get_stat("moral")) 
elif Mr_Arthur == "3":
  print("you have decided to go to the nearest town and get some suplies but im am affraid you have gathered the supplied but the T-1000 has found you and made you skull byeconcave")
  Player.statsmanager.update_stats("health -12") 
  print(Player.statsmanager.get_stat("health"))
  sleep(10)
  clear()
  
Mr_johnson = input(""" you have escaped the T-1000 once again how much longer can you keep this up ? will you survive you next encounter ? 
There is a fork in the road, no street signs to tell you which fork does what, whitch way do you choose?
1.) right
2.) left
""")

if Mr_johnson == '1':
print("im affraid you have chosen the right option")
Player.statsmanager.update_stats("moral", +2.5)
print(Player.statsmanager.get_stat("moral")) 
else:
print("im affraid you have chosen thew wrong option and the T-1000 has found you!")
Player.statsmanager.update_stats("health -15") 
print(Player.statsmanager.get_stat("health"))

sleep(10)
clear() 
Mr_christian = input(""" 

""")
print("some parts of this code was made by @TobezEdu I take no credit for those bits of code") 
print("Help me Toby wan Kenobi") 
