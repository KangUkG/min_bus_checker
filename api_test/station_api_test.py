"""

전체 노선 경유 정류소
 - > 모든 정류소가 출력된다.

 내가 만들고 싶은 것
  - A 정류장 -> B정류장 이동 시 환승할 경우 환승 대상을 기다릴 때가 종종 있음.
  - b 정류장 몇시 도착. -> 버스 예상 도착 시간 몇분남음?
  - 남는 시간이 가장 적은 최적의 시간 계산.

 필요한 정보
  - 어떤 버스가 B 정류장에 도착하는데 걸리는 평균 시간.
  - 어떤 버스의 최초 출발 시간 or B 조회 당시 정류장에 도착하는데 남은 시간
  -
"""

import requests
from config import CONSTANTS
import json
import xmltodict

def to_json(dict_data, file_name):
    with open(f'{file_name}.txt', 'a') as f:
        js = json.dumps(dict_data, indent=4)
        f.write(js)
def all_bus_line():
    all_bul_url = "http://openapitraffic.daejeon.go.kr/api/rest/busRouteInfo/getRouteInfoAll"
    serviceKey = CONSTANTS.get('PUCLIC_BUS_DATA_API_KEY')

    route_cd_set = set()
    # 전체 노선 조회
    for req_page in range(1, 3):
        res = requests.get(f"{all_bul_url}?serviceKey={serviceKey}&reqPage={req_page}")
        data = xmltodict.parse(res.text)
        item_list = data['ServiceResult']['msgBody']['itemList']

        # for item in item_list:
            





        # route_cd_set.add(item_list['ROUTE_CD'])


    """ServiceResult -> msgHeader, msgBody -> itemList -> ROUTE_CD(노선ID)"""


    print("완료")
    # rst = xmltodict.parse(page1)
    # print(rst)


all_bus_line()

