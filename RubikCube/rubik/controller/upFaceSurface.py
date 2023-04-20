from rubik.model.constants import *
from rubik.model.cube import Cube

def solveUpSurface(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the up face is solved.
        
        input:  an instance of the cube class with up-face cross solved
        output: the rotations required to solve the up surface 
         
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
    #            Declare Center of Each Face                #
    #########################################################
    UpFace = cubeList[UMM] #40 
    
    
    if cubeList[UTL]==UpFace and cubeList[UTR]==UpFace and cubeList[UBL]==UpFace and cubeList[UBR]==UpFace:
        return "".join(rotations)
    
    #########################################################
    #                     Check for Fish                    #
    #########################################################
    
    while cubeList[UTL]!=UpFace or cubeList[UTR]!=UpFace or cubeList[UBL]!=UpFace or cubeList[UBR]!=UpFace:
        if cubeList[UBL]==UpFace and cubeList[UTL]!=UpFace and cubeList[UTR]!=UpFace and cubeList[UBR]!=UpFace:
            theCube.rotate('RUrURUUr')
            rotations.append('RUrURUUr')
            cubeList = list(theCube.get())
            
        elif cubeList[UTL]==UpFace and cubeList[UBL]!=UpFace and cubeList[UBR]!=UpFace and cubeList[UTR]!=UpFace:
            theCube.rotate('uRUrURUUr')
            rotations.append('uRUrURUUr')
            cubeList = list(theCube.get())
            
        elif cubeList[UTR]==UpFace and cubeList[UTL]!=UpFace and cubeList[UBL]!=UpFace and cubeList[UBR]!=UpFace:
            theCube.rotate('UURUrURUUr')
            rotations.append('UURUrURUUr')
            cubeList = list(theCube.get())
        
        elif cubeList[UBR]==UpFace and cubeList[UBL]!=UpFace and cubeList[UTL]!=UpFace and cubeList[UTR]!=UpFace:
            theCube.rotate('URUrURUUr')
            rotations.append('URUrURUUr')
            cubeList = list(theCube.get())
            
        else:
            while cubeList[LTR]!=UpFace:
                theCube.rotate('U')
                rotations.append('U')
                cubeList = list(theCube.get())
            theCube.rotate('RUrURUUr')
            rotations.append('RUrURUUr')
            cubeList = list(theCube.get())
            
       
    return "".join(rotations)      #TODO:  remove this stubbed value
