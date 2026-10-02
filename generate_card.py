"""Neofetch-style profile card: writes dark_mode.svg, light_mode.svg and the
section divider (divider.svg) used by README.md.

Edit the data below and run `python generate_card.py`. Uses only the standard
library. The GitHub Action in .github/workflows runs it every day with
GITHUB_TOKEN set, which refreshes the "GitHub Stats" block; stats.json keeps the
last numbers so local runs without a token don't lose them.
"""
from __future__ import annotations

import json
import os
import urllib.request
from datetime import date
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOGIN = os.getenv("GITHUB_LOGIN", "EEw3n3")
CODING_SINCE = date(2022, 9, 1)  # first programming course at RVT
WIDTH = 60                       # characters per line on the right side
LOGO_COLUMNS = 28                # width of the logo column, in characters
LOGO_LINE = 18                   # px between logo lines: "█" is ~1.15em tall, so blocks touch
INFO_X = 330                     # x of the right column, px

# The "distro logo": the nickname in block letters, one row of letters per line
# of text below. "█" is drawn with the gradient, the frame characters in grey.
GLYPHS = {
    "E": ["███████╗", "██╔════╝", "█████╗  ", "██╔══╝  ", "███████╗", "╚══════╝"],
    "W": ["██╗    ██╗", "██║    ██║", "██║ █╗ ██║", "██║███╗██║", "╚███╔███╔╝", " ╚══╝╚══╝ "],
    "3": ["██████╗ ", "╚════██╗", " █████╔╝", " ╚═══██╗", "██████╔╝", "╚═════╝ "],
    "N": ["███╗   ██╗", "████╗  ██║", "██╔██╗ ██║", "██║╚██╗██║", "██║ ╚████║", "╚═╝  ╚═══╝"],
}
LOGO_ROWS = ["EW", "3N3"]  # Ew3n3 (the GitHub login is EEw3n3)

# Right side: ("title", text) | ("kv", key, value) | ("blank",) | ("section", name)
#             | ("stats",) | ("palette",)
INFO = [
    ("title", "ervin@ubinin"),
    ("kv", "OS", "Windows 11, Ubuntu Linux"),
    ("kv", "Uptime", None),  # computed from CODING_SINCE
    ("kv", "Host", "Rīgas Valsts tehnikums"),
    ("kv", "Kernel", "Software Developer"),
    ("kv", "Location", "Riga, Latvia"),
    ("kv", "Focus", "Backend · Web scraping · DevOps"),
    ("blank",),
    ("kv", "Languages.Programming", "Python, TypeScript, SQL, Bash"),
    ("blank",),
    ("kv", "Stack.Backend", "FastAPI, PostgreSQL, Redis"),
    ("kv", "Stack.Scraping", "Playwright, curl_cffi, XHR interception"),
    ("kv", "Stack.DevOps", "Docker, Linux, GitHub Actions"),
    ("blank",),
    ("kv", "AI.Anthropic", "Claude Opus 5.5, Sonnet 5.5, Fable 5.1"),
    ("kv", "AI.OpenAI", "GPT-6 Astra"),
    ("kv", "AI.Google", "Gemini Flash & Pro models"),
    ("blank",),
    ("kv", "Project", "MarketPulse (price monitoring)"),
    ("blank",),
    ("section", "Contact"),
    ("kv", "Email", "ervinubinin1@gmail.com"),
    ("kv", "LinkedIn", "in/ervīns-ubiņins-4099653a3"),
    ("blank",),
    ("section", "GitHub Stats"),
    ("stats",),
    ("blank",),
    ("palette",),
]

