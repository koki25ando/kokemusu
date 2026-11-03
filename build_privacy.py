import re, sys, html
src = open(sys.argv[1], encoding="utf-8").read().strip().split("\n")
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\[(.+?)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', t)
    return t
out, i, title = [], 0, ""
while i < len(src):
    line = src[i]
    if line.startswith("# "):
        title = line[2:]; out.append(f"<h1>{inline(title)}</h1>")
    elif line.startswith("## "):
        out.append(f"<h2>{inline(line[3:])}</h2>")
    elif line.startswith("|"):
        rows = []
        while i < len(src) and src[i].startswith("|"):
            rows.append([c.strip() for c in src[i].strip("|").split("|")]); i += 1
        out.append("<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in rows[0]) + "</tr></thead><tbody>")
        for r in rows[2:]:
            out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
        out.append("</tbody></table>"); continue
    elif line.startswith("- "):
        items = []
        while i < len(src) and src[i].startswith("- "):
            items.append(src[i][2:]); i += 1
        out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>"); continue
    elif line.strip():
        para = []
        while i < len(src) and src[i].strip() and not src[i].startswith(("#", "|", "- ")):
            para.append(inline(src[i])); i += 1
        out.append("<p>" + "<br>".join(para) + "</p>"); continue
    i += 1
body = "\n".join(out)
print(f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>
  :root {{ --bg:#F3EFE6; --card:#FBF9F4; --ink:#2F3A2E; --muted:#6E776A; --moss:#4F6B3A; --line:#DDD6C6; }}
  @media (prefers-color-scheme: dark) {{ :root {{ --bg:#1E231D; --card:#262C25; --ink:#E6E8DF; --muted:#A7AE9F; --moss:#A6C98A; --line:#3A4237; }} }}
  body {{ margin:0; background:var(--bg); color:var(--ink); font-family:-apple-system,"Hiragino Sans","Noto Sans JP",sans-serif; line-height:1.85; }}
  main {{ max-width:720px; margin:0 auto; padding:40px 16px 64px; }}
  h1 {{ font-size:1.6rem; font-weight:600; margin:0 0 8px; }}
  h2 {{ font-size:1.15rem; font-weight:600; margin:40px 0 8px; padding-top:16px; border-top:1px solid var(--line); }}
  a {{ color:var(--moss); }}
  table {{ width:100%; border-collapse:collapse; font-size:.92rem; background:var(--card); }}
  th, td {{ text-align:left; vertical-align:top; padding:10px; border:1px solid var(--line); }}
  th {{ color:var(--muted); font-weight:600; }}
  .scroll {{ overflow-x:auto; }}
  footer {{ margin-top:48px; color:var(--muted); font-size:.85rem; }}
</style>
</head>
<body>
<main>
{body.replace("<table>", '<div class="scroll"><table>').replace("</table>", "</table></div>")}
<footer>Kokemusu（苔むす）</footer>
</main>
</body>
</html>""")
