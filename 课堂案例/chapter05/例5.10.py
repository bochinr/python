from StuScore import *

def averageScore(data):
    totalScore = 0
    for i in data:
        if i < 0:
            raise ScoreError(str(i))
        totalScore += i
    return totalScore / len(data)
if __name__ == '__main__':
    data1 = (44, 78, 90, 80, 55)
    print("平均值=", averageScore(data1))
    data2 = (44, 78, 90, -80, 55)
    print("平均值=", averageScore(data2))
