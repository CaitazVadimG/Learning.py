X, Y, Z = 42, 404, 415
S = 'Spectral'
D = {'a': 2, 'b': 14}
L = [1, 22, 333]
F = open('datafile.txt', 'w')
F.write(S + '\n')
F.write('{0},{1},{2}\n'.format(X, Y, Z))
F.write(str(L) + '$' + str(D) + '\n')
F.close()
