import cv2
#import numpy as np

"""
# 定数定義
ORG_WINDOW_NAME = "org"
GRAY_WINDOW_NAME = "gray"
CANNY_WINDOW_NAME = "canny"

ORG_FILE_NAME = "de.png"
GRAY_FILE_NAME = "gray.png"
CANNY_FILE_NAME = "canny.png"

# 元の画像を読み込む
org_img = cv2.imread(ORG_FILE_NAME, cv2.IMREAD_UNCHANGED)
# グレースケールに変換
gray_img = cv2.imread(ORG_FILE_NAME, cv2.IMREAD_GRAYSCALE)
# エッジ抽出
canny_img = cv2.Canny(gray_img, 50, 110)

# ウィンドウに表示
cv2.namedWindow(ORG_WINDOW_NAME)
cv2.namedWindow(GRAY_WINDOW_NAME)
cv2.namedWindow(CANNY_WINDOW_NAME)

cv2.imshow(ORG_WINDOW_NAME, org_img)
cv2.imshow(GRAY_WINDOW_NAME, gray_img)
cv2.imshow(CANNY_WINDOW_NAME, canny_img)

# ファイルに保存
cv2.imwrite(GRAY_FILE_NAME, gray_img)
cv2.imwrite(CANNY_FILE_NAME, canny_img)

# 終了処理
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
"""
ORG_FILE_NAME = "cut1.png"
im = cv2.imread(ORG_FILE_NAME)
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(img, contours,1,(-1,-1,-1), -1)
cv2.imwrite("rinkaku1.png",img)



ORG_FILE_NAME = "cut2.png"
im = cv2.imread(ORG_FILE_NAME)
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(img, contours, 1, -1,-1,0,4)
cv2.imwrite("rinkaku2.png",img)


ORG_FILE_NAME = "cut3.png"
im = cv2.imread(ORG_FILE_NAME)
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(img, contours, -1, (0,255,0), 1)
cv2.imwrite("rinkaku3.png",img)
"""

''' 
img = cv2.imread('cut1.png')
inv = cv2.bitwise_not(img)
 
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
invgray = cv2.bitwise_not(gray)
 
cv2.imwrite('inv.png',inv)
cv2.imwrite('invgray.png',invgray)
'''

img = cv2.imread('cut1.png')
inv = cv2.bitwise_not(img)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
thresh = 220
max_pixel = 255
ret, img_dst = cv2.threshold(img_gray,thresh,max_pixel,cv2.THRESH_BINARY)
cv2.imwrite('result1.png',img_dst)


img = cv2.imread('cut2.png')
inv = cv2.bitwise_not(img)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
thresh = 220
max_pixel = 255
ret, img_dst = cv2.threshold(img_gray,thresh,max_pixel,cv2.THRESH_BINARY)
cv2.imwrite('result2.png',img_dst)


img = cv2.imread('cut3.png')
inv = cv2.bitwise_not(img)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
thresh = 220
max_pixel = 255
ret, img_dst = cv2.threshold(img_gray,thresh,max_pixel,cv2.THRESH_BINARY)
cv2.imwrite('result3.png',img_dst)