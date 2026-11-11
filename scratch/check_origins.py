import json

# Check transcript for how mahindra_farmers_of_india and punjab_farmer_cultivating were fetched
with open('C:/Users/Sanjai/.gemini/antigravity/brain/04f78d30-dfde-49a7-8d6a-da6fa246ba48/.system_generated/logs/transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        if 'mahindra_farmers_of_india' in line or 'punjab_farmer_cultivating' in line:
            obj = json.loads(line)
            for tc in obj.get('tool_calls', []):
                cmd = tc.get('args', {}).get('CommandLine', '')
                if cmd:
                    print(cmd[:200])
