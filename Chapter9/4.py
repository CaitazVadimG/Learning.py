import pickle
F = open("datafile2.txt",'rb')
E = pickle.load(F)
print("E = {0}".format(E))
