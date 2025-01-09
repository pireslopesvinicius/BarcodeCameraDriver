import cv2
import pyautogui
from PIL import Image
from pyzbar.pyzbar import decode
from timer import Timer

# Constants
IMG_TEMP_PATH = 'captura_temp.jpg'

# Variables
cap = cv2.VideoCapture(0)
picture_timer = Timer(1).start()


def analyse_camera():
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error when capturing image from camera!")
            break

        # If timer is not over then ignore 
        if not picture_timer.is_finished(): continue

        # Restart timer
        picture_timer.start()

        # Save photo
        cv2.imwrite(IMG_TEMP_PATH, frame)

        barcodes = decode(Image.open(IMG_TEMP_PATH))

        for barcode in barcodes:
            if barcode is not None:
                print(f'Barcode detected: {barcode.data.decode('utf-8')}')
                pyautogui.write(barcode.data.decode('utf-8'))
                pyautogui.typewrite(['enter']) 
            else:
                print('It was not possible to read barcode from camera')
        else:
            print('It was not possible to read barcode from camera')

        # Stop loop when pressing key 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def destroy():
    cap.release()
    cv2.destroyAllWindows()


def main():
    analyse_camera()
    destroy()


# Run driver
if __name__ == "__main__":
    main()
