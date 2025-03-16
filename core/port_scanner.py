import subprocess
import re
import platform

def scan_ports(domain):
    """Executa um scan de portas abertas no domínio/IP usando Nmap."""
    try:
        # Detectar se estamos rodando no Windows chamando WSL
        if platform.system() == "Windows":
            command = ["wsl", "nmap", "-F", domain]
        else:
            command = ["nmap", "--top-ports", "20", domain]


        result = subprocess.run(command, capture_output=True, text=True, timeout=15)
        output = result.stdout

        open_ports = {}

        # Expressão regular para encontrar portas abertas
        pattern = re.compile(r"(\d+/tcp)\s+open\s+(\S+)")
        matches = pattern.findall(output)

        for match in matches:
            port = match[0].split("/")[0]
            service = match[1]
            open_ports[port] = service

        return open_ports if open_ports else {"info": "Nenhuma porta aberta encontrada"}

    except Exception as e:
        return {"error": f"Erro ao escanear {domain}: {str(e)}"}

# Teste rápido
if __name__ == "__main__":
    domain = "scanme.nmap.org"  # Domínio de teste oficial do Nmap
    print(scan_ports(domain))
