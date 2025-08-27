`python

parser.py - 語義解析模組
def parse_text(text):
"""
將輸入文字進行語義拆解與腐蝕標記。
"""
if "制度" in text:
return {"status": "腐蝕疑似", "keywords": ["制度"], "note": "可能涉及語義崩解"}
else:
return {"status": "正常", "keywords": [], "note": "未偵測腐蝕語"}

測試範例
if name == "main":
sample = "制度語言已遭腐蝕，需進行語義重構。"
result = parse_text(sample)
print(result)
`
