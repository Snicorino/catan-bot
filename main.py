import numpy as np
import random
from enum import Enum
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

class DevCard(Enum):
  KNIGHT = 0
  ROAD_BUILD = 1
  YEAR_OF_PLENTY = 2
  MONOPOLY = 3
  VICTORY_POINT = 4
  
class Recipe(Enum):
  #alternative use numbers 0-3
  ROAD = [Resource.LUMBER, Resource.BRICK]
  SETTLEMENT = [Resource.LUMBER, Resource.BRICK, Resource.WOOL, Resource.GRAIN]
  CITY = [Resource.ORE, Resource.ORE, Resource.ORE, Resource.GRAIN, Resource.GRAIN]
  DEVCARD = [Resource.ORE, Resource.GRAIN, Resource.WOOL]

class Tile:
  def __init__(self, resource, dicevalue):
    self.resource = resource
    self.dicevalue = dicevalue
  def __str__(self) -> str:
    return str(self.resource)[9:] + ";" + str(self.dicevalue)

class TileSet:
  def __init__(self):
    #for standard board [[3],[4],[5],[4],[3]]x2
    self.tile = [[Tile(Resource.GRAIN, 5), Tile(Resource.WOOL, 2), Tile(Resource.GRAIN, 6)],
                 [Tile(Resource.BRICK, 8), Tile(Resource.GRAIN, 10), Tile(Resource.ORE, 9), Tile(Resource.WOOL, 3)],
                 [Tile(Resource.LUMBER, 4), Tile(Resource.LUMBER, 3), Tile(Resource.ORE, 11), Tile(Resource.GRAIN, 4), Tile(Resource.ORE, 8)],
                 [Tile(Resource.LUMBER, 11), Tile(Resource.BRICK, 6), Tile(Resource.WOOL, 5), Tile(Resource.LUMBER, 10)],
                 [Tile(Resource.WOOL, 12), Tile(Resource.DESERT, 1), Tile(Resource.BRICK, 9)]] 
    self.generate_board()
    for i in self.tile:
      for j in i:
        print(str(j) + ", ", end="")
      print()
    
    self.edge = [] #for standard board [[6],[8],[10],[10],[8],[6]]x2
    self.corner = [] #for standard board [[7],[9],[11],[11],[9],[7]]x2

  #problem: don't think distribution of resources and dice values is random
  def generate_board(self):
    availableResources = [Resource.BRICK, Resource.BRICK, Resource.BRICK, Resource.WOOL, Resource.WOOL, Resource.WOOL, Resource.WOOL, Resource.ORE, Resource.ORE, Resource.ORE,
                          Resource.LUMBER, Resource.LUMBER, Resource.LUMBER, Resource.LUMBER, Resource.GRAIN, Resource.GRAIN, Resource.GRAIN, Resource.GRAIN, Resource.DESERT]
    availableDiceValues = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
    for i in range (len(self.tile)):
      for j in range(len(self.tile[i])):
        resourceValue = availableResources.pop(random.randint(0, len(availableResources)-1))
        if resourceValue != Resource.DESERT:
          diceValue = availableDiceValues.pop(random.randint(0, len(availableDiceValues)-1))
          self.tile[i][j] = Tile(resourceValue, diceValue)
        else: 
          self.tile[i][j] = Tile(resourceValue, 1)
  

  def get_tile(self, i,j):
    return self.tile[i][j]


  def get_corner(self, i,j):
    pass

  def get_corner_by_tiles(self, idx1,idx2,idx3):
    #some function to convert idx1, idx2, idx3 to corner index
    pass

  def get_line_by_corners(self, idx1, idx2):
    #some function to convert idx1, idx2 to line index
    pass


class GameState:

  def __init__(self):
    self.tileset = TileSet()
    #14 knights, 2 road buildings, 2 year of plentys, 2 monopolys, 5 victory points
    self.devset = [DevCard.KNIGHT, DevCard.KNIGHT, DevCard.KNIGHT, DevCard.KNIGHT, DevCard.KNIGHT, DevCard.KNIGHT, DevCard.KNIGHT, DevCard.KNIGHT, DevCard.KNIGHT, DevCard.KNIGHT, 
                   DevCard.KNIGHT, DevCard.KNIGHT, DevCard.KNIGHT, DevCard.KNIGHT, DevCard.ROAD_BUILD, DevCard.ROAD_BUILD, DevCard.YEAR_OF_PLENTY, DevCard.YEAR_OF_PLENTY, 
                   DevCard.MONOPOLY, DevCard.MONOPOLY, DevCard.VICTORY_POINT, DevCard.VICTORY_POINT, DevCard.VICTORY_POINT, DevCard.VICTORY_POINT, DevCard.VICTORY_POINT]
    #19 of each ressource, individual or together?
    self.resourceset = []

  def get_special_card_num(self):
    return len(self.devset)

  def get_player_resource_card_num(self, id):
    pass

  def get_player_special_card_num(self, id):
    pass


  def action_get_special_card(self):
    pass

  def action_place_settlement(self):
    pass

  def action_place_road(self):
    pass

  def action_roll_dice(self):
    pass

  def action_propose_trade(self, trade):
    pass

  


class Trade: #maybe just a delta for each resource
  def __init__():
    pass

class Player:
  #call cunstructor with gamestate? 
  def __init__(self, state):
    self.devset = []
    self.resourceset = []
    self.state = state
  
  #source either other player or bank, triggered by robbing, dice rolls, trading, dev cards
  def collect_resource(self, resource: Resource, source: []):
    idx = random.randint(0, len(source))
    self.resourceset.append(source.pop(idx))
  
  def purchase_dev_card(self, bank):
    idx = random.randint(0, len(bank))
    self.devset.append(bank.pop(idx))

  #parameter state not necessary?
  def turn(state):
    pass #interact with gamestate

  def eval_trade(offer):
    pass #return bool

  def get_resource_card_num(self):
    return len(self.resourceset)

  def get_special_card_num(self):
    return len(self.devset)


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
  ts = TileSet()
  #print(Recipe.SETTLEMENT)
  pass


