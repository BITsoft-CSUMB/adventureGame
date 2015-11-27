# ----------------------------------------------  Program information    --------------------------------------

# The ultimate adventure game  
# Written by: CSIT group BitSoft

# ---------------------------------------------- Function header template -------------------------------------

# Function: What does it do
# Params: What does it accept
# Returns: What does it return
  

# ----------------------------------------------      Library imports    --------------------------------------

import time # for measuring execution time during tests


# ----------------------------------------------      Base Classes    --------------------------------------

class GameObject(object):
   def __init__(self):
      name = "game object"
      description = "A glowing green game object "


# ----------------------------------------------   Game Map Classes    --------------------------------------

class MapTile(GameObject):
   def __init__(self, name, description):
      super(MapTile, self).__init__()
      if name == "":
        self.name = "A map Title"
      if description == "":
         self.description = "a dark void of uninitialized programming"
      self.name = name
      self.description = description
      self.mapIndex = -1
      
   def __str__(self):
      return self.description

class GameMap(object):
   """The base class for all items"""
   def __init__(self):
      self.levelTitle = "level --- the end of time"
      self.exitMap = []
      self.mapTiles = [] 
          
   def __str__(self):
      return levelTitle
      
   def getExits(self, tileNumber):
      return self.exitMap[tileNumber]
    
   def setExits(self, tileNumber, exits):
      self.exitMap[tileNumber] = exits
        
   def addTile(self, mapTile, exits):
      self.mapTiles.append(mapTile)
      index = len(self.mapTiles) - 1
      self.mapTiles[index].mapIndex = index
      self.exitMap.append(exits)
           
#    def addTile(exits[5]):
    

tile = MapTile("","")        
gameMap = GameMap()
gameMap.addTile(MapTile("Starting tile", "a dark room with no exits"), [-1,-1,-1,-1,-1])
currentTile = gameMap.mapTiles[0]

exit = false

while(exit == false):
   cmd = requestString("What would you like to do?").lower()
   if cmd == "quit":
     exit = true
   else:
   showInformation("You are standing in " + str(currentTile))
#GameMap.addTile()