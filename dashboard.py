import requests
from flask import Flask, render_template, jsonify
import os
import json

app = Flask(__name__)

RESULTS_DIR = "results"
def sanitize_filename(domain):
    """Remove caracteres especiais para criar nomes de arquivos seguros"""
    return domain.replace(".", "_").replace("/", "_")

@app.route("/")
def index():
    """Carrega a interface do Dashboard"""
    return render_template("index.html")

@app.route("/results")
def list_results():
    """Lista os domínios disponíveis para visualização"""
    try:
        domains = [d for d in os.listdir("results") if os.path.isdir(f"results/{d}")]
        return jsonify({"domains": domains})
    except FileNotFoundError:
        return jsonify({"error": "O diretório de resultados não foi encontrado"}), 500

@app.route("/results/<domain>")
def get_result(domain):
    """Carrega o último scan de um domínio"""
    sanitized_domain = sanitize_filename(domain)
    json_file = f"results/{sanitized_domain}/latest_scan.json"

    if not os.path.exists(json_file):
        return jsonify({"error": "Nenhum resultado encontrado para este domínio"}), 404

    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    return jsonify(data)



@app.route("/geolocate/<domain>")
def geolocate(domain):
    """Obtém a geolocalização de um domínio"""
    try:
        response = requests.get(f"http://ip-api.com/json/{domain}")
        data = response.json()
        if data["status"] == "fail":
            return jsonify({"error": "Geolocalização não encontrada"}), 404
        
        return jsonify({
            "lat": data["lat"],
            "lon": data["lon"],
            "country": data["country"],
            "city": data["city"],
            "isp": data["isp"]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
