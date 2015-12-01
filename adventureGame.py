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

# Function: What does it do
# Params: What does it accept
# Returns: What does it return 
def play():
  global hasSpaceSuit
  hasSpaceSuit = False
  exiting = False
  winner = False
  room = 1 # Begin game in room 1 (medical bay)
  
  printNow(" -------------------------------------------------------------------------------------------------")
  printNow(" | You're in a large space station. A few hundred people used to live here, but they were attacked")
  printNow(" | by an unknown threat. Everyone evacuated. You are still here because you were in the medical")
  printNow(" | unit recovering from an explosion that heppened during routine maintenance. You were")
  printNow(" | unconscious when the attack happened and missed the action. Explore the ship, stay alive, find")
  printNow(" | your way back to earth.. To quit type quit, for commands type help, otherwise good luck.")
  printNow(" -------------------------------------------------------------------------------------------------")
  displayHelp()
  
  while not exiting and not winner:
    # User quit early if room is -1
    if room == -1:
      exiting = True
    # User won if room is 0      
    elif room == 0:
      winner = True
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
      
  if winner:
    printNow(" -------------------------------------------------------------------------------------------------")
    printNow(" | WOO? YOU WON SOME SPECIAL INTERNET BADGES HERE.")
    printNow(" -------------------------------------------------------------------------------------------------")
      

# ------------------------------------------------------------------------------------------------------------
# --------------------------------------------  Room functions   ---------------------------------------------
# ------------------------------------------------------------------------------------------------------------

# Function: Allows user to manipulate their direction, collect items, or win the game (if possible) from room
#           #1 (A.K.A. "Medical Bay").
# Params: (none)
# Returns:
#   -1          -> User requested help.
#   0           -> User won the game.
#   integer > 0 -> The next room number to move to.
# Notes: 
#   Room number -> 1
#   Room name   -> "Medical Bay"
#   Exits       -> East (utility tunnel)               to room 2 ("Space Walk Utility Room")
#               -> South (airlock)                     to room 4 ("Transit Bay")
#               -> [hidden exit] North (sliding panel) to room 6 ("Drug Closet")
def roomOne():
  slideDoorOpen = False
  printNow(" -------------------------------------------------------------------------------------------------")
  printNow(" You are standing in the medical bay. To the south is an airlock. To the east is the Utility tunnel.")
  printNow(" To the north is a medical cabinet that looks like it has already been pilfered for supplies.")
  cmd = getDirection()
  
  if cmd == "search cabinet":
    printNow(" It looks like the cabinet might be able to slide if you pushed it.")
    cmd = getDirection()
  if "cabinet" in cmd and ("slide" in cmd or "push" in cmd): 
    printNow(" You push the cabinet out of the way, opening a door to the north. It will spring shut if you walk")
    printNow(" away so be careful")
    slideDoorOpen = True
    cmd = getDirection()
  if isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 1
  elif cmd == "east" or cmd == "e":
    return 2
  elif cmd == "south" or cmd == "s":
    return 4
  elif cmd == "north" or cmd == "n":
    if slideDoorOpen == False:
      printNow(" You run into the medical cabinet and it shakes a bit, maybe you should search it more closely")
    else:
      printNow(" You sneak into the hidden medical closet")
      return 6
  return 1 # Return the room we're in if user doesn't indicate valid response

# Function: Allows user to manipulate their direction, collect items, or win the game (if possible) from room
#           #2 (A.K.A. "Space Walk Utility Room").
# Params: (none)
# Returns:
#   -1          -> User requested help.
#   0           -> User won the game.
#   integer > 0 -> The next room number to move to.
# Notes: 
#   Room number -> 2
#   Room name   -> "Space Walk Utility Room"
#   Exits       -> West (utility tunnel)               to room 1 ("Medical Bay")
#               -> South (airlock)                     to room 3 ("Cafeteria")
#   * User can grab the space suit to win the game here (set hasSpaceSuit to True).
def roomTwo():
  global hasSpaceSuit
  printNow(" -------------------------------------------------------------------------------------------------")
  printNow(" You are standing in the space walk utility room. To the North is the Utility Tunnel to the medical")
  printNow(" bay. To the south is an airlock.")
  cmd = getDirection()
  if hasSpaceSuit == False: 
    printNow(" There is a space suit here.")
    if "get" in cmd and "suit" in cmd: # Looking for something like "get space suit"
      hasSpaceSuit = True
      printNow(" You have picked up the space suit.")
      # Get a new command from the user if they got the space suit.
      cmd = getDirection() 
  if cmd == "north" or cmd == "n": 
     return 1
  elif cmd == "south" or cmd == "s":
     return 3
  elif isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 2
  return 2

# Function: Allows user to manipulate their direction, collect items, or win the game (if possible) from room
#           #3 (A.K.A. "Cafeteria").
# Params: (none)
# Returns:
#   -1          -> User requested help.
#   0           -> User won the game.
#   integer > 0 -> The next room number to move to.
# Notes: 
#   Room number -> 3
#   Room name   -> "Cafeteria"
#   Exits       -> North (airlock)                     to room 2 ("Space Walk Utility Room")
#               -> West (catwalk)                      to room 4 ("Transit Bay")
def roomThree():
  printNow(" -------------------------------------------------------------------------------------------------")
  printNow(" You are standing in the cafeteria. To the West is a catwalk that looks like it could be sketchy. To")
  printNow(" the North is an airlock.")
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


