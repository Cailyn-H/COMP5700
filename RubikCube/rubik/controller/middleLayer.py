from rubik.model.constants import *
from rubik.model.cube import Cube

def solveMiddleLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the middle layer is solved.
        
        input:  an instance of the cube class with the bottom layer solved
        output: the rotations required to solve the middle layer  
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
    DownFace = cubeList[DMM] #49
    FrontFace = cubeList[FMM] #4
    RightFace = cubeList[RMM] #13
    BackFace = cubeList[BMM] #22
    LeftFace = cubeList[LMM] #31
    UpFace = cubeList[UMM] #40 
    
    
    
    #########################################################
    #                                                       #
    #           Checking for Perfect Middle Layer           #
    #             Before Starting a Rotation                #
    #########################################################
    if (cubeList[FML]==FrontFace and cubeList[FMR]==FrontFace and cubeList[RML]==RightFace and cubeList[RMR]==RightFace and cubeList[BML]==BackFace and cubeList[BMR]==BackFace and cubeList[LML]==LeftFace and cubeList[LMR]==LeftFace):
        return "".join(rotations)
    
    #########################################################
    #                                                       #
    #           Start Rotating for Middle Layer             #
    #                                                       #
    #########################################################    
    while (cubeList[FML]!=FrontFace or cubeList[FMR]!=FrontFace or cubeList[RML]!=RightFace or cubeList[RMR]!=RightFace or cubeList[BML]!=BackFace or cubeList[BMR]!=BackFace or cubeList[LML]!=LeftFace or cubeList[LMR]!=LeftFace):
        #########################################################
        #                                                       #
        #               Start Rotating for Up Face              #
        #                                                       #
        ######################################################### 
        ##############
        # Front Face #
        ##############
        if cubeList[RTM] == FrontFace:
            theCube.rotate('U')
            rotations.append('U')
            cubeList = list(theCube.get())
            
        elif cubeList[BTM] == FrontFace:
            theCube.rotate('UU')
            rotations.append('UU')
            cubeList = list(theCube.get())
        
        elif cubeList[LTM] == FrontFace:
            theCube.rotate('u')
            rotations.append('u')
            cubeList = list(theCube.get())
            
        if cubeList[UBM] == RightFace:
            theCube.rotate('URurufUF')
            rotations.append('URurufUF')
            cubeList = list(theCube.get())
            
        elif cubeList[UBM] == LeftFace:
            theCube.rotate('ulULUFuf')
            rotations.append('ulULUFuf')
            cubeList = list(theCube.get())
        
        ##############
        # Right Face #
        ##############
        if cubeList[FTM] == RightFace:
            theCube.rotate('u')
            rotations.append('u')
            cubeList = list(theCube.get())
        
        elif cubeList[LTM] == RightFace:
            theCube.rotate('uu')
            rotations.append('uu')
            cubeList = list(theCube.get())
            
            
        elif cubeList[BTM] == RightFace:
            theCube.rotate('U')
            rotations.append('U')
            cubeList = list(theCube.get())
            
        if cubeList[UMR] == BackFace:
            theCube.rotate('UBuburUR')
            rotations.append('UBuburUR')
            cubeList = list(theCube.get())
        
        elif cubeList[UMR] == FrontFace:
            theCube.rotate('ufUFURur')
            rotations.append('ufUFURur')
            cubeList = list(theCube.get())
            
        
        ##############
        #  Back Face #
        ##############
        if cubeList[RTM] == BackFace:
            theCube.rotate('u')
            rotations.append('u')
            cubeList = list(theCube.get())
        
        elif cubeList[FTM] == BackFace:
            theCube.rotate('uu')
            rotations.append('uu')
            cubeList = list(theCube.get())
            
        elif cubeList[LTM] == BackFace:
            theCube.rotate('U')
            rotations.append('U')
            cubeList = list(theCube.get())
        
        if cubeList[UTM] == RightFace:
            theCube.rotate('urURUBub')
            rotations.append('urURUBub')
            cubeList = list(theCube.get())
            
        elif cubeList[UTM] == LeftFace:
            theCube.rotate('ULulubUB')
            rotations.append('ULulubUB')
            cubeList = list(theCube.get())
        
        ##############
        #  Left Face #
        ##############
        if cubeList[BTM] == LeftFace:
            theCube.rotate('u')
            rotations.append('u')
            cubeList = list(theCube.get())
        
        elif cubeList[RTM] == LeftFace:
            theCube.rotate('uu')
            rotations.append('uu')
            cubeList = list(theCube.get())
        
        elif cubeList[FTM] == LeftFace:
            theCube.rotate('U')
            rotations.append('U')
            cubeList = list(theCube.get())
            
        
        if cubeList[UML] == BackFace:
            theCube.rotate('ubUBULul')
            rotations.append('ubUBULul')
            cubeList = list(theCube.get())
            
        elif cubeList[UML] == FrontFace:
            theCube.rotate('UFufulUL')
            rotations.append('UFufulUL')
            cubeList = list(theCube.get())
            
        
        #########################################################
        #                                                       #
        #             Start Rotating for Front Face             #
        #                                                       #
        ######################################################### 
        if cubeList[RML] == FrontFace and cubeList[FMR] == RightFace:
            theCube.rotate('URurufUFUUURurufUF')
            rotations.append('URurufUFUUURurufUF')
            cubeList = list(theCube.get())
        
        if cubeList[FTM] == RightFace:
            theCube.rotate('u')
            rotations.append('u')
            cubeList = list(theCube.get())
            
            if cubeList[UMR] == BackFace:
                theCube.rotate('UBuburUR')
                rotations.append('UBuburUR')
                cubeList = list(theCube.get())
                   
            elif cubeList[UMR] == FrontFace:
                theCube.rotate('ufUFURur')
                rotations.append('ufUFURur')
                cubeList = list(theCube.get())
                   
                
        elif cubeList[FTM] == BackFace:
            theCube.rotate('uu')
            rotations.append('uu')
            cubeList = list(theCube.get())
            
            
            if cubeList[UTM] == LeftFace:
                theCube.rotate('ULulubUB')
                rotations.append('ULulubUB')
                cubeList = list(theCube.get())
                
            elif cubeList[UTM] == RightFace:
                theCube.rotate('urURUBub')
                rotations.append('urURUBub')
                cubeList = list(theCube.get())
                
        elif cubeList[FTM] == LeftFace:
            theCube.rotate('U')
            rotations.append('U')
            cubeList = list(theCube.get())
            
            if cubeList[UML] == FrontFace:
                theCube.rotate('UFufulUL')
                rotations.append('UFufulUL')
                cubeList = list(theCube.get())
                
            elif cubeList[UML] == BackFace:
                theCube.rotate('ubUBULul')
                rotations.append('ubUBULul')
                cubeList = list(theCube.get())
                
        else:
            if cubeList[UBM] == RightFace:
                theCube.rotate('URurufUF')
                rotations.append('URurufUF')
                cubeList = list(theCube.get())
                
            elif cubeList[UBM] == LeftFace:
                theCube.rotate('ulULUFuf')
                rotations.append('ulULUFuf')
                cubeList = list(theCube.get())
                
        #########################################################
        #                                                       #
        #             Start Rotating for Right Face             #
        #                                                       #
        #########################################################    
        if cubeList[BML] == RightFace and cubeList[RMR] == BackFace:
            theCube.rotate('UBuburURUUUBuburUR')
            rotations.append('UBuburURUUUBuburUR')
            cubeList = list(theCube.get())
        
        if cubeList[RTM] == FrontFace:
            theCube.rotate('U')
            rotations.append('U')
            cubeList = list(theCube.get())
            
            if cubeList[UBM] == RightFace:
                theCube.rotate('URurufUF')
                rotations.append('URurufUF')
                cubeList = list(theCube.get())
                
            elif cubeList[UBM] == LeftFace:
                theCube.rotate('ulULUFuf')
                rotations.append('ulULUFuf')
                cubeList = list(theCube.get())
                
        elif cubeList[RTM] == LeftFace:
            theCube.rotate('UU')
            rotations.append('UU')
            cubeList = list(theCube.get())
            if cubeList[UML] == FrontFace:
                theCube.rotate('UFufulUL')
                rotations.append('UFufulUL')
                cubeList = list(theCube.get())
                
            elif cubeList[UML] == BackFace:
                theCube.rotate('ubUBULul')
                rotations.append('ubUBULul')
                cubeList = list(theCube.get())
                
        elif cubeList[RTM] == BackFace:
            theCube.rotate('u')
            rotations.append('u')
            cubeList = list(theCube.get())
            
            
            if cubeList[UTM] == RightFace:
                theCube.rotate('urURUBub')
                rotations.append('urURUBub')
                cubeList = list(theCube.get())
                
            elif cubeList[UTM] == LeftFace:
                theCube.rotate('ULulubUB')
                rotations.append('ULulubUB')
                cubeList = list(theCube.get())
                
        else:
            if cubeList[UMR] == BackFace:
                theCube.rotate('UBuburUR')
                rotations.append('UBuburUR')
                cubeList = list(theCube.get())
                
            elif cubeList[UMR] == FrontFace:
                theCube.rotate('ufUFURur')
                rotations.append('ufUFURur')
                cubeList = list(theCube.get())
                
        #########################################################
        #                                                       #
        #             Start Rotating for Back Face              #
        #                                                       #
        #########################################################  
        if cubeList[LML] == BackFace and cubeList[BMR] == LeftFace:
            theCube.rotate('ULulubUBUUULulubUB')
            rotations.append('ULulubUBUUULulubUB')
            cubeList = list(theCube.get())
            
        if cubeList[BTM] == LeftFace:
            theCube.rotate('u')
            rotations.append('u')
            cubeList = list(theCube.get())
            
            
            if cubeList[UML] == FrontFace:
                theCube.rotate('UFufulUL')
                rotations.append('UFufulUL')
                cubeList = list(theCube.get())
            
            elif cubeList[UML] == BackFace:
                theCube.rotate('ubUBULul')
                rotations.append('ubUBULul')
                cubeList = list(theCube.get())
                
        elif cubeList[BTM] == FrontFace:
            theCube.rotate('uu')
            rotations.append('uu')
            cubeList = list(theCube.get())
            
            if cubeList[UBM] == RightFace:
                theCube.rotate('URurufUF')
                rotations.append('URurufUF')
                cubeList = list(theCube.get())
                
            elif cubeList[UBM] == LeftFace:
                theCube.rotate('ulULUFuf')
                rotations.append('ulULUFuf')
                cubeList = list(theCube.get())
                
        elif cubeList[BTM] == RightFace:
            theCube.rotate('U')
            rotations.append('U')
            cubeList = list(theCube.get())
            
            if cubeList[UMR] == BackFace:
                theCube.rotate('UBuburUR')
                rotations.append('UBuburUR')
                cubeList = list(theCube.get())
                
            elif cubeList[UMR] == FrontFace:
                theCube.rotate('ufUFURur')
                rotations.append('ufUFURur')
                cubeList = list(theCube.get())
                
        else:
            if cubeList[UTM] == LeftFace:
                theCube.rotate('ULulubUB')
                rotations.append('ULulubUB')
                cubeList = list(theCube.get())
                
            elif cubeList[UTM] == RightFace:
                theCube.rotate('urURUBub')
                rotations.append('urURUBub')
                cubeList = list(theCube.get())
                
        #########################################################
        #                                                       #
        #             Start Rotating for Left Face              #
        #                                                       #
        #########################################################  
        if cubeList[FML] == LeftFace and cubeList[LMR] == FrontFace:
            theCube.rotate('UFufulUL')
            rotations.append('UFufulUL')
            cubeList = list(theCube.get())
            theCube.rotate('UUUFufulUL')
            rotations.append('UUUFufulUL')
            cubeList = list(theCube.get())
            
        if cubeList[LTM] == FrontFace:
            theCube.rotate('u')
            rotations.append('u')
            cubeList = list(theCube.get())
            
            if cubeList[UBM] == LeftFace:
                theCube.rotate('ulULUFuf')
                rotations.append('ulULUFuf')
                cubeList = list(theCube.get())
                
            elif cubeList[UBM] == RightFace:
                theCube.rotate('URurufUF')
                rotations.append('URurufUF')
                cubeList = list(theCube.get())
                
        elif cubeList[LTM] == RightFace:
            theCube.rotate('uu')
            rotations.append('uu')
            cubeList = list(theCube.get())
            
            if cubeList[UMR] == FrontFace:
                theCube.rotate('ufUFURur')
                rotations.append('ufUFURur')
                cubeList = list(theCube.get())
                
            elif cubeList[UMR] == BackFace:
                theCube.rotate('UBuburUR')
                rotations.append('UBuburUR')
                cubeList = list(theCube.get())
                
        elif cubeList[LTM] == BackFace:
            theCube.rotate('U')
            rotations.append('U')
            cubeList = list(theCube.get())
            
            if cubeList[UTM] == RightFace:
                theCube.rotate('urURUBub')
                rotations.append('urURUBub')
                cubeList = list(theCube.get())
                
            elif cubeList[UTM] == LeftFace:
                theCube.rotate('ULulubUB')
                rotations.append('ULulubUB')
                cubeList = list(theCube.get())
                
                
        else:
            if cubeList[UML] == BackFace:
                theCube.rotate('ubUBULul')
                rotations.append('ubUBULul')
                cubeList = list(theCube.get())
                
                
            elif cubeList[UML] == FrontFace:
                theCube.rotate('UFufulUL')
                rotations.append('UFufulUL')
                cubeList = list(theCube.get())
                
                
            
   
    return "".join(rotations)       
