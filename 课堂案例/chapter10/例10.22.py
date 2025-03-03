import json

new_dict = {"网站":
    [
        {"name": "百度",
         "url": "www.baidu.com"},
        {"name": "谷歌",
         "url": "www.google.com"},
        {"name": "微博",
         "url": "www.weibo.com"}
    ]
}

with open("record.json", "w") as f:
    json.dump(new_dict, f, indent=4, ensure_ascii=False)
    print("加载入文件完成...")
