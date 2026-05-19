from pathlib import Path


def ensure_directory(path: str):
    Path(path).mkdir(parents=True, exist_ok=True)


def write_file(path: str, content: str):

    file_path = Path(path)

    ensure_directory(file_path.parent)

    file_path.write_text(content)

    print(f"✅ Wrote: {path}")