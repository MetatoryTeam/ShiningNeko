import json
import os
#Build의 jSonFile 디렉토리 내 파일 개수 변수에 저장
count_JSON = os.listdir("./json/")

for i in count_JSON:
    try :
        with open("./json/" + i, "r", encoding="utf8", errors='ignore') as json_file:
            json_data = json.load(json_file)
            #DNA 삭제하기
            json_data.pop("dna")
            if int(i.split(".json")[0]) in [1, 10, 74, 279, 445, 567, 815, 936, 994, 1000]:
                #레전드로 리빌하기 코드 두줄
                # json_data["image"] = "https://shiningneko.metatory.co.kr/reveal/legend.png"
                # json_data["animation_url"] = "https://shiningneko.metatory.co.kr/reveal/legend_ticket.mp4"
                #리빌로 에셋 링크 변경하기 코드 두줄
                json_data["image"] = "https://shiningneko.metatory.co.kr/reveal/reveal.png"
                json_data["animation_url"] = "https://shiningneko.metatory.co.kr/reveal/reveal_ticket.mp4"
            else:
                json_data["image"] = "https://shiningneko.metatory.co.kr/reveal/reveal.png"
                json_data["animation_url"] = "https://shiningneko.metatory.co.kr/reveal/reveal_ticket.mp4"
            for j in range(len(json_data["attributes"])):
                json_data["attributes"][j]["value"] = "Unknown"
            with open("./json/" + i, 'w', encoding="utf8", errors='ignore') as outfile:
                json.dump(json_data, outfile, indent=4)
    except:
        print(i)
#Opensea Reference
#https://docs.opensea.io/docs/metadata-standards