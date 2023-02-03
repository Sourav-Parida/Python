#Program to write dictionary to a binary file
import pickle
dict1 = {'Python': 90, 'Java': 95, 'C++': 85}
f = open('bin_file.dat','wb')
pickle.dump(dict1,f)
f.close()






