import requests
try:
    import ujson as json
except ModuleNotFoundError:
    import json

with open('zh2en.json', 'r', encoding='UTF-8') as f:
    zh2en = json.load(f)

r = requests.get("https://cdn.jsdelivr.net/gh/EhTagTranslation/DatabaseReleases/db.text.json")
r.raise_for_status()
j = r.json()
assert j["version"] == 6

detrans_namespace = zh2en["namespace"]
detrans_tag = zh2en["tag"]
for namespace in j["data"]:
    detrans_namespace[namespace["frontMatters"]["name"]] = namespace["namespace"]
    detrans_tag[namespace["namespace"]] = detrans_tag.get(namespace["namespace"], {})
    for tag in namespace["data"]:
        detrans_tag[namespace["namespace"]][namespace["data"][tag]["name"]] = tag

with open('zh2en.json', 'w', encoding='UTF-8') as f:
    json.dump(zh2en, f, ensure_ascii=False, indent='\t')