import cv2

#acessa a câmera de vídeo do computador
#argumento 0 indica que a primeira câmera disponível no dispositivo será acessada
webcam  = cv2.VideoCapture(0)

#teste de conexão com a camera
if webcam.isOpened():
    #enquanto validacao retornar True, o laço continuara rodando
    validacao, frame = webcam.read()
    while validacao:
        validacao, frame = webcam.read()
        #imshow exibe a captura
        cv2.imshow("Video da Webcam", frame)

        #O método waitKey(5) exibe a captura em uma janela e garante que o quadro
        #seja exibido por um tempo de (5) milissegundos para a próxima captura de quadro.
        #Além disso, o método retorna as teclas pressionadas pelo usuário, permitindo controlar a captura de vídeo.
        key = cv2.waitKey(5)
        if key == 27: #ESC
            break


webcam.release()
cv2.destroyAllWindows()