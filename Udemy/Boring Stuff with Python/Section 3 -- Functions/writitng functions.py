def hello(to_print):
        """
        This function prints the paramater
        """
        print('Hello ' + to_print)
    

hello("Alice")

def length(to_object_length):
        """
        This function retruns a string which tells how many characters 
        there are in your string.
        """
        object_length = str(len(to_object_length))
        print(to_object_length + ' has ' + object_length + ' letters in it')

length("Hi")

def plusOne(integer_to_parse):
        """
        Adds + 1 to value
        """
        if isinstance(integer_to_parse, int) or isinstance(integer_to_parse, float):
                print(integer_to_parse + 1)
        else:
                print("You didn't put an Integer")

plusOne(5)
