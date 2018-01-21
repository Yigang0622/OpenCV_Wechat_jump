import cv2 as cv

img = cv.imread("3.png")
player_template = cv.imread('player.png')

img_blur = cv.GaussianBlur(img, (5, 5), 0)

canny_img = cv.Canny(img_blur, 1, 10)

height, width = canny_img.shape

crop_img = canny_img[300:int(height/2), 0:width]
crop_h, crop_w = crop_img.shape

player = cv.matchTemplate(img, player_template, cv.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(player)
center1_loc = (max_loc[0] + 50, max_loc[1] + 150)
player_spot = (max_loc[0] + 25, max_loc[1] + 150)

cv.circle(img, player_spot, 10, (0, 255, 255), -1)
cv.rectangle(img, max_loc, center1_loc, (0, 0, 255), 5)

for y in range(max_loc[1], max_loc[1]+150):
    for x in range(max_loc[0], max_loc[0]+50):
        canny_img[y][x] = 0


print(crop_w, crop_h)

center_x, center_y = 0, 0

max_x = 0

for y in range(crop_h):
    for x in range(crop_w):
        if crop_img[y, x] == 255:
            if center_x == 0:
                center_x = x
            if x > max_x:
                center_y = y
                max_x = x




print(center_x, center_y)

cv.circle(crop_img, (center_x, center_y), 10, 255, -1)

block_center = (center_x, center_y+300)

cv.circle(img, block_center, 10, 255, -1)

cv.line(img, player_spot, block_center, (0, 0, 255), 5)


print("玩家位置", player_spot)
print("落点位置", (center_x, center_y+300))


cv.namedWindow('img', cv.WINDOW_KEEPRATIO)
cv.imshow("img", canny_img)
cv.waitKey(0)
