#!/usr/bin/python3
import sys
import os
import math
import unicodedata as ud

if len(sys.argv) != 2:
    print("Error: entropia.py [directorio]")
    sys.exit()


directory=sys.argv[1]
results=[]
target = ''
# Iteramos sobre los ficheros del directorio(srting) dado como parametro
# y calculamos la entropia de Shannon de cada uno
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        target = (os.path.join(directory, filename))
        byteArray=[]
        
        # Lectura del fichero en un array de bytes
        with open(target, "rb") as f:
            while (byte := f.read(1)):
                byteArray.append(byte)

        f.close()
        fileSize = len(byteArray)

        print(f'{target} bytes size:', str(fileSize))
        print()

        # Calculo de frecuencia de cada byte
        freqList = []
        for b in range(256):
            ctr = 0
            for byte in byteArray:   
                if ord(byte) == b:
                    ctr += 1
            freqList.append(float(ctr) / fileSize)

        # Entropia de Shannon
        ent = 0.0
        for freq in freqList:
            if freq > 0:
                ent = ent + freq * math.log(freq, 2)
        ent = -ent

        results.append({'file': target, 'value': ent})

        print('Entropia:', str(ent))
        print('*********************************')

final={'file': '', 'value': 0.0}
for result in results:
    if(result['value'] > final['value']):
        final = result

print('Ganador: ', final)
print('*********************************')
print('*********************************')  