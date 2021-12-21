import cv2 as cv
import numpy as np
import argparse
from matplotlib import pyplot as plt

def main(args):
    for j in range(0, 9):
        pruebasIndex = j+1
        path = 'pruebas' + str(pruebasIndex) + '/'
        forge = args.forge

        print('Carpeta pruebas ' + str(pruebasIndex))

        # Leemos imagen query
        forgename = path + str(forge) + '.png'

        # Cargamos la imagen
        img_forg = cv.imread(forgename)

        # Comprobamos que la imagen se ha podido leer
        if img_forg is None:
            print('Error al cargar la imagen falsificada')
            quit()

        for i in range(0,5):
            realIndex = i+1
            # Ignoramos esta imagen si es la misma que la de referencia
            if (str(realIndex) != str(forge)):
                # Leemos la imagen
                realName = path + str(realIndex) + '.png'
            else:
                realName = path + 'forge' + '.png'
                
            img_real = cv.imread(realName)

            if img_real is None:
                print('Error al cargar la imagen real')
                quit()

            img_f = img_forg.copy()
            img_r = img_real.copy()

            gray_f= cv.cvtColor(img_f,cv.COLOR_BGR2GRAY)
            gray_r= cv.cvtColor(img_r,cv.COLOR_BGR2GRAY)

            sift = cv.SIFT_create()

            # Usamos SIFT para detectar los keypoints y calcular sus descriptores
            keypoints_f, descriptors_f = sift.detectAndCompute(gray_f, None)
            keypoints_r, descriptors_r = sift.detectAndCompute(gray_r, None)
            
            #BFMatcher with default params
            matcher = cv.BFMatcher()

            matches = matcher.knnMatch(descriptors_f, descriptors_r, k=2)

            # Nos quedamos sólo los matches "buenos" y los guardamos en good
            # En el artículo original de SIFT, si dos puntos tienen una distancia menor de 0.7 se consideran un match
            good = []
            for m, n in matches:
                if m.distance < 0.7 * n.distance:
                    good.append(m)

            print('Número de matches buenos encontrados:', len(good))
            
            # Dibujamos el resultado
            draw_params = dict(matchColor = (0,255,0), singlePointColor = (255,0,0))

            imageMatches = cv.drawMatches(img_forg, keypoints_f, img_real, keypoints_r, good, None, **draw_params)

            #plt.imshow(imageMatches)
            #plt.show()

        input()

        #cv.waitKey(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Pruebas')
    parser.add_argument('--forge', '-f', type=str, default = '1')
    args = parser.parse_args()
    main(args)