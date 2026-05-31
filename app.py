import json
import random

with open("quotes.json", "r", encoding="utf-8") as f:
    quotes = json.load(f)

quote = random.choice(quotes)

print()
print("✨ 今日答案")
print()
print(quote["text"])
print()
print("——", quote["source"])

