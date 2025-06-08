import cv2 as cv
import pandas as pd

#load csv file
color_data = pd.read_csv('color.csv')

def get_color_name(R, G, B):
    min_dist = float('inf')
    color_name = ""
    for i in range(len(color_data)):
        r, g, b = int(color_data.loc[i, 'R']), int(color_data.loc[i, 'G']), int(color_data.loc[i, 'B'])
        dist = abs(R - r) + abs(G - g) + abs(B - b)
        if dist < min_dist:
            min_dist = dist
            color_name = color_data.loc[i, 'color_name']
    return color_name

def draw_function(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        global clicked, r, g, b, xpos, ypos
        clicked = True
        xpos = x
        ypos = y

cap = cv.VideoCapture(0)
clicked = False
xpos = ypos = r = g = b = 0

cv.namedWindow('Color Detector')
cv.setMouseCallback('Color Detector', draw_function)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    display_frame = frame.copy()

    if clicked:
        b, g, r = frame[ypos, xpos]
        b, g, r = int(b), int(g), int(r)
        color_name = get_color_name(r, g, b)
        text = f'{color_name} (R={r} G={g} B={b})'
        cv.rectangle(display_frame, (20, 20), (750, 60), (b, g, r), -1)
        cv.putText(display_frame, text, (30, 50), 2, 0.8, (255, 255, 255) if r + g + b < 400 else (0, 0, 0), 2)

    cv.imshow('Color Detector', display_frame)

    if cv.waitKey(20) & 0xFF == 27:  # ESC key
        break

cv.destroyAllWindows()