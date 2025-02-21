import sys
import cv2
import gaze_tracking as gt
import numpy as np
import screeninfo
import datetime

error = '/test/'
epog = gt.EPOG(error, sys.argv)
screen = screeninfo.get_monitors()[0]

# Dimensões da tela
screen_width = screen.width
screen_height = screen.height
screen_overlay = np.zeros((screen_height, screen_width, 3), dtype=np.uint8)
frame_overlay = screen_overlay.copy()
calibrated = False


def generator_file():
    return f"output_{datetime.datetime.now().strftime('%d-%m-%Y_%H.%M.%S')}.txt"

output_file = generator_file()
print(f"Arquivo de saída: {output_file}")

with open(output_file, 'w') as f:
    while True:

        _, frame = epog.webcam.read()
        if frame is not None:
            # Analisa a direção do olhar e mapeia para as coordenadas da tela
            screen_x, screen_y = epog.analyze(frame)

            if screen_x is not None and screen_y is not None and not calibrated:
                calibrated = True
                print("Calibração concluída com sucesso!!")

            if calibrated:
                f.write(f"{screen_x},{screen_y}\n")
                # Exibe tela após calibração
                cv2.circle(frame_overlay, (screen_x,  screen_y), 10, (0, 0, 255), -1)
                cv2.circle(frame_overlay, (screen_x,  screen_y), 150, (0, 0, 255), 2)
                cv2.imshow("Screen Overlay", frame_overlay)
            
            if cv2.waitKey(1) == 27:
                epog.webcam.release()
                cv2.destroyAllWindows()
                break


