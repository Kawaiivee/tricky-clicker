from pathlib import Path

EXCLUDE_DIRS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    "node_modules",
    ".ipynb_checkpoints",
}

def print_tree(path: Path, prefix: str = ""):
    entries = sorted(
        [p for p in path.iterdir() if p.name not in EXCLUDE_DIRS],
        key=lambda p: (p.is_file(), p.name.lower())
    )

    for i, entry in enumerate(entries):
        connector = "└── " if i == len(entries) - 1 else "├── "
        print(prefix + connector + entry.name)

        if entry.is_dir():
            extension = "    " if i == len(entries) - 1 else "│   "
            print_tree(entry, prefix + extension)

if __name__ == "__main__":
    root = Path(".").resolve()
    print(root.name)
    print_tree(root)