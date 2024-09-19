import cv2
import cv2.data

video = cv2.VideoCapture(0)

while True:
   successs, frame,= video.read()
   successs, frame = video.read()
   gray_image = cv2.cvtColor(frame,cv2.COLOR_BGRA2GRAY)
   face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
   face = face_classifier.detectMultiScale(gray_image, scaleFactor=1.1,minNeighbors=5,minSize=(200, 200))
   for (x,y,w,h) in face:
      cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),5)
      #blur = cv2.blur(frame[y:y+h,x:x+w],ksize=(50,50))
      #frame[y:y+h,x:x+w] = blur
   cv2.imshow('frame',frame)
   key = cv2.waitKey(1)
   if key != -1:
         break
video.release()
cv2.destroyAllWindows()

#cv2.VideoCapture(0): Otwiera strumień wideo z domyślnej kamery (zazwyczaj kamera internetowa komputera).
#while True:: Rozpoczyna nieskończoną pętlę, która będzie trwała do momentu jej przerwania.
#successs, frame = video.read(): Odczytuje pojedynczą klatkę z wideo. successs jest wartością logiczną, która wskazuje, czy odczyt się powiódł,
#a frame zawiera odczytaną klatkę obrazu.
#cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY): Konwertuje klatkę z formatu kolorowego (BGRA) na obraz w skali szarości.
# Wykrywanie twarzy działa lepiej na obrazach w skali szarości.
# cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'):
# Ładuje predefiniowany klasyfikator Haar do wykrywania twarzy.
# face_classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(200, 200)): Wykrywa twarze w obrazie w skali szarości.
# scaleFactor=1.1: Określa, jak bardzo obraz jest zmniejszany przy każdym przeskalowaniu.
# minNeighbors=5: Określa, ile sąsiednich prostokątów musi zostać wykrytych, aby mogły zostać uznane za twarz.
# minSize=(200, 200): Określa minimalny rozmiar prostokąta wykrywającego twarz.
#for (x, y, w, h) in face:: Iteruje przez wszystkie wykryte twarze.
#cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3):
# Rysuje zielony prostokąt o grubości 3 pikseli wokół każdej wykrytej twarzy na oryginalnej klatce.
#cv2.imshow('Video', frame): Wyświetla aktualną klatkę w oknie o nazwie "Video".
#key = cv2.waitKey(1): Oczekuje na naciśnięcie klawisza przez 1 milisekundę.
#if key != -1:: Sprawdza, czy jakikolwiek klawisz został naciśnięty.
#video.release(): Zamyka strumień wideo i zwalnia zasoby.
#cv2.destroyAllWindows(): Zamyka wszystkie okna utworzone przez OpenCV.