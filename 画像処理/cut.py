import cv2

#画像入力
im = cv2.imread('de.png',0)
   
#新しい配列に入力画像の一部を代入
dst = im[340:610,460:680]
    
#書き出し
cv2.imwrite('cut1.png',dst)


#画像入力
im = cv2.imread('pso.png',0)
   
#新しい配列に入力画像の一部を代入
dst = im[250:450,360:490]
    
#書き出し
cv2.imwrite('cut2.png',dst)


#画像入力
im = cv2.imread('tyukan.png',0)
   
#新しい配列に入力画像の一部を代入
dst = im[360:660,520:740]
    
#書き出し
cv2.imwrite('cut3.png',dst)