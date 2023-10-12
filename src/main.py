from typing import Any
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

class Corner:
  def __init__(self) -> None:
    self.settled = False
    self.id = -1

class Tile:

  def __init__(self, resource: Resource, dicevalue: int) -> None:
    self.resource = resource
    self.dicevalue = dicevalue

  def get_resource(self) -> Resource:
    return self.resource
  
  def get_dice_value(self) -> int:
    return self.dicevalue
  
  def __str__(self) -> str:
    return str(self.resource)[9:] + ";" + str(self.dicevalue)

class TileSet:

  def __init__(self) -> None:
    #for standard board [[3],[4],[5],[4],[3]]x2
    self.tile = self.generate_board()

    #for i in self.tile:
    #  for j in i:
    #    print(str(j) + ", ", end="")
    #  print()
    
    self.edge = [] #for standard board [[6],[8],[10],[10],[8],[6]]x2
    #for standard board [[7],[9],[11],[11],[9],[7]]x2
    self.corner = [[Corner(), Corner(), Corner(), Corner(), Corner(), Corner(), Corner()],
                   [Corner(), Corner(), Corner(), Corner(), Corner(), Corner(), Corner(), Corner(), Corner()],
                   [Corner(), Corner(), Corner(), Corner(), Corner(), Corner(), Corner(), Corner(), Corner(), Corner(), Corner()],
                   [Corner(), Corner(), Corner(), Corner(), Corner(), Corner(), Corner(), Corner(), Corner(), Corner(), Corner()],
                   [Corner(), Corner(), Corner(), Corner(), Corner(), Corner(), Corner(), Corner(), Corner()],
                   [Corner(), Corner(), Corner(), Corner(), Corner(), Corner(), Corner(), ]] 

  #problem: don't think distribution of resources and dice values is random
  def generate_board(self) -> []:
    initTiles = [[Tile(Resource.GRAIN, 5), Tile(Resource.WOOL, 2), Tile(Resource.GRAIN, 6)],
                 [Tile(Resource.BRICK, 8), Tile(Resource.GRAIN, 10), Tile(Resource.ORE, 9), Tile(Resource.WOOL, 3)],
                 [Tile(Resource.LUMBER, 4), Tile(Resource.LUMBER, 3), Tile(Resource.ORE, 11), Tile(Resource.GRAIN, 4), Tile(Resource.ORE, 8)],
                 [Tile(Resource.LUMBER, 11), Tile(Resource.BRICK, 6), Tile(Resource.WOOL, 5), Tile(Resource.LUMBER, 10)],
                 [Tile(Resource.WOOL, 12), Tile(Resource.DESERT, 1), Tile(Resource.BRICK, 9)]] 
    availableResources = [Resource.BRICK, Resource.BRICK, Resource.BRICK, Resource.WOOL, Resource.WOOL, Resource.WOOL, Resource.WOOL, Resource.ORE, Resource.ORE, Resource.ORE,
                          Resource.LUMBER, Resource.LUMBER, Resource.LUMBER, Resource.LUMBER, Resource.GRAIN, Resource.GRAIN, Resource.GRAIN, Resource.GRAIN, Resource.DESERT]
    availableDiceValues = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]

    for i in range (len(initTiles)):
      for j in range(len(initTiles[i])):
        resourceValue = availableResources.pop(random.randint(0, len(availableResources)-1))
        if resourceValue != Resource.DESERT:
          diceValue = availableDiceValues.pop(random.randint(0, len(availableDiceValues)-1))
          initTiles[i][j] = Tile(resourceValue, diceValue)
        else: 
          initTiles[i][j] = Tile(resourceValue, 1)
    return initTiles
  
  def get_tile(self, i: int, j: int) -> Tile:
    return self.tile[i][j]

  def get_corner(self, i: int, j: int) -> Corner:
    return self.corner[i][j]

  def get_corner_by_tiles(self, tile1: (int, int), tile2: (int, int), tile3: (int, int)):
    #print()
    #print(tile1, tile2, tile3)
    #need to be valid connecting tiles
    #tile 1 always top/bottom left, tile2 always top/bottom right, tile3 always peak of triangle (top or bottom)
    if (tile1[1] + 1 == tile2[1]) & (tile1[0] == tile2[0]):
      if (tile1[0]+1 == tile3[0]) & (tile1[1]+1 == tile3[1]): #top is flat, upper half of board
        return self.corner[tile3[0]][2*tile3[1]+1]
      if (tile1[0]+1 == tile3[0]) & (tile1[1] == tile3[1]): #top is flat, lower half of board
        return self.corner[tile3[0]][2*tile2[1]]
      if (tile1[0]-1 == tile3[0]) & (tile1[1] == tile3[1]): #top is pointed, upper half
        return self.corner[tile1[0]][2*tile2[1]]
      if (tile1[0]-1 == tile3[0]) & (tile1[1]+1 == tile3[1]): #top is pointed, lower half
        return self.corner[tile1[0]][2*tile2[1]+1]
    else:
      return None

  def get_line_by_corners(self, idx1, idx2):
    #some function to convert idx1, idx2 to line index
    pass

