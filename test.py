import unittest
from src import main
resource = main.Resource
tileset = main.TileSet

class TestGenerateBoard(unittest.TestCase):
    def test_generate_board(self):
        tiles = tileset.generate_board(self)
        
        for i in tiles:
            for j in i:
                if j.resource == resource.DESERT:
                    self.assertEqual(j.dicevalue, 1)
                print(str(j) + ", ", end="")
            print()
        self.assertEqual(1,1)
        




if __name__ == '__main__':
    unittest.main()