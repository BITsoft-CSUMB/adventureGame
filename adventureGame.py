# ------------------------------------------------------------------------------------------------------------
# ----------------------------------------------  Program information    -------------------------------------
# ------------------------------------------------------------------------------------------------------------
# The ultimate adventure game  
# Written by: CSIT group BitSoft

# ------------------------------------------------------------------------------------------------------------
# --------------------------------------------  Function header template   -----------------------------------
# ------------------------------------------------------------------------------------------------------------
# Function: What does it do
# Params: What does it accept
# Returns: What does it return

# ------------------------------------------------------------------------------------------------------------
# --------------------------------------------  Player variables  --------------------------------------------
# ------------------------------------------------------------------------------------------------------------

hasSpaceSuit = False

# ------------------------------------------------------------------------------------------------------------
# --------------------------------------------  Play game  ---------------------------------------------------
# ------------------------------------------------------------------------------------------------------------

def play():
  global hasSpaceSuit
  exit = False
  won = False
  room = 1 # Begin game in room 1 (medical bay)
  hasSpaceSuit = False
  
  printNow(" | *****")
  printNow(" | You're in a large space station. A few hundred people used to live here, but they were attacked")
  printNow(" | by an unknown threat. Everyone evacuated. You are still here because you were in the medical")
  printNow(" | unit recovering from an explosion that heppened during routine maintenance. You were")
  printNow(" | unconscious when the attack happened and missed the action. Explore the ship, stay alive, find")
  printNow(" | your way back to earth.. To quit type quit, for commands type help, otherwise good luck.")
  printNow(" | *****")
  
  while not exit and not won:
    # User quit early if room is -1
    if room == -1:
      exit = True
    # User won if room is 0      
    elif room == 0:
      won = True
    elif room == 1:
      room = roomOne()
    elif room == 2:
      room = roomTwo()
    elif room == 3:
      room = roomThree()
    elif room == 4:
      room = roomFour()
    elif room == 5:
      room = roomFive()
    elif room == 6:
      room = roomSix()

# ------------------------------------------------------------------------------------------------------------
# --------------------------------------------  Room functions   ---------------------------------------------
# ------------------------------------------------------------------------------------------------------------

# Rooms:
# 1 -> "Medical Bay"             E ("utility tunnel") to 2; S ("airlock") to 4; N ([hidden] "sliding panel") to 6
# 2 -> "Space Walk Utility Room" W ("utility tunnel") to 1; S ("airlock") to 3
# 3 -> "Cafeteria"               N ("airlock") to 2; W ("catwalk") to 4
# 4 -> "Transit Bay"             E ("catwalk") to 3; N ("airlock") to 1; W ("ladder") to 5
# 5 -> "Missile Room"            S ("ladder") to 4
# 6 -> "[hidden] Drug Closet"    S ("sliding panel") to 1 # NOTE: ROOM 6 NOT YET IMPLEMENTED

# Return the room number (or set room to the room number) that the user would like to go to next (while loop 
# to ensure their entry is valid?). 
def roomOne():
  slideDoorOpen = False
  
  printNow("You are standing in the medical bay. To the south is an airlock. To the east is the Utility tunnel.")
  printNow("To the north is a medical cabinet that looks like it has already been pilfered for supplies.")
  cmd = getDirection()
  
  if cmd == "search cabinet":
    printNow("It looks like the cabinet might be able to slide if you pushed it.")
    cmd = getDirection()
  if cmd == "push cabinet" or cmd == "push medical cabinet" or cmd == "slide cabinet" or cmd == "slide medical cabinet":
      printNow("You push the cabinet out of the way, opening a door to the north. It will spring shut if you walk")
      printNow(" away so be careful")
      slideDoorOpen = True
      cmd = getDirection()
  if isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 1
  elif cmd == "east" or cmd == "e":
    return 2 # utility tunnel
  elif cmd == "south" or cmd == "s":
    return 4 # airlock
  elif cmd == "north" or cmd == "n":
    if slideDoorOpen == False:
      printNow("You run into the medical cabinet and it shakes a bit, maybe you should search it more closely")
    else:
      printNow("You sneak into the hidden medical closet")
      return 6
  return 1 # Return the room we're in if user doesn't indicate valid response
  
