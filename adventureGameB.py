# The Ultimate Adventure Game - Written by CSIT group BitSoft

power = true
zombieNum = 0
haveKeys = false

def command():
  global power
  global haveKeys
  printNow(' ')
  printNow('----- Command Center -----')
  printNow('You find yourself in the command center of a submarine')
  printNow('The dead bodies of the crew are strewn about the floor everywhere.')
  if power is true:
    printNow('Around you the consoles are spitting sparks.')
  else:
    printNow('The dim emergency lighting barely illuminates the walkways.')
  if haveKeys is true:
    printNow('Forward of your position is a door that leads to the Officers Quarters.')
  else:
    printNow('Forward of your position is a locked door.')
  printNow('Aft of your position is a door that leads to the main hallway.')
  move = doAction()
  cls()
  if move == 'fore' and haveKeys is true:
    printNow('You use the key to open the Officers Quarters.')
    return 'O'
  elif move == 'aft':
    return 'H'
  elif move == 'exit':
    return 'X'
  else:
    printNow('You are unable to move that direction or perform that action')
  return 'C'

def hallway():
  global power
  printNow(' ')
  printNow('----- Hallway -----')
  printNow('You are in the central hallway of the submarine.')
  printNow('All the bulkheads are covered in blood')
  if power is true:
    printNow('The lights above you flicker')
  else:
    printNow('The emergency lighting barely shows you the way around.')
  printNow('Forward of your position is a door that leads to Command, aft leads to the Engine Room.')
  printNow('To port is a door that leads to the Mess Hall, to starboard leads to the Crew Quarters.')
  move = doAction()
  cls()
  if move == 'fore':
    return 'C'
  elif move == 'port':
    return 'M'
  elif move == 'star':
    return 'Q'
  elif move == 'aft':
    return 'E'
  elif move == 'exit':
    return 'X'
  else:
    printNow('You are unable to move that direction or perform that action')
  return 'H'

def engineRoom():
  global power
  printNow(' ')
  printNow('----- Engine Room ------')
  if power is true:
    printNow('A single light bulb illuminates the very loud room.')
    printNow('Batteries line both sides of the room and a spinning shaft runs out the back.')
  else:
    printNow('You are in a very dark and quiet room.')
    printNow('Batteries line both sides of the room and a greasy shaft runs out the back.')
  printNow('On the left wall is the main power switch.')
  move = doAction()
  cls()
  if move == 'fore':
    return 'H'
  elif move == 'exit':
    return 'X'
  elif move == 'pwr':
    if power is true:
      power = false
      printNow('The ship suddenly falls dark and quiet as it lurches to a halt.')
    else:
      power = true
      printNow('The room suddenly lights up and the shaft in the center begins to spin.')
  else:
    printNow('You are unable to move that direction or perform that action')
  return 'E'

def crewQuarters():
  global zombieNum
  printNow(' ')
  printNow('----- Crew Quarters -----')
  printNow('The room is lined with bunks and lockers.')
  printNow('The door behind you (port side) is the only exit.')
  printNow('An undead crewman, with guts hanging from his stomach, slowly lumbers toward you.')
  move = doAction()
  if move == 'port':
    zombieNum = 0
    return 'H'
  elif move == 'atk':
    printNow('You do not have a weapon!!!')
  elif move == 'exit':
    return 'X'
  else:
    printNow('You are unable to move that direction or perform that action.')
  zombieNum += 1
  if zombieNum == 2:
    printNow('The undead crewman gets closer.')
  elif zombieNum >= 3:
    cls()
    printNow('The undead crewman attacks you and bites out your throat!')
    printNow('You lay on the floor bleeding out...better luck next time.')
    return 'X'
  return 'Q'

def messHall():
  global power
  global haveKeys
  global zombieNum
  printNow(' ')
  printNow('----- Mess Hall -----')
  if power is false:
    zombieNum += 1
    if zombieNum >= 2:
      cls()
      printNow('The undead crewman attacks you and bites out your throat!')
      printNow('You lay on the floor bleeding out...better luck next time.')
      return 'X'
    else:
      printNow('As you enter the room an undead crewman jumps at you from the darkness.')
      printNow('You are knocked back into the hallway and barely get the door closed.')
    return 'H'
  zombieNum = 0
  printNow('You are in the dining room, tables and chairs are strewn about.')
  printNow('On the floor, surrounded by dead bodies, is the ships captain.')
  if haveKeys is false:
    printNow('A large ring of keys hangs from his belt.')
  move = doAction()
  cls()
  if move == 'star':
    return 'H'
  elif move == 'keys':
    haveKeys = true
    printNow('You grab the keys to the Officers Quarters off the dead captain.')
  elif move == 'atk':
    printNow('You do not have a weapon!!!')
  elif move == 'exit':
    return 'X'
  else:
    printNow('You are unable to move that direction or perform that action.')
  return 'M'

def officersQuarters():
  global power
  global zombieNum
  printNow(' ')
  printNow('----- Officers Quarters -----')
  printNow('You have reached the front of the ship.')
  printNow('On each side are the slots that hold escape pods. One remains available...')
  escape = requestString('Do you want to enter the pod and escape: ').lower()
  cls()
  if "y" in escape:
    printNow(' ')
    printNow('----- Escape Pod -----')
    printNow('As you step into the escape pod, freedom just moments away -')
    printNow('an undead crewman attacks you from the darkness and bites your chest!')
    printNow('You are able to crush the dead crewmans skull and push the body away.')
    if power is true:
      printNow('You lay on the floor bleeding as the escape pod surfaces.')
      printNow('You feel weak and hungry for human brains and see shore through the portal.')
      printNow('Happy hunting...')
    else:
      printNow('You lay on the floor bleeding, never to leave this underwater grave.')
      printNow('You will never be able to satiate your hunger for human brains.')
    return 'X'
  zombieNum += 1
  if zombieNum <= 1:
    printNow('A dead crewman comes staggering through the door to the Command Center.')
  else:
    printNow('Your indecision has killed you. The dead crewman grabs you and begins pulling out your intestines.')
    return 'X'
  return 'O'

def doAction():
    direction = requestString('What do you want to do: ').lower()
    if "fore" in direction or "north" in direction:
      return 'fore'
    elif "aft" in direction or "south" in direction:
      return 'aft'
    elif "port" in direction or "west" in direction:
      return 'port'
    elif "star" in direction or "east" in direction:
      return 'star'
    elif "exit" in direction or "quit" in direction:
      return 'exit'
    elif "switch" in direction or "turn " in direction or "power" in direction:
      return 'pwr'
    elif "attack" in direction:
      return 'atk'
    elif "keys" in direction:
      return 'keys'
    return 'none'

def cls():
  for x in range(0, 15):
    printNow(' ')

cls()
printNow('You wake up in the center of a submarine command center.')
locationCode = 'C'
while locationCode != 'X':
  if locationCode == 'O':
    locationCode = officersQuarters()
  elif locationCode == 'C':
    locationCode = command()
  elif locationCode == 'M':
    locationCode = messHall()
  elif locationCode == 'H':
    locationCode = hallway()
  elif locationCode == 'Q':
    locationCode = crewQuarters()
  elif locationCode == 'E':
    locationCode = engineRoom()
  else:
    printNow('You seem to be lost...sending you back to command')
    locationCode = 'C'
