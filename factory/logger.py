from pathlib import Path
from datetime import datetime


LOG_DIR = Path("logs")

LOG_DIR.mkdir(exist_ok=True)


def log_message(filename, content):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    path = LOG_DIR / filename

    with open(path, "a", encoding="utf-8") as f:

        f.write(f"\n[{timestamp}]\n")
        f.write(str(content))
        f.write("\n")