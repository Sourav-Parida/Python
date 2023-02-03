def test1():
    A={1:"one",2:"two",3:"three"}
    print (A)
def test2():
    H={'Four': 'scanner', 'three': 'printer', 'two': 'Mouse', 'one': 'keyboard'}
    for i in H:
        print (i,":", H[i],"")
def test3():
    H = {'Four': 'scanner', 'three': 'printer', 'two': 'Mouse', 'one': 'keyboard'}
    print ("i value","\t","H[i] value")
    for i in H:
        print (i,"\t", H[i])
#Creating, initializing values during run time (Dynamic allocation)
def test4():
    classxi=dict()
    f = input("Enter total number of section in xi class-")
    f =int(f)
    x = 1
    while (x <= f):
        a=input("enter section name ---")
        b=input ("enter class teacher name---")
        classxi[a]=b
        x=x+1
    print ("Class","\t","Section","\t","teacher name")
    for x in classxi:
        print ("XI","\t",x,"\t",classxi[x])
def test5():
    a={"mon":"monday","tue":"tuesday","wed":"wednesday"}
    a["thu"]="thursday"
    print (a)
def test6():
    d1={1:10,2:20,3:30}
    d2={4:40,5:50}
    d1.update(d2)
    print (d1)
def test7():
    A={"mon":"monday","tue":"tuesday","wed":"wednesday","thu":"thursday"}
    del A["tue"]
    print (A)
'''cmp ( )
This is used to check whether the given dictionaries are same or not. If both are same, it
will return ‘zero’, otherwise return 1 or -1.'''
def test8():    
    D1={'sun':'Sunday','mon':'Monday','tue':'Tuesday','wed':'Wednesday','thu':'Thursday','fri':'Friday','sat':'Saturday'}
    D2={'sun':'Sunday','mon':'Monday','tue':'Tuesday','wed':'Wednesday','thu':'Thursday','fri':'Friday','sat':'Saturday'}
    D3={'mon':'Monday','tue':'Tuesday','wed':'Wednesday'}
    #print(D1==D3) #both are not equal
    #print(D1==D2) #both are equal
    print(cmp(D3,D1))
def test9():
    H={'Four': 'scanner', 'three': 'printer', 'two': 'Mouse', 'one': 'keyboard'}
    print(len(H))
def test10():
    D={'mon':'Monday','tue':'Tuesday','wed':'Wednesday'}
    print (D)
    {'wed': 'Wednesday', 'mon': 'Monday', 'tue': 'Tuesday'}
    D.clear()
    print (D)
def test11():
    D={'sun':'Sunday','mon':'Monday','tue':'Tuesday','wed':'Wednesday','thu':'Thursday','fri':'Friday','sat':'Saturday'}
    print(D.get('wed',"wednesday"))
    print(D.get("fri","monday"))
    print(D.get("mon"))
    print(D.get("ttu"))
def test12():
    D={'sun':'Sunday','mon':'Monday','tue':'Tuesday','wed':'Wednesday','thu':'Thursday','fri':'Friday','sat':'Saturday'}
    print(D.has_key("fri"))
    print(D.has_key("aaa"))
def test13():
    D={'sun':'Sunday','mon':'Monday','tue':'Tuesday','wed':'Wednesday','thu':'Thursday','fri':'Friday','sat':'Saturday'}
    print(D.items())
def test14():
    D={'sun':'Sunday','mon':'Monday','tue':'Tuesday','wed':'Wednesday','thu':'Thursday','fri':'Friday','sat':'Saturday'}
    print(D.keys())
def test15():
    D={'sun':'Sunday','mon':'Monday','tue':'Tuesday','wed':'Wednesday','thu':'Thursday','fri':'Friday','sat':'Saturday'}
    print(D.values())



    
