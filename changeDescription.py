import json
import os
#Build의 jSonFile 디렉토리 내 파일 개수 변수에 저장
count_JSON = os.listdir("./json/")
description = "ShiningNeko is a unique and exclusive collection of 1,000 handmade NFTs, featuring a fanciful cat character that exudes elegance and sophistication. Discover the wonders of this enchanting world today."

for i in count_JSON:
    try :
        with open("./json/" + i, "r", encoding="utf8", errors='ignore') as json_file:
            json_data = json.load(json_file)
            json_data["description"] = description
            with open("./json/" + i, 'w', encoding="utf8", errors='ignore') as outfile:
                json.dump(json_data, outfile, indent=4)
    except:
        print(i)