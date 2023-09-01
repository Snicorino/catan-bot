import numpy as np
import random
"""
class GameState:

  def __init__(self):
    # 4 rows:
    # row 1: 0-2, row 2: 3-6, row 3: 7-11, row 4: 12-15, row 5: 16-18
    self.tiles = self.initBoard()
    for x in self.tiles:
      print(x)
    pass
  # declares tiles array with near empty tiles
  def initBoard(self):
    tiles = []
    for i in range(19):
      nodes = []
      edges = []
      for j in range(6):
        # manually?
        nodes.append(Node())
        edges.append(Edge())
      tiles.append(Tile(nodes, edges, i, None, random.randint(2, 12)))  # temporary
    return tiles

class Node:
  # 7,9,11,11,9,7 represents possible settlement placements
  def __init__(self):
    # self.tiles = tiles            # array of connected tiles
    self.placement = None         # empty, settlement or city

  def placeSettlement():
    pass

  def placeCity():
    pass

  def validPlacement() -> bool:
    pass

class Edge:
  def __init__(self) -> None:
    pass

class Tile:
  # 3,4,5,4,3 represents individual hexagons
  def __init__(self, nodes, edges, index, resource, number):
    self.nodes = nodes            # array of 6 nodes connected to tile, nodes[0] is top node, clockwise
    self.edges = edges            # array of 6 edges connected to tile, edges[0] is top-right edge, connection node 0 and 1, clockwise
    self.index = index            # index in tiles array from Gamestate
    self.resource = resource      # brick, lumber, grain, wool, ore, desert
    self.number = number          # 2-12
    self.blocked = False          # depending on robber
  def __str__(self) -> str:
    return "index: " + str(self.index) + ", resource: " + str(self.resource) + ", number: " + str(self.number)

#gs1 = GameState()
"""



class Resource(Enum): # brick, lumber, grain, wool, ore, desert
  BRICK = 0
  LUMBER = 1
  GRAIN = 2
  WOOL = 3
  ORE = 4
  DESERT = 5

class Recipe():
  def __init__(self):
    pass


class Tile:
  def __init__(self, resource, dicevalue):
    self.resource = resource
    self.dicevalue = dicevalue

class TileSet:
  def __init__(self):
    self.tile = [] #for standard board [[3],[4],[5],[4],[3]]x2
    self.edge = [] #for standard board [[6],[8],[10],[10],[8],[6]]x2
    self.corner = [] #for standard board [[7],[9],[11],[11],[9],[7]]x2


  def gettile(self, i,j):
    pass


  def getcorner(self, i,j):
    pass

  def getcornerbytiles(self, idx1,idx2,idx3):
    #some function to convert idx1, idx2, idx3 to corner index
    pass

  def getlinebycorners(self, idx1, idx2):
    #some function to convert idx1, idx2 to line index
    pass


class GameState:

  def __init__(self):
    self.tileset = TileSet()
  


  def getspecialcardnum(self):
    pass

  def getplayerresourcecardnum(self, id):
    pass

  def getplayerspecialcardnum(self, id):
    pass


  def action_getspecialcard(self):
    pass

  def action_placehouse(self):
    pass

  def action_placestreet(self):
    pass

  def action_rolldice(self):
    pass

  def action_proposetrade(self, trade):
    pass

  


class Trade: #maybe just a delta for each resource
  def __init__():
    pass

class Player:
  def __init__():
    pass

  def turn(state):
    pass #interact with gamestate

  def evaltrade(offer):
    pass #return bool

  def getresourcecardnum(self):
    pass

  def getspecialcardnum(self):
    pass


"""
Player Visible Gamestate:
Tilemap (Tiles, Edges, Corners)
ModifierMap (Settlements, Roads, Robber)
ResourceCardnum (Bank, Players)
SpecialCardnum (Bank, Players)
Own resource/special cards
Prior Cards gained/traded (Other players)
Victory Points
"""


if __name__=="__main__":
  #gs1 = GameState()
  pass


