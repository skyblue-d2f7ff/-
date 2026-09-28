import json
import urllib.request

# 1. 기본 공지 문구
print("날씨 예보 프로그램")
print("6:00 및 15:00 시간때의 날씨를 알려드립니다.")

# 2. 천안 날씨 데이터 불러오기
city = "Cheonan"
url = f"https://wttr.in/{city}?format=j1"

req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=10) as response:
    weather_data = json.loads(response.read().decode("utf-8"))

# 오늘의 시간대별 예보 목록
today = weather_data["weather"][0]
hourly = today["hourly"]

# 6:00(오전 6시)와 15:00(오후 3시) 데이터 추출
data_6am = next(item for item in hourly if item["time"] == "600")
data_3pm = next(item for item in hourly if item["time"] == "1500")

# 3. 6:00 및 15:00 날씨 정보를 변수에 저장
weather_6am = {
    "날씨": data_6am["weatherDesc"][0]["value"].strip(),
    "기온": int(data_6am["tempC"]),
    "체감온도": int(data_6am["FeelsLikeC"]),
    "습도": int(data_6am["humidity"]),
    "강수확률": int(data_6am["chanceofrain"]),
}

weather_3pm = {
    "날씨": data_3pm["weatherDesc"][0]["value"].strip(),
    "기온": int(data_3pm["tempC"]),
    "체감온도": int(data_3pm["FeelsLikeC"]),
    "습도": int(data_3pm["humidity"]),
    "강수확률": int(data_3pm["chanceofrain"]),
}