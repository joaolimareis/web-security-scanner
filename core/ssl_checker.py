import ssl
import socket
from datetime import datetime, timezone

def get_ssl_info(domain):
    """Obtém informações do certificado SSL de um domínio"""
    try:
        # Conectando ao site na porta 443 (HTTPS)
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()

        # Extraindo informações do certificado
        valid_until = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z").replace(tzinfo=timezone.utc)
        current_time = datetime.now(timezone.utc)  # Substitui datetime.utcnow()

        ssl_info = {
            "domain": domain,
            "issued_to": cert.get("subject", [["Unknown"]])[0][0][1],
            "issued_by": cert.get("issuer", [["Unknown"]])[0][0][1],
            "valid_from": datetime.strptime(cert["notBefore"], "%b %d %H:%M:%S %Y %Z").replace(tzinfo=timezone.utc),
            "valid_until": valid_until,
            "is_valid": valid_until > current_time  # Verifica validade corretamente
        }

        return ssl_info

    except Exception as e:
        return {"error": f"Erro ao obter certificado SSL de {domain}: {str(e)}"}

# Teste rápido (pode ser removido depois)
if __name__ == "__main__":
    domain = "google.com"
    print(get_ssl_info(domain))
