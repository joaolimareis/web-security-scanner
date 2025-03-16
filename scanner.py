import argparse
import importlib
from utils.exporter import save_results

# Importação dinâmica para evitar problemas de importação circular
ssl_checker = importlib.import_module("core.ssl_checker")
get_ssl_info = ssl_checker.get_ssl_info

headers_checker = importlib.import_module("core.headers_checker")
check_security_headers = headers_checker.check_security_headers

tech_finder = importlib.import_module("core.tech_finder")
identify_technologies = tech_finder.identify_technologies

exposure_checker = importlib.import_module("core.exposure_checker")
check_sensitive_files = exposure_checker.check_sensitive_files

port_scanner = importlib.import_module("core.port_scanner")
scan_ports = port_scanner.scan_ports

def scan_domain(domain, save=False):
    """Executa o scan para um único domínio"""
    print(f"\n🔍 Escaneando: {domain}")

    print("\n🔍 Verificando SSL/TLS...")
    ssl_info = get_ssl_info(domain)

    print("\n=== Resultado da Análise SSL ===")
    if "error" in ssl_info:
        print(f"❌ Erro: {ssl_info['error']}")
    else:
        print(f"🌐 Domínio: {ssl_info['domain']}")
        print(f"🔐 Emitido para: {ssl_info['issued_to']}")
        print(f"🏢 Emitido por: {ssl_info['issued_by']}")
        print(f"📅 Válido de: {ssl_info['valid_from']}")
        print(f"📅 Válido até: {ssl_info['valid_until']}")
        print(f"✅ Certificado válido? {'Sim' if ssl_info['is_valid'] else 'Não'}")

    print("\n🔍 Verificando Cabeçalhos de Segurança...")
    headers_info = check_security_headers(domain)

    print("\n=== Resultado da Análise de Cabeçalhos HTTP ===")
    if "error" in headers_info:
        print(f"❌ Erro: {headers_info['error']}")
    else:
        for header, info in headers_info.items():
            status = info["status"]
            description = info["description"]
            value = info["value"] if info["value"] else "N/A"
            print(f"{status} {header}: {value}")
            print(f"   🔹 {description}")

    print("\n🔍 Identificando Tecnologias Web...")
    tech_info = identify_technologies(domain)

    print("\n=== Resultado da Identificação de Tecnologias ===")
    if "error" in tech_info:
        print(f"❌ Erro: {tech_info['error']}")
    else:
        for tech, value in tech_info.items():
            print(f"🔧 {tech}: {value}")

    print("\n🔍 Verificando Arquivos Sensíveis...")
    exposed_files = check_sensitive_files(domain)

    print("\n=== Resultado da Verificação de Arquivos Sensíveis ===")
    if "error" in exposed_files:
        print(f"❌ Erro: {exposed_files['error']}")
    else:
        for file, info in exposed_files.items():
            print(f"{info['status']} {file}")
            if "url" in info:
                print(f"   🔗 {info['url']}")

    print("\n🔍 Escaneando Portas e Serviços...")
    open_ports = scan_ports(domain)

    print("\n=== Resultado do Scanner de Portas ===")
    if "error" in open_ports:
        print(f"❌ Erro: {open_ports['error']}")
    else:
        for port, service in open_ports.items():
            print(f"🔌 Porta {port}: {service}")

    # Criando um dicionário com os resultados
    scan_results = {
        "SSL/TLS": ssl_info,
        "Cabeçalhos HTTP": headers_info,
        "Tecnologias Web": tech_info,
        "Arquivos Sensíveis": exposed_files,
        "Portas Abertas": open_ports,
    }

    # Salvar automaticamente se --save for passado
    if save:
        save_results(scan_results, domain)
    else:
        save_choice = input("\n💾 Deseja salvar os resultados? (s/n): ").strip().lower()
        if save_choice == "s":
            save_results(scan_results, domain)


def main():
    # Configurando argumentos CLI
    parser = argparse.ArgumentParser(description="Web Security Scanner")
    parser.add_argument("--url", nargs="+", help="Domínios a serem analisados (pode passar múltiplos)")
    parser.add_argument("--file", type=str, help="Arquivo contendo lista de domínios")
    parser.add_argument("--save", action="store_true", help="Salvar os resultados automaticamente em JSON/CSV")
    args = parser.parse_args()

    # Lista de domínios a escanear
    domains = []

    if args.url:
        domains.extend(args.url)

    if args.file:
        try:
            with open(args.file, "r") as f:
                file_domains = [line.strip() for line in f.readlines() if line.strip()]
                domains.extend(file_domains)
        except FileNotFoundError:
            print(f"❌ Erro: Arquivo '{args.file}' não encontrado.")
            return

    # Se nenhum domínio for especificado, pedir no terminal
    if not domains:
        domain = input("Digite o domínio para análise: ").strip()
        domains.append(domain)

    # Escanear todos os domínios da lista
    for domain in domains:
        scan_domain(domain, args.save)

if __name__ == "__main__":
    main()
