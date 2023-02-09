# 제작 Uninx Timestamp 변경하기
# 변환 사이트 : https://www.epochconverter.com/
timestamp = "1691449688888"
# 기존 1673764273871
# 1675247400000
# 1691449688888
#This Python File is deleting "edtion" & "Compiler" part for Trimming JSON File
import json
import os
#Build의 jSonFile 디렉토리 내 파일 개수 변수에 저장
count_JSON = os.listdir("./json/")

for i in count_JSON:
    try :
        with open("./json/" + i, "r", encoding="utf8", errors='ignore') as json_file:
            json_data = json.load(json_file)
            json_data["date"] = timestamp
            with open("./json/" + i, 'w', encoding="utf8", errors='ignore') as outfile:
                json.dump(json_data, outfile, indent=4)
    except:
        print(i)