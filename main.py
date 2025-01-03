import os
import time
from colorama import Fore, Style
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
  def damage_player(cls, difficulty: int, atk):
    if difficulty == 1:
      cls.StatsManager.update_stat("health", atk*5)
    elif difficulty == 2:
      cls.StatsManager.update_stat("health", (atk*4))
    elif difficulty == 3:
      cls.StatsManager.update_stat("health", (atk*3))
    elif difficulty == 8:
      cls.StatsManager.update_stat("health", (atk*2))
    elif difficulty == 9:
      cls.StatsManager.update_stat("health", (atk))

health = 100000
moral = 100      
print("your health is now", Player.StatsManager.get_stat("health"))
print (" your moral is now", Player.StatsManager.get_stat("moral"))

if Player.StatsManager.update_stat("health") <1:
  print(col.RED + "I am affraid you have died!")

if Player.StatsManager.update_stat("moral") < 1: 
    print(col.RED +"I'm afraid you have run out of moral and you have subsequently dies as a reslut!")

White = "\033[0;37m"  
Orange = "\033[0;33m"

Random_intervention = input("""
Have you watched The terminator films? y/n
""")

if Random_intervention == "y" or "Y":
    print("ok good so you should know what you are doing then")
else:
    print("hmm,ok. it doesnt affect the game play but if you have watched it then you will know what is ahead")

username = input("What would you like your username to be? Please avoid capital letters: ").lower()
print("Your username is" ,username)

def loading2 (username):
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

loading2 (username)

clear()

print({col.WHITE}, "Hello", username, "! Welcome to the game!," ,{col.WHITE})
print("Welcome to my text-based adventure game.")
print("you will be playing the role of john connor")
print("""
The future has not been written. There is no fate but what we make for ourselves. I wish I could believe that. My name is John Connor, they tried to murder me before I was born, when I was 13, they tried again. Machines from the future...Terminators. All my life my mother told me the storm was coming, Judgment Day, the beginning of the war between man and machines. Three billion lives would vanish in an instant,.
you are now being hunted by an efficant killing machine from jugment day
All right, listen. The Terminator’s an infiltration unit: part man, part machine. Underneath, it’s a hyperalloy combat chassis, microprocessor-controlled. Fully armoured; very tough. But outside, it's living human tissue: flesh, skin, hair, blood - grown for the cyborgs
The 600 series had rubber skin. We spotted them easy, but these are new. They look human... sweat, bad breath, everything. Very hard to spot.
In three years, Cyberdyne will become the largest supplier of military computer systems. All stealth bombers are upgraded with Cyberdyne computers, becoming fully unmanned. Afterwards, they fly with a perfect operational record. The Skynet Funding Bill is passed. The system goes online August 4th, 1997. Human decisions are removed from strategic defence. Skynet begins to learn at a geometric rate. It becomes self-aware at 2:14 a.m. Eastern time, August 29th. In a panic, they try to pull the plug.
Skynet fights back.”
'Judgement Day'.
""")

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

print("you see a strange humonoide shape kneeling down")

choice_1 = input("""
1.) do you go and greet them 
2.) do you search arround and look for a weapon 
3.) do you try and run away
""")

if choice_1 == "1":
  print("you go up to meet them, im affraid it doesnt end well")
  Player.StatsManager.update_stat("health", -10)
  print(Player.StatsManager.get_stat("health"))
  time.sleep(2)
  
