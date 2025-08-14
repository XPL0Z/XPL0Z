import re

# Lecture du README
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Trouver et incrémenter l'année
match = re.search(r"media/(\d+)-year\.gif", content)
if match:
    years = int(match.group(1)) + 1
    new_content = re.sub(
        r"media/\d+-year\.gif",
        f"media/{years}-year.gif",
        content
    )
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"README mis à jour avec media/{years}-year.gif")
else:
    print("Aucun GIF trouvé dans README.md")
