import json

test_dict = {"网站":
    	[
        	{"name": "百度",
         	"url": "www.baidu.com"},
        	{"name": "谷歌",
        	 "url": "www.google.com"},
        	{"name": "微博",
         	"url": "www.weibo.com"}
    	]
	}
print(test_dict)
print(type(test_dict))
# dumps 将数据转换成字符串
json_str = json.dumps(test_dict, ensure_ascii=False)
print(json_str)
print(type(json_str))

