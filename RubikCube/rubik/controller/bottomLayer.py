from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the bottom layer is solved.
        
        input:  an instance of the cube class with the down-face cross solved
        output: the rotations required to solve the bottom layer  
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
    #           Checking for Perfect Down Face              #
    #             Before Starting a Rotation                #
    #########################################################
    if (cubeList[DTL] == DownFace and cubeList[FBL] == FrontFace and cubeList[DTR] == DownFace and cubeList[RBL] == RightFace and cubeList[BBR] == BackFace and cubeList[DBL] == DownFace and cubeList[DBR] == DownFace):
        return "".join(rotations)
    
    
    
    
    
    
    #########################################################
    #                                                       #
    #             Start Rotating for Down Face              #
    #                                                       #
    #########################################################       
    while (cubeList[DTL]!=DownFace or cubeList[DTR]!=DownFace or cubeList[DBL]!=DownFace or cubeList[DBR]!=DownFace):
        
        #########################################################
        #                                                       #
        #            Checking for Edges on Down Face            #
        #                                                       #
        #########################################################
        
        while ((cubeList[DTL]==DownFace and cubeList[FBL]!=FrontFace) or (cubeList[DTR]==DownFace and cubeList[RBL]!=RightFace) or (cubeList[DBL]==DownFace and cubeList[LBL]!=LeftFace) or (cubeList[DBR]==DownFace and cubeList[BBL]!=BackFace)) or (cubeList[FBL]==DownFace or cubeList[FBR]==DownFace or cubeList[RBL]==DownFace or cubeList[RBR]==DownFace or cubeList[BBL]==DownFace or cubeList[BBR]==DownFace or cubeList[LBL]==DownFace or cubeList[LBR]==DownFace):
            
            if cubeList[DTL] == DownFace:
                if cubeList[FBL] != FrontFace:
                    theCube.rotate('lUL')
                    rotations.append('lUL')
                    cubeList = list(theCube.get())
                    
                    
            if cubeList[DTR] == DownFace:
                if cubeList[FBR] != FrontFace:
                    theCube.rotate('Rur')
                    rotations.append('Rur')
                    cubeList = list(theCube.get())
                    
                    
            if cubeList[DBL] == DownFace:
                if cubeList[LBL] != LeftFace:
                    theCube.rotate('bUB')
                    rotations.append('bUB')
                    cubeList = list(theCube.get())
                    
            if cubeList[DBR] == DownFace:
                if cubeList[RBR] != RightFace:
                    theCube.rotate('BUb')
                    rotations.append('BUb')
                    cubeList = list(theCube.get())
                    
                    
            if cubeList[FBL] == DownFace:
                theCube.rotate('FUfu')
                rotations.append('FUfu')
                cubeList = list(theCube.get())
                
               
            if cubeList[FBR] == DownFace:
                theCube.rotate('fUFu')
                rotations.append('fUFu')
                cubeList = list(theCube.get())
                
            if cubeList[RBL] == DownFace:
                theCube.rotate('RUru')
                rotations.append('RUru')
                cubeList = list(theCube.get())
                
            if cubeList[RBR] == DownFace:
                theCube.rotate('rURu')
                rotations.append('rURu')
                cubeList = list(theCube.get())
                
                
            if cubeList[BBL] == DownFace:
                theCube.rotate('BUbu')
                rotations.append('BUbu')
                cubeList = list(theCube.get())
                
            if cubeList[BBR] == DownFace:
                theCube.rotate('bUBu')
                rotations.append('bUBu')
                cubeList = list(theCube.get())
                
            if cubeList[LBL] == DownFace:
                theCube.rotate('LUlu')
                rotations.append('LUlu')
                cubeList = list(theCube.get())
                
                
            if cubeList[LBR] == DownFace:
                theCube.rotate('lULu')
                rotations.append('lULu')
                cubeList = list(theCube.get())  
                
        '''       
        #########################################################
        #                                                       #
        # checking for Edges on Bottom Layer but not Down Face  #
        #                                                       #
        #########################################################
        while (cubeList[FBL]==DownFace or cubeList[FBR]==DownFace or cubeList[RBL]==DownFace or cubeList[RBR]==DownFace or cubeList[BBL]==DownFace or cubeList[BBR]==DownFace or cubeList[LBL]==DownFace or cubeList[LBR]==DownFace):
            
            if cubeList[FBL] == DownFace:
                theCube.rotate('FUfu')
                rotations.append('FUfu')
                cubeList = list(theCube.get())
               
            elif cubeList[FBR] == DownFace:
                theCube.rotate('fUFu')
                rotations.append('fUFu')
                cubeList = list(theCube.get())
                
            elif cubeList[RBL] == DownFace:
                theCube.rotate('RUru')
                rotations.append('RUru')
                cubeList = list(theCube.get())
                print(theCube.get())
                
            elif cubeList[RBR] == DownFace:
                theCube.rotate('rURu')
                rotations.append('rURu')
                cubeList = list(theCube.get())
                print(theCube.get())
                
            elif cubeList[BBL] == DownFace:
                theCube.rotate('BUbu')
                rotations.append('BUbu')
                cubeList = list(theCube.get())
                
            elif cubeList[BBR] == DownFace:
                theCube.rotate('bUBu')
                rotations.append('bUBu')
                cubeList = list(theCube.get())
                
            elif cubeList[LBL] == DownFace:
                theCube.rotate('LUlu')
                rotations.append('LUlu')
                cubeList = list(theCube.get())
                print(theCube.get())
                print('q')
                
            elif cubeList[LBR] == DownFace:
                theCube.rotate('lULu')
                rotations.append('lULu')
                cubeList = list(theCube.get())   
        '''   
        #########################################################
        #                                                       #
        #                   Edge on Up Face                     #
        #                                                       #
        #########################################################
        if cubeList[UBL] == DownFace:
            if cubeList[FTL] == FrontFace:
                theCube.rotate('u')
                rotations.append('u')
                cubeList = list(theCube.get())
                while (cubeList[DTR] != DownFace or cubeList[FBR] != FrontFace):
                    theCube.rotate('fuFU')
                    rotations.append('fuFU')
                    cubeList = list(theCube.get())
                
            elif cubeList[FTL] == RightFace:
                theCube.rotate('uu')
                rotations.append('uu')
                cubeList = list(theCube.get())
                while (cubeList[DBR] != DownFace or cubeList[RBR] != RightFace):
                    theCube.rotate('ruRU')
                    rotations.append('ruRU')
                    cubeList = list(theCube.get())
                    
            elif cubeList[FTL] == BackFace:
                theCube.rotate('U')
                rotations.append('U')
                cubeList = list(theCube.get())
                while (cubeList[DBL] != DownFace or cubeList[BBR] != BackFace):
                    theCube.rotate('buBU')
                    rotations.append('buBU')
                    cubeList = list(theCube.get())
                    
            elif cubeList[FTL] == LeftFace:
                while (cubeList[DTL] != DownFace or cubeList[LBR] != LeftFace):
                    theCube.rotate('luLU')
                    rotations.append('luLU')
                    cubeList = list(theCube.get())
                    
        if cubeList[UBR] == DownFace:
            if cubeList[FTR] == FrontFace and cubeList[RTL] == LeftFace:
                theCube.rotate('U')
                rotations.append('U')
                cubeList = list(theCube.get())
                while (cubeList[DTL] != DownFace or cubeList[LBR] != LeftFace):
                    theCube.rotate('luLU')
                    rotations.append('luLU')
                    cubeList = list(theCube.get())
                    
            elif cubeList[FTR] == LeftFace and cubeList[RTL] == BackFace:
                theCube.rotate('UU')
                rotations.append('UU')
                cubeList = list(theCube.get())
                while (cubeList[DBL] != DownFace or cubeList[BBR] != BackFace):
                    theCube.rotate('buBU')
                    rotations.append('buBU')
                    cubeList = list(theCube.get())
                
            elif cubeList[FTR] == BackFace and cubeList[RTL] == RightFace:
                theCube.rotate('u')
                rotations.append('u')
                cubeList = list(theCube.get())
                while (cubeList[DBR] != DownFace or cubeList[RBR] != RightFace):
                    theCube.rotate('ruRU')
                    rotations.append('ruRU')
                    cubeList = list(theCube.get())
                 
                   
            elif cubeList[FTR] == RightFace and cubeList[RTL] == FrontFace:
                while (cubeList[DTR] != DownFace or cubeList[FBR] != FrontFace):
                    theCube.rotate('fuFU')
                    rotations.append('fuFU')
                    cubeList = list(theCube.get())
                    
        if cubeList[UTL] == DownFace:
            if cubeList[BTR] == BackFace:
                theCube.rotate('U')
                rotations.append('U')
                cubeList = list(theCube.get())
                while (cubeList[DBR] != DownFace or cubeList[RBR] != RightFace):
                    theCube.rotate('ruRU')
                    rotations.append('ruRU')
                    cubeList = list(theCube.get())
                
            elif cubeList[BTR] == RightFace:
                theCube.rotate('UU')
                rotations.append('UU')
                cubeList = list(theCube.get())
                
                while (cubeList[DTR] != DownFace or cubeList[FBR] != FrontFace):
                    theCube.rotate('fuFU')
                    rotations.append('fuFU')
                    cubeList = list(theCube.get())
                    
            elif cubeList[BTR] == FrontFace:
                theCube.rotate('u')
                rotations.append('u')
                cubeList = list(theCube.get())
                while (cubeList[DTL] != DownFace or cubeList[LBR] != LeftFace):
                    theCube.rotate('luLU')
                    rotations.append('luLU')
                    cubeList = list(theCube.get())
                    
            elif cubeList[BTR] == LeftFace:
                while (cubeList[DBL] != DownFace or cubeList[BBR] != BackFace):
                    theCube.rotate('buBU')
                    rotations.append('buBU')
                    cubeList = list(theCube.get())
                    
        if cubeList[UTR] == DownFace:
            if cubeList[BTL] == BackFace:
                theCube.rotate('u')
                rotations.append('u')
                cubeList = list(theCube.get())
                while (cubeList[DBL] != DownFace or cubeList[BBR] != BackFace):
                    theCube.rotate('buBU')
                    rotations.append('buBU')
                    cubeList = list(theCube.get())
                
            elif cubeList[BTL] == LeftFace:
                theCube.rotate('uu')
                rotations.append('uu')
                cubeList = list(theCube.get())
                while (cubeList[DTL] != DownFace or cubeList[LBR] != LeftFace):
                    theCube.rotate('luLU')
                    rotations.append('luLU')
                    cubeList = list(theCube.get())
                    
            elif cubeList[BTL] == FrontFace:
                theCube.rotate('U')
                rotations.append('U')
                cubeList = list(theCube.get())
                while (cubeList[DTR] != DownFace or cubeList[FBR] != FrontFace):
                    theCube.rotate('fuFU')
                    rotations.append('fuFU')
                    cubeList = list(theCube.get())
                    
            elif cubeList[BTL] == RightFace:
                while (cubeList[DBR] != DownFace or cubeList[RBR] != RightFace):
                    theCube.rotate('ruRU')
                    rotations.append('ruRU')
                    cubeList = list(theCube.get())
                
        #########################################################
        #                                                       #
        #                  Edge on Front Face                   #
        #                                                       #
        #########################################################
        
        if cubeList[FTL] == DownFace:
            if cubeList[UBL] == RightFace:
                theCube.rotate('u')
                rotations.append('u')
                cubeList = list(theCube.get())
                while (cubeList[DTR] != DownFace or cubeList[FBR] != FrontFace):
                    theCube.rotate('fuFU')
                    rotations.append('fuFU')
                    cubeList = list(theCube.get())
                
            elif cubeList[UBL] == BackFace:
                theCube.rotate('uu')
                rotations.append('uu')
                cubeList = list(theCube.get())
                while (cubeList[DBR] != DownFace or cubeList[RBR] != RightFace):
                    theCube.rotate('ruRU')
                    rotations.append('ruRU')
                    cubeList = list(theCube.get())
                
                
            elif cubeList[UBL] == LeftFace:
                theCube.rotate('U')
                rotations.append('U')
                cubeList = list(theCube.get())
                while (cubeList[DBL] != DownFace or cubeList[BBR] != BackFace):
                    theCube.rotate('buBU')
                    rotations.append('buBU')
                    cubeList = list(theCube.get())
                
            elif cubeList[UBL] == FrontFace:
                while (cubeList[DTL] != DownFace or cubeList[LBR] != LeftFace):
                    theCube.rotate('luLU')
                    rotations.append('luLU')
                    cubeList = list(theCube.get())
                
        if cubeList[FTR] == DownFace:
            if cubeList[UBR] == RightFace:
                theCube.rotate('u')
                rotations.append('u')
                cubeList = list(theCube.get())
                while (cubeList[DBR] != DownFace or cubeList[RBR] != RightFace):
                    theCube.rotate('ruRU')
                    rotations.append('ruRU')
                    cubeList = list(theCube.get())
                
            elif cubeList[UBR] == BackFace:
                theCube.rotate('uu')
                rotations.append('uu')
                cubeList = list(theCube.get())
                while (cubeList[DBL] != DownFace or cubeList[BBR] != BackFace):
                    theCube.rotate('buBU')
                    rotations.append('buBU')
                    cubeList = list(theCube.get())
                    
            elif cubeList[UBR] == LeftFace:
                theCube.rotate('U')
                rotations.append('U')
                cubeList = list(theCube.get())
                while (cubeList[DTL] != DownFace or cubeList[LBR] != LeftFace):
                    theCube.rotate('luLU')
                    rotations.append('luLU')
                    cubeList = list(theCube.get())
                    
            elif cubeList[UBR] == FrontFace:
                while (cubeList[DTR] != DownFace or cubeList[FBR] != FrontFace):
                    theCube.rotate('fuFU')
                    rotations.append('fuFU')
                    cubeList = list(theCube.get())
                
        #########################################################
        #                                                       #
        #                  Edge on Right Face                   #
        #                                                       #
        #########################################################           
        if cubeList[RTL] == DownFace:
            if cubeList[UBR] == BackFace:
                theCube.rotate('u')
                rotations.append('u') 
                cubeList = list(theCube.get())
                while (cubeList[DBR] != DownFace or cubeList[RBR] != RightFace):
                    theCube.rotate('ruRU')
                    rotations.append('ruRU')
                    cubeList = list(theCube.get())
                
            elif cubeList[UBR] == LeftFace:
                theCube.rotate('uu')
                rotations.append('uu')
                cubeList = list(theCube.get())
                while (cubeList[DBL] != DownFace or cubeList[BBR] != BackFace):
                    theCube.rotate('buBU')
                    rotations.append('buBU')
                    cubeList = list(theCube.get())
                    
            elif cubeList[UBR] == FrontFace:
                theCube.rotate('U')
                rotations.append('U')
                cubeList = list(theCube.get())
                while (cubeList[DTL] != DownFace or cubeList[LBR] != LeftFace):
                    theCube.rotate('luLU')
                    rotations.append('luLU')
                    cubeList = list(theCube.get())
                    
            elif cubeList[UBR] == RightFace:
                while (cubeList[DTR] != DownFace or cubeList[FBR] != FrontFace):
                    theCube.rotate('fuFU')
                    rotations.append('fuFU')
                    cubeList = list(theCube.get())
                
        if cubeList[RTR] == DownFace:
            if cubeList[UTR] == BackFace:
                theCube.rotate('u')
                rotations.append('u')
                cubeList = list(theCube.get())
                while (cubeList[DBL] != DownFace or cubeList[BBR] != BackFace):
                    theCube.rotate('buBU')
                    rotations.append('buBU')
                    cubeList = list(theCube.get())
                    
            elif cubeList[UTR] == LeftFace:
                theCube.rotate('uu')
                rotations.append('uu')
                cubeList = list(theCube.get())
                while (cubeList[DTL] != DownFace or cubeList[LBR] != LeftFace):
                    theCube.rotate('luLU')
                    rotations.append('luLU')
                    cubeList = list(theCube.get())
                    
            elif cubeList[UTR] == FrontFace:
                theCube.rotate('U')
                rotations.append('U')
                cubeList = list(theCube.get())
                while (cubeList[DTR] != DownFace or cubeList[FBR] != FrontFace):
                    theCube.rotate('fuFU')
                    rotations.append('fuFU')
                    cubeList = list(theCube.get())
                    
            elif cubeList[UTR] == RightFace:
                while (cubeList[DBR] != DownFace or cubeList[RBR] != RightFace):
                    theCube.rotate('ruRU')
                    rotations.append('ruRU')
                    cubeList = list(theCube.get())
        
        #########################################################
        #                                                       #
        #                   Edge on Back Face                   #
        #                                                       #
        #########################################################
        if cubeList[BTL] == DownFace:
            if cubeList[UTR] == LeftFace:
                theCube.rotate('u')
                rotations.append('u')
                cubeList = list(theCube.get())
                while (cubeList[DBL] != DownFace or cubeList[BBR] != BackFace):
                    theCube.rotate('buBU')
                    rotations.append('buBU')
                    cubeList = list(theCube.get())
                    
            elif cubeList[UTR] == FrontFace:
                theCube.rotate('uu')
                rotations.append('uu')
                cubeList = list(theCube.get())
                while (cubeList[DTL] != DownFace or cubeList[LBR] != LeftFace):
                    theCube.rotate('luLU')
                    rotations.append('luLU')
                    cubeList = list(theCube.get())
                    
            elif cubeList[UTR] == RightFace:
                theCube.rotate('U')
                rotations.append('U')
                cubeList = list(theCube.get())
                while (cubeList[DTR] != DownFace or cubeList[FBR] != FrontFace):
                    theCube.rotate('fuFU')
                    rotations.append('fuFU')
                    cubeList = list(theCube.get())
                
            elif cubeList[UTR] == BackFace:
                while (cubeList[DBR] != DownFace or cubeList[RBR] != RightFace):
                    theCube.rotate('ruRU')
                    rotations.append('ruRU')
                    cubeList = list(theCube.get())
                    
        if cubeList[BTR] == DownFace:
            if cubeList[UTL] == LeftFace:
                theCube.rotate('u')
                rotations.append('u')
                cubeList = list(theCube.get())
                while (cubeList[DTL] != DownFace or cubeList[LBR] != LeftFace):
                    theCube.rotate('luLU')
                    rotations.append('luLU')
                    cubeList = list(theCube.get())
                    
            elif cubeList[UTL] == FrontFace:
                theCube.rotate('uu')
                rotations.append('uu')
                cubeList = list(theCube.get())
                while (cubeList[DTR] != DownFace or cubeList[FBR] != FrontFace):
                    theCube.rotate('fuFU')
                    rotations.append('fuFU')
                    cubeList = list(theCube.get())
                    
            elif cubeList[UTL] == RightFace:
                theCube.rotate('U')
                rotations.append('U')
                cubeList = list(theCube.get())
                while (cubeList[DBR] != DownFace or cubeList[RBR] != RightFace):
                    theCube.rotate('ruRU')
                    rotations.append('ruRU')
                    cubeList = list(theCube.get())
                
            elif cubeList[UTL] == BackFace:
                while (cubeList[DBL] != DownFace or cubeList[BBR] != BackFace):
                    theCube.rotate('buBU')
                    rotations.append('buBU')
                    cubeList = list(theCube.get())
        
        #########################################################
        #                                                       #
        #                   Edge on Left Face                   #
        #                                                       #
        #########################################################
        if cubeList[LTL] == DownFace:
            if cubeList[UTL] == FrontFace:
                theCube.rotate('u')
                rotations.append('u')
                cubeList = list(theCube.get())
                while (cubeList[DTL] != DownFace or cubeList[LBR] != LeftFace):
                    theCube.rotate('luLU')
                    rotations.append('luLU')
                    cubeList = list(theCube.get())
                    
            elif cubeList[UTL] == RightFace:
                theCube.rotate('uu')
                rotations.append('uu')
                cubeList = list(theCube.get())
                while (cubeList[DTR] != DownFace or cubeList[FBR] != FrontFace):
                    theCube.rotate('fuFU')
                    rotations.append('fuFU')
                    cubeList = list(theCube.get())
                    
            elif cubeList[UTL] == BackFace:
                theCube.rotate('U')
                rotations.append('U')
                cubeList = list(theCube.get())
                while (cubeList[DBR] != DownFace or cubeList[RBR] != RightFace):
                    theCube.rotate('ruRU')
                    rotations.append('ruRU')
                    cubeList = list(theCube.get())
                    
            elif cubeList[UTL] == LeftFace:
                while (cubeList[DBL] != DownFace or cubeList[BBR] != BackFace):
                    theCube.rotate('buBU')
                    rotations.append('buBU')
                    cubeList = list(theCube.get())
                
        if cubeList[LTR] == DownFace:
            if cubeList[UBL] == FrontFace:
                theCube.rotate('u')
                rotations.append('u')
                cubeList = list(theCube.get())
                while (cubeList[DTR] != DownFace or cubeList[FBR] != FrontFace):
                    theCube.rotate('fuFU')
                    rotations.append('fuFU')
                    cubeList = list(theCube.get())
                    
            elif cubeList[UBL] == RightFace:
                theCube.rotate('uu')
                rotations.append('uu')
                cubeList = list(theCube.get())
                while (cubeList[DBR] != DownFace or cubeList[RBR] != RightFace):
                    theCube.rotate('ruRU')
                    rotations.append('ruRU')
                    cubeList = list(theCube.get())
                    
            elif cubeList[UBL] == BackFace:
                theCube.rotate('U')
                rotations.append('U')
                cubeList = list(theCube.get())
                while (cubeList[DBL] != DownFace or cubeList[BBR] != BackFace):
                    theCube.rotate('buBU')
                    rotations.append('buBU')
                    cubeList = list(theCube.get())
                    
            elif cubeList[UBL] == LeftFace:
                while (cubeList[DTL] != DownFace or cubeList[LBR] != LeftFace):
                    theCube.rotate('luLU')
                    rotations.append('luLU')
                    cubeList = list(theCube.get())
      
    
         
    return "".join(rotations)  
