import unittest
import collections.abc
from src import main


def get_iterable(x):
    if isinstance(x, collections.Iterable):
        return x
    else:
        return (x,)


class TestGetCornerByTiles(unittest.TestCase):
    def test_get_corner_by_tile(self):
        tileset = main.TileSet()
        
        self.assertEqual(tileset.get_corner_by_tiles((0,0),(0,1),(1,1)), tileset.get_corner(1,3))
        self.assertEqual(tileset.get_corner_by_tiles((2,1),(2,2),(3,1)), tileset.get_corner(3,4))
        self.assertEqual(tileset.get_corner_by_tiles((1,0),(1,1),(0,0)), tileset.get_corner(1,2))
        #self.assertEqual(tileset.get_corner_by_tiles((0,0),(0,1),(1,1)), tileset.get_corner(1,3))
    def test_get_tiles_by_corner(self):
        tileset = main.TileSet()
        tileset.print_tiles()
        corner = (0,0)
        for x in get_iterable(tileset.get_tiles_by_corner(corner[0], corner[1])):
            print(x)
        #self.assertEqual(tileset.get_tiles_by_corner(2,0), tileset.get_tile(0,0))
        
    
        
class TestGenerateBoard(unittest.TestCase):
    def test_generate_board(self):
        resource = main.Resource
        tileset = main.TileSet
        tiles = tileset.generate_board(self)
        resources = []
        diceValues = []
        for i in tiles:
            for j in i:
                resources.append(j.get_resource())
                diceValues.append(j.get_dice_value())
                if j.resource == resource.DESERT:
                    self.assertEqual(j.get_dice_value(), 1)
        #tests amount of occurences of each resource on board
        self.assertEqual(resources.count(resource.BRICK), 3)
        self.assertEqual(resources.count(resource.LUMBER), 4)
        self.assertEqual(resources.count(resource.WOOL), 4)
        self.assertEqual(resources.count(resource.ORE), 3)
        self.assertEqual(resources.count(resource.GRAIN), 4)
        self.assertEqual(resources.count(resource.DESERT), 1)
        #tests if dice values were distributed correctly
        self.assertEqual(diceValues.count(1), 1)
        self.assertEqual(diceValues.count(2), 1)
        self.assertEqual(diceValues.count(3), 2)
        self.assertEqual(diceValues.count(4), 2)
        self.assertEqual(diceValues.count(5), 2)
        self.assertEqual(diceValues.count(6), 2)
        self.assertEqual(diceValues.count(8), 2)
        self.assertEqual(diceValues.count(9), 2)
        self.assertEqual(diceValues.count(10), 2)
        self.assertEqual(diceValues.count(11), 2)
        self.assertEqual(diceValues.count(12), 1)
        
class TestGetAttribute(unittest.TestCase):
    def test_get_attribute(self):
        player = main.Player(None, 0)
        self.assertEqual(player.get_victory_points('vp'), 0)



if __name__ == '__main__':
    unittest.main()