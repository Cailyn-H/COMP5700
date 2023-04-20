from rubik.model.constants import *
from rubik.model.cube import Cube

def solveUpCross(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube into the up-face cross configuration.
        
        input:  an instance of the cube class with the middle layer solved
        output: the rotations required to solve the up-face cross  
    ''' 
    '''
    #########################################################
    #         Check Cube Validation Before Rotation         #
    #########################################################
    if theCube.get() is None or (len(theCube.get()) == 0):
        
        return ""
    
    elif (len(theCube.get()) != numofElements):
        
        return ""
    
    elif (len(set(theCube.get())) > numofFaces):
            
            return ""
        
    else:
        for i in list(theCube.get()):
            if not((47<ord(i)<58) or (64<ord(i)<91) or (96<ord(i)<123)):
                
                return ""
    
    for character in set(list(theCube.get())):
        for element in list(theCube.get()):
            if element == character:
                charactersOfCube.append(element)
        if len(charactersOfCube) > 9:
            
            return ""
        else:
            charactersOfCube.clear()
    
    for character in list(theCube.get()):
        facesOfCube = [list(theCube.get())[4],list(theCube.get())[13],list(theCube.get())[22],list(theCube.get())[31],list(theCube.get())[40],list(theCube.get())[49]]
        if len(set(facesOfCube)) < 6:
            
            return ""
    '''
    
    rotations = []
    cubeList = list(theCube.get())
    #########################################################
    #              Declare Center of Up Face                #
    #########################################################
    UpFace = cubeList[UMM] #40 
    
    #########################################################
    #                                                       #
    #          Checking for Perfect Up Face Cross           #
    #             Before Starting a Rotation                #
    #########################################################
    if cubeList[UTM]==UpFace and cubeList[UML]==UpFace and cubeList[UMR]==UpFace and cubeList[UBM]==UpFace:
        return "".join(rotations)

    while cubeList[UTM]!=UpFace or cubeList[UML]!=UpFace or cubeList[UMR]!=UpFace or cubeList[UBM]!=UpFace:
        if cubeList[UTM]!=UpFace and cubeList[UML]!=UpFace and cubeList[UMR]!=UpFace and cubeList[UBM]!=UpFace:
            theCube.rotate('FRUruf')
            rotations.append('FRUruf')
            cubeList = list(theCube.get())
            
        if cubeList[UTM]==UpFace and cubeList[UML]==UpFace:
            theCube.rotate('FRUruf')
            rotations.append('FRUruf')
            cubeList = list(theCube.get())
            
        elif cubeList[UML]==UpFace and cubeList[UBM]==UpFace:
            theCube.rotate('RBUbur')
            rotations.append('RBUbur')
            cubeList = list(theCube.get())
            
        elif cubeList[UBM]==UpFace and cubeList[UMR]==UpFace:
            theCube.rotate('BLUlub')
            rotations.append('BLUlub')
            cubeList = list(theCube.get())
        
        elif cubeList[UMR]==UpFace and cubeList[UTM]==UpFace:
            theCube.rotate('LFUful')
            rotations.append('LFUful')
            cubeList = list(theCube.get())
        
        if cubeList[UML]==UpFace and cubeList[UMR]==UpFace:
            theCube.rotate('FRUruf')
            rotations.append('FRUruf')
            cubeList = list(theCube.get())
        
        elif cubeList[UBM]==UpFace and cubeList[UTM]==UpFace:
            theCube.rotate('RBUbur')
            rotations.append('RBUbur')
            cubeList = list(theCube.get())
        
        elif cubeList[UML]==UpFace and cubeList[UMR]==UpFace:
            theCube.rotate('BLUlub')
            rotations.append('BLUlub')
            cubeList = list(theCube.get())
        
        elif cubeList[UTM]==UpFace and cubeList[UBM]==UpFace:
            theCube.rotate('LFUful')
            rotations.append('LFUful')
            cubeList = list(theCube.get())
            
    return "".join(rotations)      #TODO:  remove this stubbed value
