def div42by(divideBy):
    """
    Divide 42 by a parameter.
    """
    try:
       return 42 / divideBy
    except:
        print("Error! -- You tried to divide by Zero!")

print(div42by(0))