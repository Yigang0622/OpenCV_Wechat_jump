import cv2 as cv

img = cv.imread("4.png")
player_template = cv.imread('player.png')

player = cv.matchTemplate(img, player_template, cv.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(player)

corner_loc = (max_loc[0] + 50, max_loc[1] + 150)
player_spot = (max_loc[0] + 25, max_loc[1] + 150)

#绘制player位置标记
cv.rectangle(img, max_loc, corner_loc, (0, 0, 255), 5)
cv.circle(img, player_spot, 10, (255, 0, 0), -1)




img_blur = cv.GaussianBlur(img, (5, 5), 0) #高斯模糊
canny_img = cv.Canny(img_blur, 1, 10) #边缘检测
height, width = canny_img.shape

#消除多余的头部
for y in range(max_loc[1], max_loc[1]+150):
    for x in range(max_loc[0], max_loc[0]+50):
        canny_img[y][x] = 0

crop_img = canny_img[300:int(height/2), 0:width] #裁切
crop_h, crop_w = crop_img.shape

center_x, center_y = 0, 0 #临时变量
max_x = 0

#计算中央点
for y in range(crop_h):
    for x in range(crop_w):
        if crop_img[y, x] == 255:
            if center_x == 0:
                center_x = x
            if x > max_x:
                center_y = y
                max_x = x


cv.circle(crop_img, (center_x, center_y), 10, 255, -1)


block_center = (center_x, center_y+300) #中央点

cv.circle(img, block_center, 10, 255, -1) #绘制落脚点
cv.line(img, player_spot, block_center, (0, 255, 0), 5) #绘制直线

print("玩家位置", player_spot)
print("落点位置", (center_x, center_y+300))

cv.namedWindow('img', cv.WINDOW_KEEPRATIO)
cv.imshow("img", img)
cv.waitKey(0)
