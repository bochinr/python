import time

timenow = int(time.time())
print('当前时间：%d' % timenow)

time.sleep(3)

timenow = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timenow))
print('当前标准时间：%s' % timenow)
