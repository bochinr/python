# from rectangle import *  # 导入矩形模块
# from circular import *  # 导入圆形模块

import rectangle
import circular

if __name__ == '__main__':
    print("圆形的周长为：", circular.girth(10))  # 计算圆形的周长
    print("矩形的周长为：", rectangle.girth(10, 20))  # 计算矩形的周长
