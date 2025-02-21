import numpy as np
import cv2
import sys

# Caminho do arquivo com as coordenadas
file_path = sys.argv[1]

# Tamanho da tela
screen_width = 1920  
screen_height = 1080

# Inicializar a matriz de pontos de gaze
gaze_points = np.zeros((screen_height, screen_width), dtype=np.float32)

# Tamanho do raio de dilatação
dilation_radius = 30  


with open(file_path, 'r') as file:
    for line in file:
        coords = line.strip().split(',')
        if len(coords) >= 2:
            try:
                x, y = map(int, coords[:2])

                if 0 <= x < screen_width and 0 <= y < screen_height:
                    # Dilatar o ponto de gaze
                    for dx in range(-dilation_radius, dilation_radius + 1):
                        for dy in range(-dilation_radius, dilation_radius + 1):
                            if 0 <= x + dx < screen_width and 0 <= y + dy < screen_height:
                                gaze_points[y + dy, x + dx] += 1
            except ValueError:
                continue

# Normalizar a matriz de frequências
heatmap = np.uint8(cv2.normalize(gaze_points, None, 0, 255, cv2.NORM_MINMAX))

# Aplicar o colormap
heatmap_color = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)

# Exibir o mapa de calor
cv2.imshow("Heatmap", heatmap_color)

# Salvar o heatmap como uma imagem
#cv2.imwrite('heatmap.png', heatmap_color)

# Aguarde até que uma tecla seja pressionada
cv2.waitKey(0)
cv2.destroyAllWindows()