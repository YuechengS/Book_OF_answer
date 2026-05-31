import json

new_quotes = [
    {"text": "宁愿错也不愿错过", "source": "我说今晚月光那么美,你说是的"},
    {"text": "流着眼泪的晴天", "source": "你曾是少年"},
    {"text": "故事的结局我还是我", "source": "我到外地去看你"},
    {"text": "时间带不走的美好", "source": "熟悉的拥抱"},
    {"text": "是否越是遗憾就越难忘", "source": "那年的愿望"},
    {"text": "许多人来来去去，相聚又别离", "source": "一个人的北京"},
    {"text": "一切都归于平静", "source": "达不到的爱"},
    {"text": "你曾是少年", "source": "你曾是少年"},
    {"text": "不知明天的方向", "source": "那年的愿望"},
    {"text": "一时停不下匆忙", "source": "月光曲"},
    {"text": "微笑告别，各自远去", "source": "达不到的爱"},
    {"text": "说再见也比较容易", "source": "我到外地去看你"},
    {"text": "我还要远走", "source": "我说今晚月光那么美,你说是的"},
    {"text": "能不能让我留下片刻的回忆", "source": "一个人的北京"},
]

with open("quotes.json", "r", encoding="utf-8") as f:
    existing = json.load(f)

combined = existing + new_quotes

with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(combined, f, ensure_ascii=False, indent=2)

print(f"完成！现在共有 {len(combined)} 句")
