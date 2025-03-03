# 例5.9
class ScoreError(Exception):  # 自定义异常类，继承于Exception
    def __init__(self, data):
        Exception.__init__(self, data)
        self.data = data

def __str__(self):  # 重载__str__方法
    return str(self.data) + "：非法数值( <0)"

if __name__ == '__main__':
    score = -60
    if score <= 0:
        raise ScoreError(score)