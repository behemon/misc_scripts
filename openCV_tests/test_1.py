import time
import cv2
import mss
import numpy
import pytesseract
from PIL import Image


def main():
    tessdata_dir_config = '--tessdata-dir C:/Tesseract-OCR/tessdata'
    method = cv2.cv2.TM_CCOEFF_NORMED
    template = cv2.imread('car.png', 0)
    w, h = template.shape[::-1]
    with mss.mss() as sct:
        # Part of the screen to capture
        monitor = {'top': 40, 'left': 0, 'width': 800, 'height': 640}

        while 'Screen capturing':
            last_time = time.time()

            # Get raw pixels from the screen, save it to a Numpy array
            img = numpy.array(sct.grab(monitor))
            imgG = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # print pytesseract.image_to_string(img)
            # print pytesseract.image_to_string(img, config=tessdata_dir_config)
            # print(pytesseract.image_to_data(cv2.imread('car.png')))

            result = cv2.matchTemplate(imgG,template,method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            # print min_val, max_val, min_loc, max_loc

            threshold = 0.8
            loc = numpy.where(result >= threshold)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

            # Display the picture
            cv2.imshow('OpenCV/Numpy normal', img)


            # print('fps: {0}'.format(1 / (time.time() - last_time)))
            # Press "q" to quit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break


def test_OCR():
    tessdata_dir_config = '--tessdata-dir C:/Tesseract-OCR/tessdata'
    img = Image.open('./numbers.png')
    i = img.load()
    i = pytesseract.image_to_string(img , config=tessdata_dir_config)
    print i

if __name__ == '__main__':
    main()
    # test_OCR()