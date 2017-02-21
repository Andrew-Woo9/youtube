# 1. .conf폴더의 setting_local.json을 불러온다
# 2. 해당 내용을 json.loads()를 이용해 str-> dict형태로 변환
# 3. requests 라이브러리를 이용(pip install request), GET요청으로 데이터를 받아온 후
# 4. 해당 내용을 다시 json.load()를 이용해 파이선 객체로 변환
# 이후 내부에 있는 검색결과를 적절히 루프하여 print해주기

import json
import os

import requests
#현제 파일의 경로 위치
current_file_path = os.path.abspath(__file__)
go_to_parent_path = os.path.dirname(current_file_path)
# go_to_child_path_or_file = os.path.join(go_to_parent_path, 'youtube.py')
go_to_parent_path2 = os.path.dirname(go_to_parent_path)

# 상위 단계로 갈 때 os.path.dirname(이번단계)
# 하위 단계로 갈 때 os.path.join(이번단계)

#열기만 할때
config = json.loads(open(os.path.join(go_to_parent_path2, '.conf/settings_local.json')).read())


### 열고 닫아 줄때
# f = open(os.path.join(go_to_parent_path2, '.conf/settings_local.json'))
# config = f.read()
# f.close()


DEFAULT_URL = 'https://www.googleapis.com/youtube/v3/search'
KEY_par = config['youtube']['API_KEY_YOUTUBE']
PART_Par = 'snippet'
Q_par = 'aoa'

#전달할 키 캆을 params으로 넘겨줌
params = {
    'key': KEY_par,
    'part': PART_Par,
    'maxResults': 30,
    'q': Q_par,
}

r = requests.get(DEFAULT_URL, params=params)
# content = r.json()
# items = json.loads(open(content)).read()

result = r.text
result_dict = json.loads(result)

kind = result_dict['kind']
etag = result_dict['etag']
next_page_token = result_dict['nextPageToken']
region = result_dict['regionCode']
page_info = result_dict['pageInfo']
page_info_total_results = page_info['totalResults']
items = result_dict['items']

for index, item in enumerate(items):
    title = item['snippet']['title']
    print(index, title)
