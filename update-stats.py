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


def is_flag(txt):
    return not txt.isascii() or txt in "$"


def text_flags(line):
    prev = "-"
    res = []
    for x in line:
        if is_flag(x):
            if not is_flag(prev):
                res.append("")
            res[-1] += x
        prev = x
    return res


def new_line(line, all_flags):
    repo = None

    parts = line.split("|")
    assert not parts[0].strip()
    name = parts[1].strip()
    prev_flags = parts[2].strip()
    flags = text_flags(prev_flags)
    desc = parts[3].strip()
    impl_lang = parts[4].strip()
    prev_stars = parts[5].strip()
    if prev_stars.endswith(")"):
        _, repo = get_github_repo(prev_stars)
    else:
        assert name.endswith(")")
        _, repo = get_github_repo(name)
    if repo is None:
        return

    update_key = "pushedAt"
    stars_key = "stargazerCount"
    result_raw = subprocess.check_output(
        ["gh", "repo", "view", repo, "--json", f"{update_key},{stars_key}"])
    result = json.loads(result_raw.decode("UTF-8"))
    stars = result[stars_key]
    if prev_stars.endswith(")"):
        stars = f"[{stars}](https://github.com/{repo})"
    date = result[update_key]
    year = int(date.split("-", 1)[0])
    flags = " ".join(sorted(flags, key=lambda x: all_flags.index(x)))
    assert len(flags) == len(prev_flags)
    return f"| {name} | {flags} | {desc} | {impl_lang} | {stars} | {year}\n"


def line_order(line):
    head, stars, prev_year = [x.strip() for x in line.rsplit("|", 2)]
    if stars.endswith(")"):
        stars, _ = get_github_repo(stars)
    return -int(stars) if stars.isdigit() else 0, -int(prev_year), head


def process_table(prev, all_flags):
    return sorted([new_line(line, all_flags) or line for line in prev], key=line_order)


def new_lines():
    lines = iter(open("README.md"))
    all_flags = []
    for line in lines:
        yield line
        if line.endswith("| ⭐️ | Updated\n"):
            break
        all_flags.extend(text_flags(line))
    else:
        print("Did not find table")
        sys.exit(1)
    assert len(all_flags) == len(set(all_flags))
    yield next(lines)
    table = []
    for line in lines:
        if not line.strip():
            yield from process_table(table, all_flags)
            yield line
            break
        table.append(line)
    yield from lines


res = "".join(new_lines())
open("README.md", "w").write(res)
