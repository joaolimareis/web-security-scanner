import requests

# Lista de arquivos sensíveis comuns
SENSITIVE_FILES = [
    "robots.txt", ".env", "config.php", "wp-config.php", "error.log",
    "debug.log", "database.sql", "backup.zip", ".git/config"
]

def check_sensitive_files(url):
    """Verifica se arquivos sensíveis estão acessíveis publicamente."""
    try:
        if not url.startswith("http"):
            url = "https://" + url

        exposed_files = {}

        for file in SENSITIVE_FILES:
            full_url = f"{url}/{file}"
            response = requests.get(full_url, timeout=5)

            if response.status_code == 200:
                exposed_files[file] = {"status": "❌ Exposto", "url": full_url}
            elif response.status_code in [403, 401]:
                exposed_files[file] = {"status": "🔒 Protegido (Acesso negado)"}
            else:
                exposed_files[file] = {"status": "✅ Não encontrado"}

        return exposed_files

    except requests.RequestException as e:
        return {"error": f"Erro ao acessar {url}: {str(e)}"}

# Teste rápido
if __name__ == "__main__":
    url = "example.com"
    print(check_sensitive_files(url))
