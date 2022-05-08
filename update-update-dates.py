import requests
import sys

result = []

lines = iter(open("README.md"))

for line in lines:
    result.append(line)
    if line.endswith(" | Last known update\n"):
        break
else:
    print("Did not find table")
    sys.exit(1)
result.append(next(lines))

for line in lines:
    if not line.strip():
        result.append(line)
        break
    namelink = line.split("|")[1].strip()
    if not namelink.endswith(")"):
        result.append(line)
        continue
    link = namelink.split("](", 1)[1][:-1]
    prefix = "https://github.com/"
    if not link.startswith(prefix):
        result.append(line)
        continue
    repo = link[len(prefix):]
    date = requests.get(f"https://api.github.com/repos/{repo}/commits?per_page=1").json()[
        0]["commit"]["committer"]["date"]
    year = date.split("-", 1)[0]
    head = line.rsplit("| ", 1)[0]
    result.append(f"{head}| {year}\n")

for line in lines:
    result.append(line)

open("README.md", "w").write("".join(result))
