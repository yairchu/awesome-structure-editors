import requests
import sys


def new_line(line):
    namelink = line.split("|")[1].strip()
    if not namelink.endswith(")"):
        return
    link = namelink.split("](", 1)[1][:-1]
    prefix = "https://github.com/"
    if not link.startswith(prefix):
        return
    repo = link[len(prefix):]
    date = requests.get(f"https://api.github.com/repos/{repo}/commits?per_page=1").json()[
        0]["commit"]["committer"]["date"]
    year = date.split("-", 1)[0]
    head = line.rsplit("| ", 1)[0]
    return f"{head}| {year}\n"


def new_lines():
    lines = iter(open("README.md"))
    for line in lines:
        yield line
        if line.endswith(" | Last known update\n"):
            break
    else:
        print("Did not find table")
        sys.exit(1)
    yield next(lines)
    for line in lines:
        if not line.strip():
            yield line
            break
        yield new_line(line) or line
    yield from lines


res = "".join(new_lines())
open("README.md", "w").write(res)
