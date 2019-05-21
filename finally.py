print ("Iniciado o processo!")
try:
    f = open("myfile.txt", 'r')
except IOError:
    print ('cannot open')
else:
    print (arg, 'has', len(f.readlines()), 'lines')
    f.close()
finally:
    print ("Finalizado o processo!")
