import requests
import time
import re

song_ids = [
    (26427653, "风从海面吹过来"),
    (26427656, "北上的列车"),
    (26427658, "晚风"),
    (26427659, "我到外地去看你"),
    (26427661, "达不到的爱"),
    (26427662, "一个人的北京"),
    (26427663, "你曾是少年"),
    (26427664, "愿在秋天死去"),
    (26427665, "月光曲"),
    (26427666, "我说今晚月光那么美,你说是的"),
    (26427667, "熟悉的拥抱"),
    (26427668, "那年的愿望"),
    (26427655, "那么多的人,你要去哪里"),
    (26427660, "一个人的北京(钢琴版)"),
]

headers = {"Referer": "https://music.163.com/"}

with open("lyrics_raw.txt", "w", encoding="utf-8") as f:
    for song_id, song_name in song_ids:
        url = f"https://music.163.com/api/song/lyric?id={song_id}&lv=1&kv=1&tv=-1"
        resp = requests.get(url, headers=headers)
        data = resp.json()
        lyric = data.get("lrc", {}).get("lyric", "")
        # 去掉时间戳
        clean = re.sub(r'\[[\d:.]+\]', '', lyric).strip()
        f.write(f"=== {song_name} ===\n{clean}\n\n")
        print(f"✓ {song_name}")
        time.sleep(0.5)

print("完成！歌词存到 lyrics_raw.txt")