elif choice_1 == "2":
  print("the only weapon you find is a bent rusty shovel")
  attack = input("do you go and hit them with the ruty bent shovel? y/n")
  
  if attack == "y":
    print("i mean what did you exspect that you where going to own them with a shovel, no it crumbles as soon as you hit him ill stop there it didnt end well")
    time.sleep(2)
    clear()
    
    Player.StatsManager.update_stat("health", -15)
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
3.)take him on in a 1v1
""")

if choice_2 == 1:
  print("yeah once again it doesnt end well for you I shall save you the time")
  Player.StatsManager.update_stat("health", -1000)
  print(Player.StatsManager.get_stat("health"))  
  clear()
  time.sleep(2)
  
elif choice_2 == 2: 
  print("well done", username, "you have chosen the correct option")
  time.sleep(2)
  clear()
  
elif choice_2 == 3:
  print("still doesnt end well I will finnish there for your sanity")
Player.StatsManager.update_stat("health", -1500)
print(Player.StatsManager.get_stat("health"))  
clear()
clear()

trap = input("""
what kind of trap do you want to set up?
1.) exsplode the living day lights out of him
2.) make him fall into a hole 
3.) make him fall into some molten metal
""")

if trap == 1:
  print("well done you removed an arm and then he throws the arm at you pentrating your skull")
  Player.StatsManager.update_stat("health", -1000)
  print(Player.StatsManager.get_stat("health"))  

  clear()

elif trap == 2:
  print("he just jumps out of the hole as it was not deep enought you die")
  Player.StatsManager.update_stat("health", -1800)
  print(Player.StatsManager.get_stat("health"))
  clear()
    
elif trap == 3:
  print("well done you survived level one")
clear()

print("time for level 2")
lvl2_backstory = ("""
they people form the future have sent down another terminator but this time it is more advanced and upgraded.
""")
print(lvl2_backstory)
print ("your current health is", health )

start = input("Would you like to start level 2? (y/n)")
if start[0].lower() == "y": 
  print("Okay, no worries. Game beginning!")
  time.sleep(2)
  
else:
  print("Interesting.")
  Player.StatsManager.update_stat("health", -26000000000)
  print(Player.StatsManager.get_stat("health"))
  Player.StatsManager.update_stat("moral", -26000000000)
  print(Player.StatsManager.get_stat("moral"))
clear()

def loading(username):
  for i in range(4):
    print(f"{col.LIGHTYELLOW_EX}Hello, {username}! Please wait while the level finishes loading.")
    print("Loading   |")
    time.sleep(0.60)
    clear()
    print(f"{col.LIGHTYELLOW_EX}Hello, {username}! Please wait while the level finishes loading.")
    print("Loading   /")
    time.sleep(0.60)
    clear()
    print(f"{col.LIGHTYELLOW_EX}Hello, {username}! Please wait while the level finishes loading.")
    print("Loading   -")
    time.sleep(0.60)
    clear()
    print(f"{col.LIGHTYELLOW_EX}Hello, {username}! Please wait while the level finishes loading.")
    print("Loading   \\")
    time.sleep(0.60)
    clear()

loading(username)
print("I would lead what was left of the human race to ultimate victory.It hasn’t happened, no bombs fell, computers didn’t take control, we stopped Judgment Day.")
lvl2_choice = input(f"""{col.WHITE}
what would ytou like to do ?
1.) go hunting for the new veriant of the terminators
2.) wait for the terminator to find you
3.) run as far as you can
""")

if lvl2_choice == 1:
  print("yeah, you find him and you get sent back home to mum in a jam jar")
  Player.StatsManager.update_stat("health", -25.5)
  print(Player.StatsManager.get_stat("health"))
  time.sleep(2)
  
elif lvl2_choice == 2:
  print("yeah still not gonna end well")
  Player.StatsManager.update_stat("health", -20)
  print(Player.StatsManager.get_stat("health"))
  time.sleep(2)

  
elif lvl2_choice == 3:
  print("welldone",username,"you go to your secret hideout.")
  Player.StatsManager.update_stat("health", +5)
  print(Player.StatsManager.get_stat("health"))
  time.sleep(2)

print("you have made it to your secret hide out you meet up with a few peopple who agree to help you")
time.sleep(2)
clear()

ybot = input("""
what would you like to do now as you are safe for a short period of time petanshaly
would you like to :
1.) band togeather and try to make a plan to take down the terminator 
2.) stay there and hope for the best
3.) check your supplies
""")

if ybot == 1:
  print("well done",username,"you have chosen the best option")
  time.sleep(2)
  
elif ybot == 2:
  print("yeah not the best option as he finds you and ends you and your team")
  Player.StatsManager.update_stat("health", -26)
  print(Player.StatsManager.get_stat("health"))
  time.sleep(2)

  
elif ybot == 3:
  print("your supplies are full and perfect!")
  time.sleep(2)
clear()

print("""
you have gathered a team who all want the same as you and you gather your suplies and make for the chopper
""")
time.sleep(2)
clear()

erm = input("""you have gathered your supplies and headed to previous terminator strikes to see what kind of machine you are up against what would you like to do ?
1.) record all the data and then plan an attack from this information 
2.) record the information and try and intercept his next attack
3.) record how he attcks and try and find his weaknesess 
""")

if erm == "1":
  print("good choice",username,)
  time.sleep(2)
  
elif erm == "2":
  print("yeah thats not gonna work he interceps your attack on his attack")
  Player.StatsManager.update_stat("health", -15)
  print(Player.StatsManager.get_stat("health"))
  time.sleep(2)
  
elif erm == "3":
  print("yeah you find no weakneses")
  Player.StatsManager.update_stat("moral", - 10)
  print(Player.StatsManager.get_stat("moral"))
  time.sleep(2)
  
clear()

next_32 = input("""so you have recorded some information on the new generation of terminator you find that he is in a arcade what would you like to do ?
1.) bring the old genration of terminator who has been sent back in time to protect you
2.) go there and confrount him try and take him on a 1V1
3.) kiss your arse goodbye !
""")

if next_32 == "1":
  print("im affraid tht you find he is a polymorphic one but you survive ")
  Player.StatsManager.update_stat("moral", - 23)
  print(Player.StatsManager.get_stat("moral"))
  time.sleep(2)
  
elif next_32 == "2":
  print("yh you might as well kiss your arse goodbye at this point there no coming back!")
  Player.StatsManager.update_stat("health", -26)
  print(Player.StatsManager.get_stat("moral"))
  time.sleep(2)
  
elif next_32 == "3":
  print("I like your thinking you may survive this round ")
  Player.StatsManager.update_stat("health", + 26)
  print(Player.StatsManager.get_stat("health"))
  time.sleep(2)
clear()

tbyo = input("""
so you have found out that the new veriant is polymorthic and your terminator is not as efficant as the new one you see the t-800 terminator get uppercutted half way accros the parcking lot by the t-1000 what would ypu like to do ?
1.) use the shotgun to try and take it down 
2.) hop back into the truck that you got here in and drive away 
""")

if tbyo == "1":
  print(" you first shoot it in the sholder and allthought you hit and you are able to see staright through the t-1000 remorfs its self to be complete ")
  Player.StatsManager.update_stat("moral", - 32)
  print(Player.StatsManager.get_stat("moral"))
  time.sleep(2)
  
else: 
  print(" you drive away but you see the t-1000 runnig after you")
  print("you run and hide in an storm drain the t-1000 after being chased by the police he crashes his cop bike into the helicopter as he is impersinating a cop")
  Player.StatsManager.update_stat("moral", - 12 - 54)
  print(Player.StatsManager.get_stat("moral"))
  time.sleep(2)
  
clear ()


print("HAND OVER OF TEACHERS MAY BE DIRECTLY LINKED TO DETERIATION OF WORK")
sleep(20)

print("if you are still hear good on ya it may get worse fyi ")
Player.StatsManager.update_stat("health", +0.3)
print(Player.StatsManager.get_stat("health"))
time.sleep(2)
clear()

feedback = input("""
the T-1000 is now chasing you in a stolen helicopter would you like to 
1.) try and drive away
2.) lose him by chucking a few uie's
3.) other
""")

if feedback == "1":
  print("you satrt to drive away but you find thata the T-1000 is right on your tail")
  Player.StatsManager.update_stat("moral", -36)
  print(Player.StatsManager.get_stat("moral"))
  time.sleep(2)
  
elif feedback == "2":
  print("you chuck a few uie's you magange to lose him but for how long")
  Player.StatsManager.update_stat("moral", +12)
  print(Player.StatsManager.get_stat("moral"))
  time.sleep(2)

clear()
time.sleep(2)
print("you have managed to shake the T-1000 off of your tail tempararaley, you do not have enought fule to go you will have to make a vital decigion that will determin you survival.")
time.sleep(2)
clear()

fule_crisis = input("""
You do not have enogut fule to last you the journey ahead of you. You can either:
1.) hijack another vechile 
2.) get some petrol 
""")

if fule_crisis == "1":
  print("well done you have hijack a different veichle yuou have checked it over and chosen this one precisedly for its blending in ability, but you feel a little guilty about stealing the veichle evenought its a life or death situation so you leave you veichle where your new vechle was just parked")
  Player.StatsManager.update_stat("moral", - 12)
  print(Player.StatsManager.get_stat("moral")) 
  sleep(2)
  clear()
  
elif fule_crisis == "2":
  print("you have a dilema ahead of you.")
  sleep(2)
  
fule_crisis_part2=input("""
  now you have decided to go and get some petrol witch seems like the better sulution but are yuou going to pay for your fule or are you going top steal the fule ?
  1.) steal
  2.) pay
  3.) pay a subsadised amount. 
  """)

if fule_crisis_part2 == "1":
  print("you have stolen the fule and drive off but you are feeling a little guilty about stealing all that fule especialy in such an econimical crisis.")
  Player.StatsManager.update_stat("moral", - 20)
  print(Player.StatsManager.get_stat("moral"))
  time.sleep(2)
  
elif fule_crisis_part2 == "2": 
  print("you have decided to the moraly correct decicion and pay for your fule.")
  Player.StatsManager.update_stat("moral",+3)
  print(Player.StatsManager.get_stat("moral"))
  time.sleep(2)
  
elif fule_crisis_part2 == "2":
  print("you have decided to pay a subsadised amount for your fule you didnt want to steal the fule but also you didnt realy want to waste that much money on fule.")
  Player.StatsManager.update_stat("moral",-13)
  print(Player.StatsManager.get_stat("moral"))
  sleep(2)
clear()

variable_name = input("""
so you now you have sorted out the minor life or death crisis you are now needing a place to sleep what would you like to do
1.) stay at the nearest hotel
2.) sleep in the car 
3.) bunk at the nearest hotel
""")

if variable_name == "1":
  print("you have decided to stay at the nearest hotel and sleep there for the night.")
  time.sleep(2)
  
elif variable_name == "2":
  print("you have chosen to save money and sleep in the car and take shifts watching out fo the T-1000")
  Player.StatsManager.update_stat("moral", - 13)
  print(Player.StatsManager.get_stat("moral"))
  time.sleep(2)
  
elif variable_name == "3":
  print("you have decided to use a hotel room and not pay")
  Player.StatsManager.update_stat("moral", -25)
  print(Player.StatsManager.get_stat("moral"))
  sleep(2)
  clear()

print("you have woken up to the sound of the T-800 shouting at you to get your backside out of bed as he wants to get moving again")
sleep(5)
clear()

Mr_Arthur = input("""
you have been awoken, you have now gotten up and dresd as well as done all the nesasary things that you do in the morning. you have had breakfast you hav eto make another decigon do you
1.) edge your bets and stay here and gather resorses.
2.) hop in the car and get going 
3.) head to the nearest town and grab some supplies 
""")

if Mr_Arthur == "1":
  print("you decide to edge your bets and stay here im affraid the T-1000 finds you and it doesnt end well")
  Player.StatsManager.update_stat("health", -12) 
  print(Player.StatsManager.get_stat("health"))
  time.sleep(2)
  
elif Mr_Arthur == "2":
  print("you have decided to hop in a car  and get going to see where the jerney would take you next you have escaped the T-1000 for now")
  Player.StatsManager.update_stat("moral", +5)
  print(Player.StatsManager.get_stat("moral")) 
  time.sleep(2)
  
elif Mr_Arthur == "3":
  print("you have decided to go to the nearest town and get some suplies but im am affraid you have gathered the supplied but the T-1000 has found you and made you skull byeconcave")
  Player.StatsManager.update_stat("health", -12) 
  print(Player.StatsManager.get_stat("health"))
  sleep(2)
  clear()
  
Mr_johnson = input(""" you have escaped the T-1000 once again how much longer can you keep this up ? will you survive you next encounter ? 
There is a fork in the road, no street signs to tell you which fork does what, whitch way do you choose?
1.) right
2.) left
""")

if Mr_johnson == '1':
  print("im affraid you have chosen the right option")
  Player.StatsManager.update_stat("moral", +2.5)
  print(Player.StatsManager.get_stat("moral")) 
  time.sleep(2)

else:
  print("im affraid you have chosen thew wrong option and the T-1000 has found you!")
  Player.StatsManager.update_stat("health", -15) 
  print(Player.StatsManager.get_stat("health"))
  sleep(2)
clear() 

Mr_christian = input(""" 
you have managed to escape the T-1000 so far you have proved to be a formidable force, you and the T-800 have worked well as a team! 
you are feeling rather hungry and tiered you can either:
1.) go to a motel and rest well as well as have a nice breakfast/dinner to help you on your journey.
2.) you can take shifts to look after you your mum and the T-100 you will each take turns to sleep and then rotate to be on guard. 
what will you chose 1 or 2 ?
""")

if Mr_christian == '1':
  print("you have chosen the comfortable option, it has paid off well")
  time.sleep(2)
  Player.StatsManager.update_stat("health" ,+22)
  print(Player.StatsManager.get_stat("health")) 
  Player.StatsManager.update_stat("moral" ,+2)
  print(Player.StatsManager.get_stat("moral")) 

else:
  print("im affraid you have chsen the wrong option and you oversleep and the T-1000 finds you")
  time.sleep(2)
  Player.StatsManager.update_stat("health",-26) 
  print(Player.StatsManager.get_stat("health"))
  Player.StatsManager.update_stat("moral" ,-13)
  print(Player.StatsManager.get_stat("moral"))
  clear()

print("I have not watched the Terminator films in a while so this may no longer start to follow the story")
time.sleep(2)
clear()

Mr_Warwick = ("""
A radom person walks up to you on the street and says to you,'I know what you are going through I can help you',
What would you like to do ?
1.) Trust them. 
2.) Don't trust them andc walk away.
3.) Knock them unconscious and run.
your answer: 
""")

if Mr_Warwick == '1':
  print("You have chosen to ignore your gut feeling and trust them",time.sleep(5),"it doesn't work out they knock you out unconscious and robe you of all your belongings")
  time.sleep(2)
  Player.StatsManager.update_stat("health", -26) 
  print(Player.StatsManager.get_stat("health"))
  Player.StatsManager.update_stat("moral", -13)
  print(Player.StatsManager.get_stat("moral"))

elif Mr_Warwick == '2':
  print("you have decided to not trust them well done," username,"you have chosen the correct option but they still chase after you claming they can help")
  time.sleep(2)
  Player.StatsManager.update_stat("moral", -3.25)
  print(Player.StatsManager.get_stat("moral"))
clear()

elif Mr_Warwick == '3':
  print("well done,"username,"you knock the sucker out unconscious and you breake his nose while doing so as a result you have hurt your hand but it is worth it as you gain some cash.")
  time.sleep(2)  
  Player.StatsManager.update_stat("health", -5) 
  print(Player.StatsManager.get_stat("health"))
  Player.StatsManager.update_stat("moral", +23)
  print(Player.StatsManager.get_stat("moral"))
  clear()

Mrs_Hatter= input("""
you have managed to escape the police by some miricale what would you like to do now?
1.) take yourself in
2.) go and do some more crazy shit
3.) go home and rest
""")

elif Mrs_Hatter == '1':
  print("you have decided to do the moraly correct option but they just reject you and send you home")
  time.sleep(2)
  Player.StatsManager.update_stat("moral", +3.145)
  print(Player.StatsManager.get_stat("moral"))

elif Mrs_Hatter == '2':
  print("you have chosen the more reclace and fun option, ")
  time.sleep(2)
  Player.StatsManager.update_stat("moral", *2)
  print(Player.StatsManager.get_stat("moral"))

elif Mrs_Hatter == '3':
  print("you have decided to go home and be boring")
  time.sleep(2)
  Player.StatsManager.update_stat("moral",-23)
  print(Player.StatsManager.get_stat("moral")
clear()

Mini_Mr_Christian = input("""whilst you arde trying not to stay in one place for too long you get an idea to go to skyet its self to see if you can shut it down from the source you end up at a milatry base some how the T-100 has located and mannaged to smuggle you in.
what would you like to do? 
1.) steel a plane and go to sky net. 
2.) yoink a plane and do a coupkle doughtnuts. 
3.) turn arround and drive there yourself.
""")

if Mini_Mr_Christian == '1':    
  print("you have chosen to do the reclase option, but never the less it is the correct option")
  time.sleep(2)
  Player.StatsManager.update_stat("moral", + 12)
  print(Player.StatsManager.get_Stat("moral")

elif Mini_Mr_Christian == '2':
  print("you have decided to hijack a miltary grade plane and do some doughnuts, the pepple on site notice you and quesation you. you are then forced to take off and go to sky net")
  print("your the doughnut")
  time.sleep(2)
  Player.StatsManager.update_stat("moral", - 26)
  print(Player.StatsManager.get_Stat("moral")

elif Mini_Mr_Christian == '3':
  print("stupid bozo")
  time.sleep(2)
  player.StatsManager.update_stat("moral", - 12000)
  print(player.StatsManager.get_Stats("moral")
clear()
      
phoebe = input("""you reach skynet's runway but you find the door is locked to enter skynet.
1.) do you get the T-100 to rip a hole in the door 
2.) kamakazee the plane into the door 
3.) look in the plane and see if anything is there that you can use 
""")

if phoebe ==  '1':
  print("you try and get the T-100 to rip a hold in the door but no luck") 
  time.sleep(2)
  player.StatsManager.update_stat("moral", - 120)
  print(player.StatsManager.get_Stats("moral")

elif phoebe == '2':
  print("you get the T-100 to kamikaze the door but the plane end up becoming flat like it would in the cartoons.")
  time.sleep(2)
  player.StatsManager.update_stat("moral", - 12000)
  print(player.StatsManager.get_Stats("moral")

elif phoebe == '3':
  print("You have a quick search in the plane and find a lock picking kit, useing this you manage to unlock the door.")
  time.sleep(2)
  player.StatsManager.update_stat("moral", + 12)
  print(player.StatsManager.get_Stats("moral")
clear()
        
lizz =input("""
you find your way in and see that its basicaly full of conputers that don't work.
1.) do you try to go back home 
2.) look for the data room
3.) try and diasble the computers. 
""")

if lizz == '1':
  print("You try to go back home but something inseide of you wants you to acctualy do something to stop this feeling you run to the end of the runway and jump to your death!")
  time.sleep(2)
  player.StatsManager.update_stat("health", - 12000000)
  print(player.StatsManager.get_Stats("health")

elif lizz == '2':
  print("you have a quick look around you find this stair case leading to a basement, to your supprise you find the data center")
  time.sleep(2)
  player.StatsManager.update_stat("moral", + 32)
  print(player.StatsManager.get_Stats("health")

elif lizz == '3':
  print("you try to disable to computers but find that they are already deactivated so you go to the basement and find the data center.")
  player.StatsManager.update_stat("moral", - 250)
  print(player.StatsManager.get_Stats("moral")
  time.sleep(2)
clear()
        
padre == input("""you have turned on the emergancy power switch and you check the data do you 
1.) make a coppy of the data then decativate the terminators
2.) erase all the data and blow it to smitherenes 
""")

print("some parts of this code was made by @Tobezdev I take no credit for those bits of code") 
time.sleep(2)
print("Help me Toby wan Kenobi your my only hope")
print("if you understand the majority of the quote you have had a priviliged life!") 
time.sleep(2)
exit()