THEMES = {
    "dark_mode.svg": {"bg": "#161b22", "text": "#c9d1d9", "key": "#ffa657", "value": "#a5d6ff", "cc": "#616e7f",
                      "logo": ("#79c0ff", "#d2a8ff"),
                      "palette": ["#484f58", "#ff7b72", "#3fb950", "#d29922", "#58a6ff", "#bc8cff", "#39c5cf", "#b1bac4"]},
    "light_mode.svg": {"bg": "#f6f8fa", "text": "#24292f", "key": "#953800", "value": "#0a3069", "cc": "#8c959f",
                       "logo": ("#0969da", "#8250df"),
                       "palette": ["#24292f", "#cf222e", "#116329", "#4d2d00", "#0969da", "#8250df", "#1b7c83", "#6e7781"]},
}


def uptime(since: date, today: date | None = None) -> str:
    today = today or date.today()
    months = (today.year - since.year) * 12 + today.month - since.month - (today.day < since.day)
    years, months = divmod(months, 12)
    parts = [f"{years} year{'s' * (years != 1)}"] if years else []
    parts.append(f"{months} month{'s' * (months != 1)}")
    return ", ".join(parts) + " of coding"


def fetch_stats(login: str, token: str) -> dict | None:
    query = """query($login: String!) { user(login: $login) {
        followers { totalCount }
        repositories(ownerAffiliations: OWNER, privacy: PUBLIC, first: 100) { totalCount nodes { stargazerCount } }
        repositoriesContributedTo(contributionTypes: [COMMIT, PULL_REQUEST, REPOSITORY]) { totalCount }
        contributionsCollection { totalCommitContributions restrictedContributionsCount } } }"""
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": {"login": login}}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            user = json.load(resp)["data"]["user"]
    except Exception as exc:  # keep the last known numbers
        print(f"GitHub API: {exc}")
        return None
    c = user["contributionsCollection"]
    return {
        "repos": user["repositories"]["totalCount"],
        "contributed": user["repositoriesContributedTo"]["totalCount"],
        "stars": sum(n["stargazerCount"] for n in user["repositories"]["nodes"]),
        "commits": c["totalCommitContributions"] + c["restrictedContributionsCount"],
        "followers": user["followers"]["totalCount"],
    }


def load_stats() -> dict:
    path = HERE / "stats.json"
    stats = json.loads(path.read_text()) if path.exists() else {}
    token = os.getenv("GITHUB_TOKEN")
    fresh = fetch_stats(LOGIN, token) if token else None
    if fresh:
        stats = fresh
        path.write_text(json.dumps(stats, indent=2) + "\n")
    return stats


def logo_lines() -> list[str]:
    lines = []
    for i, word in enumerate(LOGO_ROWS):
        if i:
            lines.append("")
        for row in range(6):
            text = " ".join(GLYPHS[ch][row] for ch in word)
            lines.append(text.center(LOGO_COLUMNS).rstrip())
    return lines


def logo_spans(line: str) -> str:
    """Solid blocks take the gradient, the frame characters are grey."""
    out, run, cls = [], "", None
    for ch in line:
        c = cls if ch == " " else ("logo" if ch == "█" else "c")
        cls = cls or c
        if c and c != cls:
            out.append(f'<tspan class="{cls}">{escape(run)}</tspan>')
            run, cls = "", c
        run += ch
    if run:
        out.append(f'<tspan class="{cls or "c"}">{escape(run)}</tspan>')
    return "".join(out)


def kv(key: str, value: str, width: int = WIDTH) -> str:
    dots = "." * max(1, width - len(key) - len(value) - 3)
    return (f'<tspan class="key">{escape(key)}</tspan>:<tspan class="cc"> {dots} </tspan>'
            f'<tspan class="value">{escape(value)}</tspan>')


def rule(label: str) -> str:
    return f"{escape(label)} " + "—" * (WIDTH - len(label) - 1)


