D = {'First': 'S', 'Second': 'S'}
F = open('datafile2.txt', 'wb')
import pickle
pickle.dump(D, F)
F.close()
