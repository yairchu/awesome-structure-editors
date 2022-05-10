import requests
import sys


github_repo_prefix = "https://github.com/"


def get_github_repo(markdown_hyperlink):
    assert markdown_hyperlink.startswith("[") and markdown_hyperlink.endswith(")")
    link = markdown_hyperlink.split("](", 1)[1][:-1]
    if not link.startswith(github_repo_prefix):
        return
    return link[len(github_repo_prefix):]


def new_line(line):
    repo = None
    yearlink = None

    parts = line.split("|")
    name = parts[1].strip()
    prev_year = parts[-1].strip()
    if name.endswith(")"):
        repo = get_github_repo(name)
    if repo is None and prev_year.endswith(")"):
        repo = get_github_repo(prev_year)
        yearlink = github_repo_prefix + repo
    if repo is None:
        return

    date = requests.get(f"https://api.github.com/repos/{repo}/commits?per_page=1").json()[
        0]["commit"]["committer"]["date"]
    year = date.split("-", 1)[0]
    if yearlink is not None:
        year = f"[{year}]({yearlink})"
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