def info_lines(stats: dict, palette: list[str]) -> list[str]:
    def n(key):
        return f"{stats[key]:,}" if key in stats else "—"

    lines = []
    for item in INFO:
        kind = item[0]
        if kind == "title":
            lines.append(rule(item[1]))
        elif kind == "section":
            lines.append(rule(f"- {item[1]}"))
        elif kind == "blank":
            lines.append("")
        elif kind == "kv":
            lines.append(kv(item[1], item[2] if item[2] is not None else uptime(CODING_SINCE)))
        elif kind == "stats":
            half = (WIDTH - 3) // 2
            lines.append(kv("Repos", f'{n("repos")} {{Contributed: {n("contributed")}}}', half)
                         + " | " + kv("Stars", n("stars"), WIDTH - half - 3))
            lines.append(kv("Commits (last 12 mo)", n("commits"), half)
                         + " | " + kv("Followers", n("followers"), WIDTH - half - 3))
        elif kind == "palette":
            lines.append("".join(f'<tspan fill="{c}">███</tspan>' for c in palette))
    return lines


def render(theme: dict, stats: dict) -> str:
    right = info_lines(stats, theme["palette"])
    logo = logo_lines()
    rows = len(right)
    height = 30 + 20 * rows
    top = (height - LOGO_LINE * len(logo)) // 2 + 12  # centre the logo vertically (baseline of line 1)
    art = "\n".join(f'<tspan x="15" y="{top + LOGO_LINE * i}">{logo_spans(line)}</tspan>'
                    for i, line in enumerate(logo) if line)
    info = "\n".join(f'<tspan x="{INFO_X}" y="{30 + 20 * i}">{line}</tspan>' for i, line in enumerate(right) if line)
    g1, g2 = theme["logo"]
    return f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" width="985px" height="{height}px" font-size="16px"
     font-family="Consolas, 'SFMono-Regular', Menlo, 'DejaVu Sans Mono', 'Liberation Mono', monospace" role="img"
     aria-labelledby="card-title card-desc">
<title id="card-title">Ervin Ubinin — Software Developer</title>
<desc id="card-desc">Software developer from Riga, Latvia: Python, TypeScript, SQL; FastAPI, PostgreSQL, Redis; web scraping with Playwright and curl_cffi; Docker, Linux and GitHub Actions; Claude, OpenAI and Gemini APIs.</desc>
<defs>
<linearGradient id="logo" gradientUnits="userSpaceOnUse" x1="15" y1="{top - 16}" x2="{15 + LOGO_COLUMNS * 9}" y2="{top + LOGO_LINE * len(logo)}">
<stop offset="0" stop-color="{g1}"/><stop offset="1" stop-color="{g2}"/>
</linearGradient>
</defs>
<style>
text, tspan {{ white-space: pre; }}
.key {{ fill: {theme["key"]}; }} .value {{ fill: {theme["value"]}; }} .cc {{ fill: {theme["cc"]}; }} .c {{ fill: {theme["cc"]}; }}
.logo {{ fill: url(#logo); }}
</style>
<rect width="985px" height="{height}px" fill="{theme["bg"]}" rx="15"/>
<text x="15" y="30" fill="{theme["text"]}">
{art}
</text>
<text x="{INFO_X}" y="30" fill="{theme["text"]}">
{info}
</text>
</svg>
"""


# Thin gradient line between README sections, in the logo's colours; it reads
# on both the light and the dark GitHub theme.
DIVIDER = """<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="6" viewBox="0 0 1000 6" preserveAspectRatio="none">
<defs><linearGradient id="line" x1="0" x2="1" y1="0" y2="0">
<stop offset="0" stop-color="#58a6ff" stop-opacity="0"/><stop offset="0.2" stop-color="#58a6ff"/>
<stop offset="0.8" stop-color="#bc8cff"/><stop offset="1" stop-color="#bc8cff" stop-opacity="0"/>
</linearGradient></defs>
<rect x="0" y="2" width="1000" height="2" rx="1" fill="url(#line)"/>
</svg>
"""


def main() -> None:
    stats = load_stats()
    for name, theme in THEMES.items():
        (HERE / name).write_text(render(theme, stats), encoding="utf-8")
        print(f"wrote {name}")
    (HERE / "divider.svg").write_text(DIVIDER, encoding="utf-8")


if __name__ == "__main__":
    main()
