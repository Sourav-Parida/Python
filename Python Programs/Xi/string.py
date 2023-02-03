def test1():                    #String Literals
    print("Hello")
    print('Hello')
def test2():                    #Assign String to a Variable
    a = "Hello"
    print(a)
def test3():                    #Multiline Strings
    a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
    print(a)
    b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
    print(b)
def test4():                    #Strings are Arrays
    a = "Hello, World!"
    print(a[1])
def test5():                    #Slicing
    b = "Hello, World!"
    print(b[2:5])
def test6():                    #Negative Indexing   #Slicing
    b = "Hello, World!"
    print(b[-5:-2])
def test7():                    #String Length
    a = "Hello, World!"
    print(len(a))
'''strip() method removes any whitespace from the beginning or end'''
def test8():    
    a = "    Hello, World!    "
    print(a.strip())         
'''lower() method returns the string in lower case'''
def test9():
    a = "Hello, World!"
    print(a.lower())
'''upper() method returns the string in upper case:'''
def test10():
    a = "Hello, World!"
    print(a.upper())
'''replace() method replaces a string with another string'''
def test11():
    a = "Hello, World!"
    print(a.replace("H", "J"))
'''split() method splits the string into substrings if it finds instances of the separator'''
def test12():
    a = "Hello, World!"
    print(a.split(","))




