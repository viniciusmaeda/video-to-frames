# importação da bibliote opencv
import cv2 as cv

# abre o vídeo presente na pasta
cap = cv.VideoCapture("./video/video.mp4")

# índice para nomear os arquivos dos frames
idx = 0

# laço para percorrer cada frame do vídeo
while True:
  # obtém o frame
  ret, frame = cap.read()

  # qndo não houver mais frame, interrompe o laço
  if ret == False:
    cap.release()
    break

  # salva o arquivo da imagem (frame)
  cv.imwrite(f"saved/frame_{idx}.png", frame)

  # incrementa o índice
  idx += 1

  print(idx)

