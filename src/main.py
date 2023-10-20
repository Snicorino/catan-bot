from typing import Any
import numpy as np
import random
from enum import Enum

class Resource(Enum):
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
    self.id = -1

  def can_place_settlement(self, id: int) -> bool:
    return self.id == -1  #todo: plus no other settlements in surrounding corners
  
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
    
    self.edge = [] #for standard board [[6],[8],[10],[10],[8],[6]]x2 plus vertical edges

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

  def get_corner_by_tiles(self, tile1: (int, int), tile2: (int, int), tile3: (int, int)) -> Corner:
    #todo: need to be valid connecting tiles
    
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

  def get_edge_by_corners(self, idx1, idx2):
    #some function to convert idx1, idx2 to edge index
    pass

  def get_tiles_by_corner(self, i: int, j: int) -> list[Tile]:
    #todo: LUT?, put outside of method
    lut = [ [[self.get_tile(0, 0)],[self.get_tile(0, 0)],[self.get_tile(0, 0), self.get_tile(0, 1)], [self.get_tile(0, 1)], [self.get_tile(0, 1), self.get_tile(0, 2)],
              [self.get_tile(0, 2)], [self.get_tile(0, 2)]],
            [[self.get_tile(1, 0)], [self.get_tile(1, 0), self.get_tile(0, 0)], [self.get_tile(1, 0), self.get_tile(0, 0), self.get_tile(1, 1)],
              [self.get_tile(1, 1), self.get_tile(0, 0), self.get_tile(0, 1)], [self.get_tile(1, 1), self.get_tile(0, 1), self.get_tile(1, 2)],
              [self.get_tile(1, 2), self.get_tile(0, 1), self.get_tile(0, 2)], [self.get_tile(1, 2), self.get_tile(1, 3), self.get_tile(0, 2)],
              [self.get_tile(1, 3), self.get_tile(0, 2)], [self.get_tile(1, 3)]],
            []] #todo
    return lut[i][j]

  # returns value which corresponds to likeliness that a settlement on that corner receives resources at dice roll, ranks corners by value
  def corner_value(self, i: int, j: int) -> int:
    val = 0
    for x in self.get_tiles_by_corner(i, j):
      val += 6 - abs(7-x.dicevalue)
    return val
    
  def print_tiles(self) -> None:
    for i in self.tile:
            for j in i:
                print(j, end=" ")
            print()

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


  def action_get_dev_card(self, id: int) -> None:
    if self.players[id].can_purchase(Recipe.DEVCARD):
      if bool(self.devset): #False if devset empty?
        self.players[id].resourceset.remove(Resource.GRAIN)
        self.players[id].resourceset.remove(Resource.WOOL)
        self.players[id].resourceset.remove(Resource.ORE)
        #choose random dev card from stack
        idx = random.randint(0, len(self.devset))
        #add that dev card to players dev stack
        self.players[id].devset.append(self.devset.pop(idx))
      else:
        print("No more dev cards to purchase")
    else:
      print("Not enough resources to purchase dev card")

  def action_place_settlement(self, id: int, i: int, j: int) -> None:
    if self.players[id].can_purchase(Recipe.SETTLEMENT):
      if self.tileset.get_corner(i, j).can_place_settlement(id):
        self.tileset.corner[i][j].id = id #use get_corner?
        self.players[id].vp += 1
        self.players[id].resourceset.remove(Resource.GRAIN)
        self.players[id].resourceset.remove(Resource.WOOL)
        self.players[id].resourceset.remove(Resource.LUMBER)
        self.players[id].resourceset.remove(Resource.BRICK)
      else:
        print("Can't place settlement on wanted corner")
    else:
      print("Not enough resources to place settlement")
      


  def action_place_road(self) -> None:
    pass

  def action_roll_dice(self) -> None:
    r1 = random.randint(1, 6)
    r2 = random.randint(1, 6)
    rolledVal = r1 + r2
    if rolledVal == 7:
      #robber, discard cards
      pass
    #todo: hand out resources to players

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
    self.vp = 0
  
  #source either other player or bank, triggered by robbing, dice rolls, trading, dev cards
  #should maybe be in gamestate class?
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
  
  def get_victory_points(self, __name: str) -> Any:
    return self.vp
  
  def can_purchase(self, rec: Recipe) -> bool:
    if rec == Recipe.CITY:
      return self.resourceset.count(Resource.ORE)>=3 & self.resourceset.count(Resource.GRAIN)>=2
    if rec == Recipe.SETTLEMENT:
      return self.resourceset.count(Resource.WOOL)>=1 & self.resourceset.count(Resource.GRAIN)>=1 & self.resourceset.count(Resource.LUMBER)>=1 & self.resourceset.count(Resource.BRICK)>=1
    if rec == Recipe.ROAD:
      return self.resourceset.count(Resource.BRICK)>=1 & self.resourceset.count(Resource.LUMBER)>=1
    if rec == Recipe.DEVCARD:
      return self.resourceset.count(Resource.GRAIN)>=1 & self.resourceset.count(Resource.WOOL)>=1 & self.resourceset.count(Resource.ORE)>=1
    else:
      return None





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
  pass


