import markdown
from pathlib import Path

# Зчитуємо README.md
readme_text = Path("README.md").read_text(encoding="utf-8")

# Конвертуємо Markdown у HTML
html = markdown.markdown(readme_text)

# Зберігаємо у папку docs/
Path("docs").mkdir(exist_ok=True)
Path("docs/index.html").write_text(html, encoding="utf-8")

print("Документацію згенеровано у docs/index.html")
