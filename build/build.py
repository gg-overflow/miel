import json
import os
import re

with open("index.template.html", encoding="utf-8") as f:
    template = f.read()

with open("translations.json", encoding="utf-8") as f:
    translations = json.load(f)

def render(template, strings):
    def replacer(match):
        key = match.group(1)
        return strings.get(key, f"MISSING:{key}")
    return re.sub(r"\{\{(\w+)\}\}", replacer, template)

# English → en/index.html
en_output = render(template, translations["en"])
with open("../en/index.html", "w", encoding="utf-8") as f:
    f.write(en_output)
print("✔ index.html (EN)")

# French → /index.html
os.makedirs("fr", exist_ok=True)
fr_output = render(template, translations["fr"])
with open("../index.html", "w", encoding="utf-8") as f:
    f.write(fr_output)
print("✔ fr/index.html (FR)")