import json
import csv

# 读取JSON文件
with open('item.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 创建CSV文件
with open('item.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # 写入列名
    writer.writerow(['id', 'name'])

    # 写入数据
    for item in data:
        if len(item['name']) > 0:
            writer.writerow([item['id'], item['name']])
