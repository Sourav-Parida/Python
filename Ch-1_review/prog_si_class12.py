#Program to calculate simple interest
Principal=eval(input("Enter the value of Principal:"))
Rate=eval(input("Enter the annual rate of interest:"))
Time=5
Simple_Int = Principal*Rate*Time/100
Amount = Principal+Simple_Int
print("Simple Interest = ",Simple_Int)
print("Amount payable = ",Amount)
