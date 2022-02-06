import json
import os
import csv
import requests

file_path = "../data"
dirs = ["rice", "noodle", "other"]

categories = ["food", "basics", "soup", "cooks", "ingredients", "states"]
select = {
    "basics": {"밥": 1, "그외": 2, "면": 3, "빵": 4},
    "soup": {"국물있음": 1, "국물없음": 2},
    "cooks": {"삶기": 1, "굽기": 2, "튀기기": 3, "볶기": 4, "끓이기": 5, "날것": 6, "절이기": 7},
    "ingredients": {"소고기": 1, "돼지고기": 2, "닭고기": 3, "채소": 4, "해산물": 5, "유제품": 6, "갑각류": 7},
    "states": {"신남": 1, "스트레스": 2, "추움": 3, "보통": 4, "더움": 5, "우울함": 6, "배고픔": 7}
 }

s3 =

num = 1
for d in dirs:
    file_names = sorted(os.listdir(file_path + "/" + d))
    csv_file = open(file_path + "/" + d + ".csv", 'r')
    foods = csv.reader(csv_file)

    for i, food in enumerate(foods):
        body = {}
        # print(food)
        for idx, c in enumerate(food):
            if idx == 2:
                c = str(select[categories[idx]][c])
            if idx in [1, 3, 4, 5]:
                tmp = c.split(",")
                t_list = []
                for t in tmp:
                    t_list.append(select[categories[idx]][t.strip()])
                c = t_list
            body[str(categories[idx])] = c
        #post to db
        # print(i, file_names[i])
        tmp = file_names[i].split(".")
        # 사진 파일의 확장자
        ext = tmp[1]
        src = os.path.join(file_path + "/" + d, file_names[i])
        new_name = str(num) + "." + ext
        new_name = os.path.join(file_path + "/" + d, new_name)
        os.rename(src, new_name)
        body["imgSrc"] = s3 + str(new_name)
        url =
        headers = {'Content-Type': 'application/json'}
        res = requests.post(url, headers=headers, data=json.dumps(body))
        num += 1
        