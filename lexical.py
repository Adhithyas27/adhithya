def Lexo(my_string):
    words = my_string.split()
    words.sort()
    for i in words:
        print( i )
if __name__ == '__main__':
     my_string = "python class is ver drowsy"\
     "we need sleep"
Lexo(my_string)
