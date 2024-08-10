import json
from pathlib import Path

def readFile(file):
  filePath = Path(__file__).resolve().parent.parent / 'storage' / file
  if filePath.exists():
    with filePath.open('r', encoding='utf-8') as document:
      content = document.read()
      if content:
        try:
          return json.loads(content)
        except:
          return None
      else:
        return None
  else:
    return None

def writeFile(file, data):
  filePath = Path(__file__).resolve().parent.parent / 'storage' / file
  filePath.parent.mkdir(parents=True, exist_ok=True)
  with filePath.open('w', encoding='utf-8') as jsonFile:
    json.dump(data, jsonFile, ensure_ascii=False, indent = 2)