class GameState:

  def __init__(self) -> None:
    self.tileset = TileSet()
    #14 knights, 2 road buildings, 2 year of plentys, 2 monopolys, 5 victory points
    self.devset = [DevCard.KNIGHT, DevCard.KNIGHT, DevCard.KNIGHT, DevCard.KNIGHT, DevCard.KNIGHT, DevCard.KNIGHT, DevCard.KNIGHT, DevCard.KNIGHT, DevCard.KNIGHT, DevCard.KNIGHT, 
                   DevCard.KNIGHT, DevCard.KNIGHT, DevCard.KNIGHT, DevCard.KNIGHT, DevCard.ROAD_BUILD, DevCard.ROAD_BUILD, DevCard.YEAR_OF_PLENTY, DevCard.YEAR_OF_PLENTY, 
                   DevCard.MONOPOLY, DevCard.MONOPOLY, DevCard.VICTORY_POINT, DevCard.VICTORY_POINT, DevCard.VICTORY_POINT, DevCard.VICTORY_POINT, DevCard.VICTORY_POINT]
    #19 of each ressource, individual or together?
    self.resourceset = []
    #players?
    self.players = [Player(self, 0), Player(self, 1), Player(self, 2), Player(self, 3)]

  def get_dev_card_num(self) -> int:
    return len(self.devset)

  def get_player_resource_card_num(self, id: int) -> int:
    return self.players[id].get_resource_card_num()

  def get_player_dev_card_num(self, id: int) -> int:
    return self.players[id].get_dev_card_num()


  def action_get_dev_card(self) -> None:
    pass

  def action_place_settlement(self) -> None:
    pass

  def action_place_road(self) -> None:
    pass

  def action_roll_dice(self) -> None:
    pass

  def action_propose_trade(self, trade) -> None:
    pass

  


class Trade: #maybe just a delta for each resource

  def __init__() -> None:
    pass

class Player:
  #call cunstructor with gamestate? 
  def __init__(self, state: GameState, id: int) -> None:
    self.devset = []
    self.resourceset = []
    self.state = state
    self.id = id
  
  #source either other player or bank, triggered by robbing, dice rolls, trading, dev cards
  #should maybe be in gamestate class
  def collect_resource(self, resource: Resource, source: []):
    idx = random.randint(0, len(source))
    self.resourceset.append(source.pop(idx))
  
  def purchase_dev_card(self, bank: []):
    idx = random.randint(0, len(bank))
    self.devset.append(bank.pop(idx))

  #parameter state not necessary?
  def turn(state) -> None:
    pass #interact with gamestate

  def eval_trade(offer) -> bool:
    pass #return bool

  def get_resource_card_num(self) -> int:
    return len(self.resourceset)

  def get_dev_card_num(self) -> int:
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
  #ts = TileSet()
  pass


