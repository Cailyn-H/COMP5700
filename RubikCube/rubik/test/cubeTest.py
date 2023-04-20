'''
Created on Jan 27, 2023

@author: cailynhyun
'''
import unittest 
import rubik.model.cube as cube


class CubeTest(unittest.TestCase):


    def test_rotate_010_F_Rotation(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('F')
        self.assertEqual('ok', rotatedCube['status'])
        self.assertEqual(rotatedCube['cube'], theCube.get())
        
    
    def test_rotate_015_f_Rotation(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('f')
        self.assertEqual('ok', rotatedCube['status'])
        self.assertEqual(rotatedCube['cube'], theCube.get())
        
        
    def test_rotate_020_R_Rotation(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('R') #R - Right clockwise 
        self.assertEqual('ok', rotatedCube['status'])
        self.assertEqual(rotatedCube['cube'], theCube.get())
        
        
    def test_rotate_025_r_Rotation(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('r') 
        self.assertEqual('ok', rotatedCube['status'])
        self.assertEqual(rotatedCube['cube'], theCube.get())
        
    
    def test_rotate_030_B_Rotation(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('B') 
        self.assertEqual('ok', rotatedCube['status'])
        self.assertEqual(rotatedCube['cube'], theCube.get())
        
    
    def test_rotate_035_b_Rotation(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('b') 
        self.assertEqual('ok', rotatedCube['status'])
        self.assertEqual(rotatedCube['cube'], theCube.get())
        
    
    def test_rotate_040_L_Rotation(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('L') 
        self.assertEqual('ok', rotatedCube['status'])
        self.assertEqual(rotatedCube['cube'], theCube.get())
        
    
    def test_rotate_045_l_Rotation(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('l') 
        self.assertEqual('ok', rotatedCube['status'])
        self.assertEqual(rotatedCube['cube'], theCube.get())
        
    
    def test_rotate_050_U_Rotation(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('U') 
        self.assertEqual('ok', rotatedCube['status'])
        self.assertEqual(rotatedCube['cube'], theCube.get())
        
        
    def test_rotate_055_u_Rotation(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('u') 
        self.assertEqual('ok', rotatedCube['status'])
        self.assertEqual(rotatedCube['cube'], theCube.get())
        
    
    def test_rotate_100_missingDirection(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate(None) 
        self.assertEqual('ok', rotatedCube['status'])
        self.assertEqual(rotatedCube['cube'], theCube.get())
        
        
    
    def test_rotate_110_emptyDirection(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate("") 
        self.assertEqual('ok', rotatedCube['status'])
        self.assertEqual(rotatedCube['cube'], theCube.get())
        
        
        
    def test_rotate_120_multipleRotation(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('uLBf') 
        self.assertEqual('ok', rotatedCube['status'])
        self.assertEqual(rotatedCube['cube'], theCube.get())
        
    
    
    def test_rotate_130_missingCube(self):
        theCube = cube.Cube(None)
        rotatedCube = theCube.rotate('F') 
        self.assertEqual('error: ', rotatedCube['status'])
        
    
    def test_rotate_140_emptyCube(self):
        cubeToRotate=''
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('F') 
        self.assertEqual('error: ', rotatedCube['status'])
        
        
    
    def test150_extraKeyCube(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrroooooooookggkgggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('F') 
        self.assertEqual('error: ', rotatedCube['status'])

        
        
    def test_rotate_910_invalidDirection(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('K') 
        self.assertEqual('error: ', rotatedCube['status'])
    
    
    
    def test_rotate_920_invalidCube(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwwwqqqqqqqqq'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('F') 
        self.assertEqual('error: ', rotatedCube['status'])
     
     
        
    def test_rotate_930_illigalCube(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyy*********'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('F') 
        self.assertEqual('error: ', rotatedCube['status'])
        
    
    def test_rotate_940_multiOccurenceOfLegalChar(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwwb'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('F') 
        self.assertEqual('error: ', rotatedCube['status'])
        
    
    def test_rotate_950_nonUniqueMiddleElement(self):
        cubeToRotate='bbbbbbbbbrrrrbrrrrooooboooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('F') 
        self.assertEqual('error: ', rotatedCube['status'])
          
        