# User can grab the space suit to win the game here (set hasSpaceSuit to True)
def roomTwo():
  global hasSpaceSuit
  printNow("You are standing in the space walk utility room. To the North is the Utility Tunnel back to the medical")
  printNow("bay. To the south is an airlock.")
  cmd = getDirection()
  if hasSpaceSuit == False: 
    printNow("There is a space suit here")
    if cmd == "get space suit" or cmd == "get suit":
      hasSpaceSuit = True
      printNow("You have picked up the space suit.")
      cmd = getDirection() # <-- second get command to decide what to do after getting the suit
  if cmd == "north" or cmd == "n": 
     return 1 #medical bay
  elif cmd == "south" or cmd == "s":
     return 3 #airlock
  elif isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 2
  return 2
  
def roomThree():
  printNow("You are standing in the cafeteria. To the West is a catwalk that looks like it could be sketchy. To")
  printNow("the North is an airlock.")
  cmd = getDirection()
  if isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 3
  if cmd == "north" or cmd == "n":
    return 2
  if cmd == "west" or cmd == "w":
    return 4
  return 3

def roomFour():
  printNow("You are standing in the transit bay. To the East is a catwalk. To the North is an airlock. There is a")
  printNow("ladder here as well.")
  cmd = getDirection()
  if isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 4
  if cmd == "use ladder" or cmd == "go up":
    if hasSpaceSuit:
      printNow("It is a bit akward with the space suit, but you make your way up the ladder.")
    return 5
  if cmd == "north" or cmd == "n":
    return 1 
  if cmd == "east" or cmd == "e":
    return 3
  return 4

def roomFive():
  global hasSpaceSuit
  printNow("You are standing in the missile room. There is a big red button here and a ladder leading back down to")
  printNow("the transit bay.")
  cmd = getDirection()
    
  if cmd == "press red button" or cmd == "press button":
    if hasSpaceSuit:
      printNow("You press the red button, and hop into the missile.")
      return 0 # Woo! Win!
    else:
      printNow("You can't press that button without a space suit on, you'll die.") # we should let them die...
  if isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 5
  return 5

def roomSix(): #die instantly in here because there is an alien? or maybe pick up something cool?
  printNow("You are standing in the medical supply closit. To the south is the medical bay.")
  printNow("Most of the medicines look like they have been taken. In the corner you see a large ")
  printNow("slime covered blob rifling through a pile of empty bottle and boxes. The alien seems ")
  printNow("occupied and has not noticed you entering the closet yet.")
  cmd = getDirection()
  
  if isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 6
  elif cmd == "south" or cmd == "s":
    return 1
  return 6

# ------------------------------------------------------------------------------------------------------------
# --------------------------------------------  Helper functions   -------------------------------------------
# ------------------------------------------------------------------------------------------------------------

# Function: Gets instructions from user.
# Params: (none)
# Returns: The user's instructions as raw text.
def getDirection():
  return raw_input("What would you like to do? ").lower()

# Function: Prints a goodbye message if the user wishes to quit.
# Params:
#   command -> The command the user input.
# Returns: What does it return
#   True -> User wishes to quit.
#   False -> User doesn't with to quit.
def isQuit(command):
  if command == "quit":
    printNow("Luckily you hid a cyanide capsule in your pocket. You pull it out and bite down on it. Goodbye.")
    return True
  return False

# Function: Prints helpful instructions if the user requests help.
# Params:
#   command -> The command the user input.
# Returns:
#   True -> User requested help.
#   False -> User did not request help.
def isHelp(command):
  if command == "help":
    printNow("Movement: north, south, east, west. Items: get, press. Examples: get space suit, press button")
    return True
  return False
