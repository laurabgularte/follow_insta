import json
import webbrowser

def extract_usernames(data):
    usernames = set()
    if isinstance(data, list):
        items = data
    elif isinstance(data, dict):
        items = []
        for val in data.values():
            if isinstance(val, list):
                items.extend(val)
    else:
        items = []

    for item in items:
        if isinstance(item, dict):
            for entry in item.get("string_list_data", []):
                if isinstance(entry, dict) and "value" in entry:
                    usernames.add(entry["value"])
            if "value" in item:
                usernames.add(item["value"])
    return usernames

# Carregar os arquivos JSON
with open("following.json", "r", encoding="utf-8") as f:
    following_data = json.load(f)

with open("followers_1.json", "r", encoding="utf-8") as f:
    followers_data = json.load(f)

following = extract_usernames(following_data)
followers = extract_usernames(followers_data)

# Quem você segue mas não te segue de volta
not_following_back = sorted(list(following - followers))

# Gerar arquivo HTML com links clicáveis
html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Quem não te segue de volta</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; max-width: 600px; margin: 40px auto; padding: 0 20px; background: #f8f9fa; }}
        h1 {{ color: #262626; font-size: 22px; }}
        .subtitle {{ color: #666; margin-bottom: 20px; }}
        ul {{ list-style: none; padding: 0; }}
        li {{ background: #fff; padding: 12px 16px; margin-bottom: 8px; border-radius: 8px; border: 1px solid #dbdbdb; display: flex; justify-content: space-between; align-items: center; }}
        a {{ color: #0095f6; font-weight: 600; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>Não te seguem de volta ({len(not_following_back)})</h1>
    <p class="subtitle">Clique no link para abrir o perfil diretamente no Instagram:</p>
    <ul>
        {"".join([f'<li><span>@{user}</span><a href="https://instagram.com/{user}" target="_blank">Ver Perfil</a></li>' for user in not_following_back])}
    </ul>
</body>
</html>
"""

with open("resultado.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Sucesso! Encontradas {len(not_following_back)} contas que não te seguem de volta.")
webbrowser.open("resultado.html")
