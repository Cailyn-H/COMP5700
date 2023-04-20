from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.model.cube import Cube
from rubik.model.constants import *
import hashlib
import random

def solve(parms):
    """Return rotates needed to solve input cube"""
    
    result = {}
     
    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)
    
    #########################################################
    #         Check Cube Validation Before Rotation         #
    #########################################################
    if theCube.get() is None or (len(theCube.get()) == 0):
        result['status'] = 'error: '
        return result
    
    elif (len(theCube.get()) != numofElements):
        result['status'] = 'error: '
        return result
    
    elif (len(set(theCube.get())) > numofFaces):
        result['status'] = 'error: '
        return result
        
    else:
        for i in list(theCube.get()):
            if not((47<ord(i)<58) or (64<ord(i)<91) or (96<ord(i)<123)):
                result['status'] = 'error: '
                return result
    
    for character in set(list(theCube.get())):
        for element in list(theCube.get()):
            if element == character:
                charactersOfCube.append(element)
        if len(charactersOfCube) > 9:
            result['status'] = 'error: '
            return result
        else:
            charactersOfCube.clear()
    
    for character in list(theCube.get()):
        facesOfCube = [list(theCube.get())[4],list(theCube.get())[13],list(theCube.get())[22],list(theCube.get())[31],list(theCube.get())[40],list(theCube.get())[49]]
        if len(set(facesOfCube)) < 6:
            result['status'] = 'error: '
            return result
    
    
    
    
    #########################################################
    #               Only Validated Cube Goes on             #
    #########################################################
    rotations = ""
    rotations += solveBottomCross(theCube)      #iteration 2
    rotations += solveBottomLayer(theCube)      #iteration 3
    rotations += solveMiddleLayer(theCube)      #iteration 4
    rotations += solveUpCross(theCube)          #iteration 5
    rotations += solveUpSurface(theCube)        #iteration 5
    rotations += solveUpperLayer(theCube)       #iteration 6
    
    
    
    result['solution'] = rotations
    result['status'] = 'ok' 
    
    itemToTokenize = theCube.get()+result['solution']+'yzh0068'
    sha256Hash = hashlib.sha256()
    sha256Hash.update(itemToTokenize.encode())
    fullToken = sha256Hash.hexdigest()
    
    #########################################################
    #       generate length 8 substring for integrity       #
    #########################################################
    idx = random.randrange(0, len(fullToken) - integritySubStr + 1)
    result['integrity'] = fullToken[idx : (idx+integritySubStr)]                    #iteration 3
    
    
    return result







