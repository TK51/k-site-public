# build_readme_toc.py
from pathlib import Path

OUTPUT_DIR = Path("docs")
README_FILE = Path("README.md")
TOC_HEADER = "## Site Contents"

emoji_map = {
    ".py": "📄",
    ".md": "📝",
    "folder": "📁"
}

def build_toc():
    if not OUTPUT_DIR.exists():
        print("❌ Output folder not found.")
        return []

    toc_lines = [TOC_HEADER, ""]

    for item in sorted(OUTPUT_DIR.iterdir()):
        if item.is_dir() and (item / "index.html").exists():
            toc_lines.append(f"- {emoji_map['folder']} [{item.name}]({item.name}/index.html)")
        elif item.is_file() and item.suffix == ".html" and "-viewer" in item.stem:
            label = item.stem.replace("-viewer", "")
            ext = Path(label).suffix
            emoji = emoji_map.get(ext, "📄")
            toc_lines.append(f"- {emoji} [{label}]({item.name})")

    return toc_lines

def toc_already_in_readme():
    if not README_FILE.exists():
        return False
    with open(README_FILE, "r", encoding="utf-8") as f:
        return TOC_HEADER in f.read()

def append_to_readme(toc_lines):
    if not toc_lines:
        print("⚠️ Nothing to append.")
        return
    if toc_already_in_readme():
        print("⚠️ TOC already exists in README.md — skipping append.")
        return
    with open(README_FILE, "a", encoding="utf-8") as f:
        f.write("\n\n" + "\n".join(toc_lines))
    print("✅ TOC appended to README.md")

if __name__ == "__main__":
    toc = build_toc()
    for line in toc:
        print(line)
    append_to_readme(toc)
