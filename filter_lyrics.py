import anthropic
import os

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

with open("lyrics_raw.txt", "r", encoding="utf-8") as f:
    lyrics = f.read()

prompt = f"""
你是一本答案之书的编辑。从以下歌词中筛选出适合作为"答案之书"的句子。

筛选标准：
1. 主语模糊或缺失，读者可以自己代入
2. 意思没有说满，有留白和解读空间
3. 脱离歌曲语境依然成立
4. 不超过20个字
5. 可以套进完全不同的两种处境都成立

歌词内容：
{lyrics}

请输出一个JSON数组，格式如下，只输出JSON不要其他文字：
[
  {{"text": "句子内容", "source": "歌曲名"}},
  ...
]
"""

message = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=2048,
    messages=[{"role": "user", "content": prompt}]
)

print(message.content[0].text)
