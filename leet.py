from pprint import pprint
from random import randrange


class Diccionario:
    def __init__(self):
        self.letras = {
            'a':[[52], [47, 92], [64], [47, 45, 92], [94], [97, 121, 101], [40, 76], [1044, 93]],
            'b':[[73, 51], [56], [49, 51], [124, 51], [223], [33, 51], [40, 51], [47, 51], [41, 51], [124, 45, 93], [106, 51], [54]],
            'c':[[91], [162], [123], [60], [40], [169]],
            'd':[[41], [124, 41], [40, 124], [91, 41], [73, 62], [124, 62], [63], [84, 41], [73, 55], [99, 108], [124, 125], [62], [124, 93]],
            'e':[[51], [38], [163], [8364], [235], [91, 45], [124, 61, 45]],
            'f':[[124, 61], [402], [124, 35], [112, 104], [47, 61], [118]],
            'g':[[38], [54], [40, 95, 43], [57], [67, 45], [103, 101, 101], [40, 63, 44], [91, 44], [123, 44], [60, 45], [40, 46]],
            'h':[[35], [47, 45, 47], [91, 45, 93], [93, 45, 91], [41, 45, 40], [40, 45, 41], [58, 45, 58], [124, 126, 124], [124, 45, 124], [93, 126, 91], [125, 123], [33, 45, 33], [49, 45, 49], [92, 45, 47], [73, 43, 73], [47
            , 45, 92]],
            'i':[[49], [91, 93], [124], [33], [101, 121, 101], [51, 121, 51], [93, 91]],
            'j':[[44, 95, 124], [95, 124], [46, 95, 124], [46, 95, 93], [95, 93], [44, 95, 93], [93], [59], [49]],
            'k':[[62, 124], [124, 60], [47, 60], [49, 60], [124, 99], [124, 40], [124, 123]],
            'l':[[49], [163], [55], [124, 95], [124]],
            'm':[[47, 92, 47, 92], [47, 86, 92], [74, 86, 73], [91, 86, 93], [91, 93, 86, 91, 93], [124, 92, 47, 124], [94, 94], [60, 92, 47, 62], [123, 86, 125], [40, 118, 41], [40, 86, 41], [124, 86, 124], [110, 110], [73, 86, 73], [124, 92, 124, 92], [93, 92, 47, 91], [49, 94, 49], [73, 84, 73], [74, 84, 73]],
            'n':[[94, 47], [124, 92, 124], [47, 92, 47], [91, 92, 93], [60, 92, 62], [123, 92, 125], [124, 86], [47, 86], [1048], [94], [3607]],
            'o':[[48], [81], [40, 41], [111, 104], [91, 93], [112], [60, 62], [216]],
            'p':[[124, 42], [124, 111], [124, 186], [63], [124, 94], [124, 62], [124, 34], [57], [91, 93, 68], [124, 176], [124, 55]],
            'q':[[40, 95, 44, 41], [57], [40, 41, 95], [50], [48, 95], [60, 124], [38]],
            'r':[[73, 50], [124, 96], [124, 126], [124, 63], [47, 50], [124, 94], [108, 122], [124, 57], [50], [49, 50], [174], [91, 122], [1071, 175], [46, 45], [124, 50], [124, 45]],
            's':[[53], [36], [122], [167], [101, 104, 115], [101, 115], [50]],
            't':[[55], [43], [45, 124, 45], [39, 93, 91, 39], [8224], [34, 124, 34], [126, 124, 126]],
            'u':[[40, 95, 41], [124, 95, 124], [118], [76, 124], [181], [3610]],
            'v':[[92, 47], [124, 47], [92, 124]],
            'w':[[92, 47, 92, 47], [86, 86], [92, 78], [39, 47, 47], [92, 92, 39], [92, 94, 47], [40, 110, 41], [92, 86, 47], [92, 88, 47], [92, 124, 47], [92, 95, 124, 95, 47], [92, 95, 58, 95, 47], [1064, 168], [1065], [117,
            117], [50, 117], [92, 92, 47, 47, 92, 92, 47, 47], [3614], [118, 178]],
            'x':[[62, 60], [1046], [125, 123], [101, 99, 107, 115], [215], [63], [41, 40], [93, 91]],
            'y':[[106], [96, 47], [1063], [55], [92, 124, 47], [165], [92, 47, 47]],
            'z':[[50], [55, 95], [45, 47, 95], [37], [62, 95], [115], [126, 47, 95], [45, 92, 95], [45, 124, 95]]
        }

    def encode(self, palabra, con_espacio=False):
        pal = palabra.lower().strip()
        res = []
        sep = ' ' if con_espacio else ''
        for letra in pal:
            if letra in self.letras.keys():
                lista = self.letras.get(letra)
                elegido = lista[randrange(0, len(lista))]
                salida = ''.join(list(map(chr, elegido)))
            else:
                salida = letra
            res.append(salida)
        return sep.join(res)
    
if __name__=="__main__":
    dic = Diccionario()
    # res = dic.encode('Si puedes leer esto, ¡realmente necesitas tener una vida!')
    res = dic.encode('Mira cómo escribo leet')
    print(res)