import json
import csv
import os
from datetime import datetime

def sanitize_filename(domain):
    """Remove caracteres especiais do nome do domínio"""
    return domain.replace(".", "_").replace("/", "_")

def save_results(data, domain):
    """Salva os resultados do scan em JSON e CSV de forma organizada"""

    sanitized_domain = sanitize_filename(domain)  # Deixa o nome do arquivo limpo
    results_dir = f"results/{sanitized_domain}"  # Cria uma pasta por domínio

    # Criar pasta do domínio se não existir
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    json_filename = f"{results_dir}/latest_scan.json"  # Sempre sobrescreve o último scan
    csv_filename = f"{results_dir}/scan_results.csv"

    # Salvando em JSON
    with open(json_filename, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False, default=str)

    # Salvando em CSV
    with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Categoria", "Chave", "Valor"])

        for category, results in data.items():
            if isinstance(results, dict):
                for key, value in results.items():
                    writer.writerow([category, key, str(value)])
            else:
                writer.writerow([category, "", str(results)])

    print(f"\n📂 Resultados salvos em: {json_filename}")
