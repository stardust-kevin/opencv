#导入基本功能cv2库
import cv2 as cv
#导入2D绘图库功能模块
from matplotlib import pyplot as plot

def threshold_average(img, t1, t2, t3):
    #BGR(OpenCV使用BGR而非RGB格式)转灰度图像  
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
    #历遍每个像素元素并处理
    for i in range(len(img)):
        for j in range(len(img[0])):
            for k in range(len(img[0][0])):
                if img[i][j][k]>t1 and img[i][j][k]>t2 and img[i][j][k]>t3:
                    gray[i][j] = 255
                else:
                    gray[i][j] = 0
    #窗口输出指定图像
    cv.imshow("threshold_multi", gray)

#加载图片
img = cv.imread("landscape.jpg",1)
#创建窗口
cv.namedWindow("FixedThreshold",cv.WINDOW_NORMAL)
#显示彩色图像
cv.imshow("color image",img)
#函数调用
threshold_average(img, 70, 90, 80)
#等待按下任意按键继续运行下一条语句
cv.waitKey(0)
#释放HighGUI窗口
#cv.destroyAllWindows()

