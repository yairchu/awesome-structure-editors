"""
Script to update the "Last known update" and "stars" columns

It uses the GitHub CLI (requirement).
"""

import datetime
import json
import subprocess
import sys


github_repo_prefix = "https://github.com/"


def get_github_repo(markdown_hyperlink):
    assert markdown_hyperlink.startswith(
        "[") and markdown_hyperlink.endswith(")")
    content, link = markdown_hyperlink[1:-1].split("](", 1)
    if not link.startswith(github_repo_prefix):
        return markdown_hyperlink, None
    return content, link[len(github_repo_prefix):]


cur_year = datetime.datetime.today().year


def new_line(line):
    repo = None
    yearlink = None

    parts = line.split("|")
    name = parts[1].strip()
    prev_stars = parts[-2].strip()
    prev_year = parts[-1].strip()
    if name.endswith(")"):
        _, repo = get_github_repo(name)
    if repo is None and prev_year.endswith(")"):
        prev_year, repo = get_github_repo(prev_year)
        yearlink = github_repo_prefix + repo
    if repo is None:
        return

    assert int(prev_year) <= cur_year

    update_key = "pushedAt"
    stars_key = "stargazerCount"
    result_raw = subprocess.check_output(
        ["gh", "repo", "view", repo, "--json", f"{update_key},{stars_key}"])
    result = json.loads(result_raw.decode("UTF-8"))
    stars = result[stars_key]
    stars_equiv = prev_stars if stars == 0 and prev_stars != "-" else stars
    date = result[update_key]
    year = int(date.split("-", 1)[0])
    if yearlink is not None:
        year = f"[{year}]({yearlink})"
    head = line.rsplit("| ", 2)[0]
    return f"{head}| {stars_equiv} | {year}\n"


def line_order(line):
    head, stars, prev_year = [x.strip() for x in line.rsplit("|", 2)]
    if prev_year.endswith(")"):
        prev_year, _ = get_github_repo(prev_year)
    return -int(stars) if stars.isdigit() else 0, -int(prev_year), head


def process_table(prev):
    return sorted([new_line(line) or line for line in prev], key=line_order)


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
    table = []
    for line in lines:
        if not line.strip():
            yield from process_table(table)
            yield line
            break
        table.append(line)
    yield from lines


res = "".join(new_lines())
open("README.md", "w").write(res)
