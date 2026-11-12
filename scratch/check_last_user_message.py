import json

with open('C:/Users/Sanjai/.gemini/antigravity/brain/043b14ed-505b-4860-b100-d2e67549e96e/.system_generated/logs/transcript.jsonl', 'r', encoding='utf-8') as f:
    lines = [json.loads(l) for l in f if l.strip()]

for entry in reversed(lines):
    if entry.get('type') == 'USER_INPUT':
        print(f"Step {entry.get('step_index')}")
        print("Content:", entry.get('content'))
        print("Media:", entry.get('media'))
        break
