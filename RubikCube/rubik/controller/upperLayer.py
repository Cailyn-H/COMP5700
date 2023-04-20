from rubik.model.constants import *
from rubik.model.cube import Cube

def solveUpperLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the entire upper layer is solved.
        
        input:  an instance of the cube class with up-face surface solved
        output: the rotations required to solve the upper layer  
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
    cube = theCube.get()
    #########################################################
    #            Declare Center of Each Face                #
    #########################################################
    DownFace = cubeList[DMM] #49
    FrontFace = cubeList[FMM] #4
    RightFace = cubeList[RMM] #13
    BackFace = cubeList[BMM] #22
    LeftFace = cubeList[LMM] #31
    UpFace = cubeList[UMM] #40 
    
    
    #########################################################
    #              Checking for Perfect Cube                #
    #########################################################
    if cubeList[FTL]==FrontFace and cubeList[FTM]==FrontFace and cubeList[FTR]==FrontFace and cubeList[RTL]==RightFace and cubeList[RTM]==RightFace and cubeList[RTR]==RightFace and cubeList[BTL]==BackFace and cubeList[BTM]==BackFace and cubeList[BTR]==BackFace and cubeList[LTL]==LeftFace and cubeList[LTM]==LeftFace and cubeList[LTR]==LeftFace:
        return "".join(rotations)
    
    #########################################################
    #                     Start Rotations                   #
    #########################################################
    while set(cubeList[FTL:FML])!=set(FrontFace) or set(cubeList[RTL:RML])!=set(RightFace) or set(cubeList[BTL:BML])!=set(BackFace) or set(cubeList[LTL:LML])!=set(LeftFace):  
        if (cubeList[FTL]==FrontFace and cubeList[FTR]==FrontFace) or (cubeList[RTL]==FrontFace and cubeList[RTR]==FrontFace) or (cubeList[BTL]==FrontFace and cubeList[BTR]==FrontFace) or (cubeList[LTL]==FrontFace and cubeList[LTR]==FrontFace):
            if set(cubeList[FTL:RTL])!=set(FrontFace) and not (cubeList[FTL]==FrontFace and cubeList[FTR]==FrontFace and cubeList[RTL]==RightFace and cubeList[RTR]==RightFace and cubeList[BTL]==BackFace and cubeList[BTR]==BackFace and cubeList[LTL]==LeftFace and cubeList[LTR]==LeftFace):
                while (cubeList[FTL]!=FrontFace and cubeList[FTR]!=FrontFace):
                    theCube.rotate('U')
                    rotations.append('U')
                    cubeList = list(theCube.get())
                theCube.rotate('fUBuFUbBUbUBUUb')
                rotations.append('fUBuFUbBUbUBUUb')
                cubeList = list(theCube.get())
     
        elif (cubeList[FTL]==RightFace and cubeList[FTR]==RightFace) or (cubeList[RTL]==RightFace and cubeList[RTR]==RightFace) or (cubeList[BTL]==RightFace and cubeList[BTR]==RightFace) or (cubeList[LTL]==RightFace and cubeList[LTR]==RightFace):
            if set(cubeList[RTL:BTL])!=set(RightFace):
                while (cubeList[RTL]!=RightFace and cubeList[RTR]!=RightFace):
                    theCube.rotate('U')
                    rotations.append('U')
                    cubeList = list(theCube.get())
                theCube.rotate('rULuRUlLUlULUUl')
                rotations.append('rULuRUlLUlULUUl')
                cubeList = list(theCube.get())
                
        elif (cubeList[FTL]==BackFace and cubeList[FTR]==BackFace) or (cubeList[RTL]==BackFace and cubeList[RTR]==BackFace) or (cubeList[BTL]==BackFace and cubeList[BTR]==BackFace) or (cubeList[LTL]==BackFace and cubeList[LTR]==BackFace):
            if set(cubeList[BTL:LTL])!=set(BackFace):
                while (cubeList[BTL]!=BackFace and cubeList[BTR]!=BackFace):
                    theCube.rotate('U')
                    rotations.append('U')
                    cubeList = list(theCube.get())
                theCube.rotate('bUFuBUfFUfUFUUf')
                rotations.append('bUFuBUfFUfUFUUf')
                cubeList = list(theCube.get())
            
        elif (cubeList[FTL]==LeftFace and cubeList[FTR]==LeftFace) or (cubeList[RTL]==LeftFace and cubeList[RTR]==LeftFace) or (cubeList[BTL]==LeftFace and cubeList[BTR]==LeftFace) or (cubeList[LTL]==LeftFace and cubeList[LTR]==LeftFace):
            if set(cubeList[LTL:UTL])!=set(LeftFace):
                while (cubeList[LTL]!=LeftFace and cubeList[LTR]!=LeftFace):
                    theCube.rotate('U')
                    rotations.append('U')
                    cubeList = list(theCube.get())
                theCube.rotate('lURuLUrRUrURUUr')
                rotations.append('lURuLUrRUrURUUr')
                cubeList = list(theCube.get())
                
        else:  
            theCube.rotate('lURuLUrRUrURUUr')
            rotations.append('lURuLUrRUrURUUr')
            cubeList = list(theCube.get())
        
        if set(cubeList[FTL:RTL])==set(FrontFace):
            theCube.rotate('BBUlRBBrLUBB')
            rotations.append('BBUlRBBrLUBB')
            cubeList = list(theCube.get())
            
        elif set(cubeList[RTL:BTL])==set(RightFace):
            theCube.rotate('LLUfBLLbFULL')
            rotations.append('LLUfBLLbFULL')
            cubeList = list(theCube.get())  
        
        elif set(cubeList[BTL:LTL])==set(BackFace):
            theCube.rotate('FFUrLFFlRUFF')
            rotations.append('FFUrLFFlRUFF')
            cubeList = list(theCube.get())
        
        elif set(cubeList[LTL:UTL])==set(LeftFace):
            theCube.rotate('FFUrLFFlRUFF')
            rotations.append('FFUrLFFlRUFF')
            cubeList = list(theCube.get())
    
        elif cubeList[FTL]==FrontFace and cubeList[FTR]==FrontFace and cubeList[RTL]==RightFace and cubeList[RTR]==RightFace and cubeList[BTL]==BackFace and cubeList[BTR]==BackFace and cubeList[LTL]==LeftFace and cubeList[LTR]==LeftFace:
            theCube.rotate('FFUrLFFlRUFF')
            rotations.append('FFUrLFFlRUFF')
            cubeList = list(theCube.get())
        
    return "".join(rotations)      #TODO:  remove this stubbed value
