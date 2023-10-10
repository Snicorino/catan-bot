import unittest
from src import main

resource = main.Resource
tileset = main.TileSet

class TestGenerateBoard(unittest.TestCase):
    def test_generate_board(self):
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
        




if __name__ == '__main__':
    unittest.main()