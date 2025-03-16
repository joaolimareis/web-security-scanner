import requests
import re

def identify_technologies(url):
    """Identifica tecnologias utilizadas pelo site analisando cabeçalhos HTTP e HTML."""
    try:
        # Garantindo que a URL tenha esquema (http/https)
        if not url.startswith("http"):
            url = "https://" + url
        
        response = requests.get(url, timeout=5)
        headers = response.headers
        body = response.text.lower()

        tech_info = {}

        # Identificando o Servidor Web
        server = headers.get("Server", "Desconhecido")
        tech_info["Servidor Web"] = server

        # Identificando CMS populares
        if "wp-content" in body or "wordpress" in headers.get("X-Powered-By", "").lower():
            tech_info["CMS"] = "WordPress"
        elif "joomla" in body:
            tech_info["CMS"] = "Joomla"
        elif "drupal" in body:
            tech_info["CMS"] = "Drupal"
        elif re.search(r'<meta\s+name="generator"\s+content="(.+?)"', body):
            match = re.search(r'<meta\s+name="generator"\s+content="(.+?)"', body)
            tech_info["CMS"] = match.group(1)
        else:
            tech_info["CMS"] = "Não identificado"

        # Identificando Linguagens de Backend
        powered_by = headers.get("X-Powered-By", "").lower()
        if "php" in powered_by:
            tech_info["Linguagem Backend"] = "PHP"
        elif "python" in powered_by:
            tech_info["Linguagem Backend"] = "Python"
        elif "node" in powered_by or "express" in powered_by:
            tech_info["Linguagem Backend"] = "Node.js"
        elif "asp" in powered_by or "microsoft" in powered_by:
            tech_info["Linguagem Backend"] = "ASP.NET"
        else:
            tech_info["Linguagem Backend"] = "Não identificada"

        # Identificando Frameworks Frontend por arquivos JS conhecidos
        if "react" in body or "react-dom" in body or "data-reactroot" in body:
            tech_info["Framework Frontend"] = "React"
        elif "vue" in body or "vue.js" in body or 'vuex' in body:
            tech_info["Framework Frontend"] = "Vue.js"
        elif "angular" in body or "ng-app" in body:
            tech_info["Framework Frontend"] = "Angular"
        elif "svelte" in body:
            tech_info["Framework Frontend"] = "Svelte"
        else:
            tech_info["Framework Frontend"] = "Não identificado"

        return tech_info

    except requests.RequestException as e:
        return {"error": f"Erro ao acessar {url}: {str(e)}"}

# Teste rápido
if __name__ == "__main__":
    url = "google.com"
    print(identify_technologies(url))
