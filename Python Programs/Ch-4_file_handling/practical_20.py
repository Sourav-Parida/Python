import pickle
f = open("student", "rb")
stud_rec = pickle.load(f) # To read the object from the opened file
print ("Contents of student file are:") #reading the fields from the file
for R in stud_rec:
    roll_no = R[0]
    name = R[1]
    marks = R[2]
    print(roll_no, name, marks)
f.close()
