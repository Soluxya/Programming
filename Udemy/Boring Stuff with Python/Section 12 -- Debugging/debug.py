def boxPrint( symbol, width, height ):
    """
    This is to show the capabilities of the raise and assert Statements
    """
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1.')
    if (width<2) or (height <2):
        raise Exception('"width" and "height" must be greater or equal to 2')
    print( symbol  *  width  )
    for i in range( height  -  2 ):
        print( symbol  +  ( ' '  *  ( width - 2 ) )   +  symbol)
        
    print(symbol * width)

boxPrint( '*', 15, 5 )
def blah():
     """
     docstring
     """
     print("blah")
     pass   
blah()

import random
def headRandom():
    """
    docstring
    """
    heads = 0
    for i in range(1, 1001):
        if random.randint(0,1) == 1:
            heads += 1
        if i == 500:
            print('Halfway Done!')
            
    print(f'Heads came up {heads} times.')
    pass
headRandom()