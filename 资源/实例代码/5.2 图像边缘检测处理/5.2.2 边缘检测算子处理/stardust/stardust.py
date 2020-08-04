#导入基本功能cv2库
import cv2 as cv
#导入2D绘图库功能模块
from matplotlib import pyplot as plot

def EdgeDetection(img):
    #BGR(OpenCV使用BGR而非RGB格式)转灰度图像  
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
    #图像转为一维数组并获得灰度直方图以便调整算法的使用
    plot.hist(gray.ravel(), 256, [0, 256])
    #显示直方图窗口
    plot.show()
    #高斯滤波降噪
    gauss = cv.GaussianBlur(gray, (3, 3), 0)  
    #20对应最小阈值,160对应最大阈值
    canny = cv.Canny(gray, 0, 10) 
    #显示边缘处理后图像
    cv.imshow("EdgeDetection", canny)

#加载图片
img = cv.imread("logo.png",1)
#创建窗口
cv.namedWindow("stardust",cv.WINDOW_NORMAL)
#显示彩色图像
cv.imshow("color image",img)
#函数调用
EdgeDetection(img)
#等待按下任意按键继续运行下一条语句
cv.waitKey(0)
#释放HighGUI窗口
#cv.destroyAllWindows()

