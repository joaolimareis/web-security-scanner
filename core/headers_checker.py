import requests

# Cabeçalhos que vamos verificar e seus significados
SECURITY_HEADERS = {
    "Strict-Transport-Security": "Proteção contra ataques de downgrade HTTP → HTTPS (HSTS)",
    "Content-Security-Policy": "Evita ataques de Cross-Site Scripting (XSS)",
    "X-Frame-Options": "Protege contra clickjacking",
    "X-Content-Type-Options": "Evita ataques de MIME-sniffing",
    "Referrer-Policy": "Controla o envio do cabeçalho Referer",
    "Permissions-Policy": "Gerencia permissões de APIs do navegador"
}

def check_security_headers(url):
    """Verifica a presença de cabeçalhos HTTP de segurança."""
    try:
        # Garantindo que a URL tenha esquema (http/https)
        if not url.startswith("http"):
            url = "https://" + url
        
        response = requests.get(url, timeout=5)
        headers = response.headers

        results = {}
        for header, description in SECURITY_HEADERS.items():
            if header in headers:
                results[header] = {"status": "✅ Presente", "description": description, "value": headers[header]}
            else:
                results[header] = {"status": "❌ Ausente", "description": description, "value": None}

        return results

    except requests.RequestException as e:
        return {"error": f"Erro ao acessar {url}: {str(e)}"}

# Teste rápido (pode ser removido depois)
if __name__ == "__main__":
    url = "google.com"
    print(check_security_headers(url))
