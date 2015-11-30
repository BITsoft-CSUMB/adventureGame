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
# --------------------------------------------  Play game  ---------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
hasSpaceSuit = False

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
  printNow(" | your way back to earth.. To quit type quit, otherwise good luck.")
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

# ------------------------------------------------------------------------------------------------------------
# --------------------------------------------  Room functions   ---------------------------------------------
# ------------------------------------------------------------------------------------------------------------

# Rooms:
# 1 -> "Medical Bay"             ("utility tunnel" to 2, "airlock" to 4, [hidden] "sliding panel" to 6)
# 2 -> "Space Walk Utility Room" ("utility tunnel" to 1, "airlock" to 3)
# 3 -> "Cafeteria"               ("airlock" to 2, "catwalk" to 4)
# 4 -> "Transit Bay"             ("catwalk" to 3, "airlock" to 1, "ladder" to 5)
# 5 -> "Missile Room"            ("ladder" to 4)
# 6 -> "[hidden] Drug Closet"    ("sliding panel" to 1) # NOTE: ROOM 6 NOT YET IMPLEMENTED

# Return the room number (or set room to the room number) that the user would like to go to next (while loop 
# to ensure their entry is valid?). 
def roomOne():
  printNow("You are standing in the medical bay. Utility tunnel or airlock")
  cmd = getDirection()
  if isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 1
  elif cmd == "utility tunnel":
    return 2
  elif cmd == "airlock":
    return 4
  return 1 # Return the room we're in if user doesn't indicate valid response
  
# User can grab the space suit to win the game here (set hasSpaceSuit to True)
def roomTwo():
  global hasSpaceSuit
  printNow("You are standing in the space walk utility room.")
  cmd = getDirection()
  if cmd == "space suit":
    hasSpaceSuit = True
    cmd = getDirection()
  if isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 2
  return 3 # TODO: Should change to 2 when other elifs are filled in
  
def roomThree():
  printNow("You are standing in the cafeteria.")
  cmd = getDirection()
  if isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 3
  return 4 # TODO: Should change to 3 when other elifs are filled in

def roomFour():
  printNow("You are standing in the transit bay.")
  cmd = getDirection()
  if isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 4
  return 5 # TODO: Should change to 4 when other elifs are filled in

def roomFive():
  global hasSpaceSuit
  printNow("You are standing in the missile room. (there's a big red button)")
  cmd = getDirection()
  if cmd == "big red button":
    if hasSpaceSuit:
      return 0 # Woo! Win!
    else:
      cmd = getDirection() 
  if isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 5
  return 6 # TODO: Should change to 5 when other elifs are filled in


# ------------------------------------------------------------------------------------------------------------
# --------------------------------------------  Helper functions   -------------------------------------------
# ------------------------------------------------------------------------------------------------------------
def getDirection():
  return requestString("What would you like to do?").lower()

def isQuit(command):
  if command == "quit":
    printNow("WE'RE SO SAD TO SEE YOU GO OR SOMETHING!!")
    return True
  return False
  
def isHelp(command):
  if command == "help":
    printNow("HERE ARE SOME HELPFUL INSTRUCTIONS!")
    return True
  return False
