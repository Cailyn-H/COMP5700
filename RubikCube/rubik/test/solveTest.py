from unittest import TestCase
from rubik.view.solve import solve
from pickle import NONE


class SolveTest(TestCase):
        
# Happy path
#    Test that the stubbed solve returns the correct result
    
    
    def test110_solve_returnEmptySolution(self):
        parms = {}
        parms['cube'] = 'rrrrrrrrrgggggggggbbbbbbbbboooooooooyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        
    
    def test120_solve_returnSolution(self):
        parms = {}
        parms['cube'] = '3athhaa3a4th437t737h7aa3taahhhh474t34t34t3tth77447473a'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
    
    
    def test130_solve_returnSolution(self):
        parms = {}
        parms['cube'] = 'KK0yJ0PJyJJyPP0PyKKJJFFF0FF0PFPKPPK0PKJJy0yyKFyJ00FyKF'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)  
    '''
    def test140_missingCube(self):
        parms = {}
        parms['cube'] = None 
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: ', result['status'])


    def test150_illigalCube(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyy*********'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: ', result['status'])
        
    
    def test160_multiOccurenceOfLegalChar(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwwb'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: ', result['status'])
        
    
    def test170_nonUniqueMiddleElement(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbrrrrbrrrrooooboooogggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: ', result['status'])
        
    def test180_tooLongCube(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwwwkkkkkkkkk'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: ', result['status'])
    
    '''
