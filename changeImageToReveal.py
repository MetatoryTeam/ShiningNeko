import json
import os
#Build의 jSonFile 디렉토리 내 파일 개수 변수에 저장
count_JSON = os.listdir("./json/")

for i in count_JSON:
    try :
        with open("./json/" + i, "r", encoding="utf8", errors='ignore') as json_file:
            json_data = json.load(json_file)
            json_data["image"] = "https://shiningneko.metatory.co.kr/reveal/reveal.png"
            json_data["animation_url"] = "https://shiningneko.metatory.co.kr/reveal/reveal_ticket.mp4"
            with open("./json/" + i, 'w', encoding="utf8", errors='ignore') as outfile:
                json.dump(json_data, outfile, indent=4)
    except:
        print(i)
#Opensea Reference
#https://docs.opensea.io/docs/metadata-standards