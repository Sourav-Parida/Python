#Program to calculate bill amount inclusive of GST
choice = 'y'
total = 0.0
while choice == 'y' or choice == 'Y':    #This loop shall executes as per user's choice till y is entered
    item_price = int(input("Enter the item price : "))
    gst = int(input("Enter the GST on the item : "))
    total =total+(item_price + (item_price*gst)/100)
    choice= input("Press y to continue else press any other key :")
print("Total amount to be paid = ",total)







    
    