# Rooms:
# 1 -> "Medical Bay"             E ("utility tunnel") to 2; S ("airlock") to 4; N ([hidden] "sliding panel") to 6
# 2 -> "Space Walk Utility Room" W ("utility tunnel") to 1; S ("airlock") to 3
# 3 -> "Cafeteria"               N ("airlock") to 2; W ("catwalk") to 4
# 4 -> "Transit Bay"             E ("catwalk") to 3; N ("airlock") to 1; W ("ladder") to 5
# 5 -> "Missile Room"            S ("ladder") to 4
# 6 -> "[hidden] Drug Closet"    S ("sliding panel") to 1

# Function: Allows user to manipulate their direction, collect items, or win the game (if possible) from room
#           #4 (A.K.A. "Transit Bay").
# Params: (none)
# Returns:
#   -1          -> User requested help.
#   0           -> User won the game.
#   integer > 0 -> The next room number to move to.
# Notes: 
#   Room number -> 4
#   Room name   -> "Transit Bay"
#   Exits       -> East (catwalk)  to room 3 ("Cafeteria")
#               -> North (airlock) to room 1 ("Medical Bay")
#               -> West (ladder)   to room 5 ("Missile Room")
def roomFour():
  printNow(" -------------------------------------------------------------------------------------------------")
  printNow(" You are standing in the transit bay. To the East is a catwalk. To the North is an airlock. There")
  printNow(" is a ladder here as well.")
  cmd = getDirection()
  if isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 4
  if cmd == "use ladder" or cmd == "go up" or "climb ladder":
    if hasSpaceSuit:
      printNow(" It is a bit awkward with the space suit, but you make your way up the ladder.")
    return 5
  if cmd == "north" or cmd == "n":
    return 1 
  if cmd == "east" or cmd == "e":
    return 3
  return 4

# Function: Allows user to manipulate their direction, collect items, or win the game (if possible) from room
#           #5 (A.K.A. "Missile Room").
# Params: (none)
# Returns:
#   -1          -> User requested help.
#   0           -> User won the game.
#   integer > 0 -> The next room number to move to.
# Notes: 
#   Room number -> 5
#   Room name   -> "Missile Room"
#   Exits       -> South (ladder) to room 4 ("Transit Bay")
def roomFive():
  global hasSpaceSuit
  printNow(" -------------------------------------------------------------------------------------------------")
  printNow(" You are standing in the missile room. There is a big red button here and a ladder leading back")
  printNow(" down to the transit bay.")
  cmd = getDirection()
    
  if "button" in cmd and "press" in cmd:
    if hasSpaceSuit:
      printNow(" You press the red button, and hop into the missile.")
      return 0 # Woo! Win!
    else:
      printNow(" You can't press that button without a space suit on, you'll die.") # we should let them die...
  if isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 5
  return 5

# Function: Allows user to manipulate their direction, collect items, or win the game (if possible) from room
#           #1 (A.K.A. "Medical Bay").
# Params: (none)
# Returns:
#   -1          -> User requested help.
#   0           -> User won the game.
#   integer > 0 -> The next room number to move to.
# Notes: 
#   Room number -> 6
#   Room name   -> "[hidden] Drug Closet"
#   Exits       -> South (sliding panel) to room 1 ("Medical Bay")
def roomSix(): #die instantly in here because there is an alien? or maybe pick up something cool?
  printNow(" -------------------------------------------------------------------------------------------------")
  printNow(" You are standing in the medical supply closet. To the south is the medical bay.")
  printNow(" Most of the medicines look like they have been taken. In the corner you see a large ")
  printNow(" slime covered blob rifling through a pile of empty bottles and boxes. The alien seems ")
  printNow(" occupied and has not noticed you entering the closet yet.")
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
  printNow("") # Extra vertical space
  return raw_input(" What would you like to do? >>> ").lower()

# Function: Prints a goodbye message if the user wishes to quit.
# Params:
#   command -> The command the user input.
# Returns: What does it return
#   True -> User wishes to quit.
#   False -> User doesn't with to quit.
def isQuit(command):
  if command == "quit":
    printNow(" Luckily you hid a cyanide capsule in your pocket. You pull it out and bite down on it. Goodbye.")
    return True
  return False

# Function: Prints helpful instructions if the user requests help.
# Params:
#   command -> The command the user input.
# Returns:
#   True -> User requested help.
#   False -> User did not request help.
def isHelp(command):
  printNow(" -------------------------------------------------------------------------------------------------")
  if command == "help":
    displayHelp()
    return True
  return False

# Function: Displays helpful instructions.
# Params: (none)
# Returns: (none)
def displayHelp():
  printNow(" | Movement: north, south, east, west.")
  printNow(" | Items: get, press. Ex. get space suit, press button")
