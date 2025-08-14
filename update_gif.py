import re

years = 1

# Lecture du README
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Remplacement du chemin media/X-year.gif
new_content = re.sub(
    r"media/\d+-year\.gif",
    f"media/{years}-year.gif",
    content
)

# Écriture du README
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"README mis à jour avec media/{years_passed}-year.gif")

years =+ 1