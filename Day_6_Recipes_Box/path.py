from pathlib import Path

base = Path.cwd().resolve()
guide = Path(base, 'Europe', 'Frane', Path('Paris', 'Eiffel_Tower.txt'))
print(guide.parent)