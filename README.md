

# 🛡️ Web Security Scanner 🔍  

> 🚀 **Web scraper para análise de segurança de sites**, coletando informações de SSL/TLS, cabeçalhos HTTP e tecnologias utilizadas.

🔹 **Tecnologias** usadas no scanner:
- 📜 **Verificação de Certificados SSL/TLS**  
- 🔐 **Análise de Cabeçalhos HTTP** (CSP, HSTS, X-Frame-Options, etc.)  
- 🏗️ **Identificação de Tecnologias Web** (CMS, frameworks, servidor web)  
- 🔍 **Busca por Arquivos Sensíveis** (`robots.txt`, `.env`, `config.php`, etc.)  
- 🌍 **Mapa Interativo de Servidores** (Leaflet.js + IP Geolocation API)  
- 🕵️ **Scanner de Portas** (via `nmap`)  
---

## 🚀 **Instalação e Uso**

### 📌 **1. Clone o repositório**
```bash
git clone https://github.com/joaolimareis/web-security-scanner.git
cd web-security-scanner
```

### 📌 **2. Instale as dependências**
> 🐍 **Requer Python 3.10+**  
```bash
pip install -r requirements.txt
```

### 📌 **3. Execute um scan de segurança**
Para escanear um único site:
```bash
python scanner.py --url example.com --save
```
Para escanear vários sites:
```bash
python scanner.py --url google.com github.com securityheaders.com --save
```
Para escanear sites de um arquivo:
```bash
python scanner.py --file sites.txt --save
```

### 📌 **4. Inicie o Dashboard**
> O Dashboard exibe os resultados de forma interativa.  
```bash
python dashboard.py
```
Acesse no navegador:
```
http://localhost:5000/
```

---

## 📊 **Funcionalidades**
✅ **Análise SSL/TLS:** Verifica o certificado digital e validade.  
✅ **Cabeçalhos HTTP:** Identifica headers importantes para segurança.  
✅ **Tecnologias Web:** Detecta frameworks backend/frontend.  
✅ **Arquivos Sensíveis:** Busca arquivos de configuração e logs expostos.  
✅ **Mapa de Servidores:** Exibe a geolocalização de domínios.  
✅ **Scanner de Portas:** Identifica portas abertas usando `nmap`.  
✅ **Resultados em JSON/CSV:** Para análise detalhada posterior.  

---

## 📜 **Exemplo de Saída JSON**
```json
{
  "SSL/TLS": {
    "domain": "google.com",
    "issued_to": "*.google.com",
    "valid_until": "2025-05-21",
    "is_valid": true
  },
  "Cabeçalhos HTTP": {
    "Content-Security-Policy": { "status": "❌ Ausente" },
    "Strict-Transport-Security": { "status": "✅ Presente" }
  },
  "Tecnologias Web": {
    "Servidor Web": "nginx",
    "CMS": "WordPress"
  },
  "Arquivos Sensíveis": {
    "robots.txt": { "status": "❌ Exposto", "url": "https://google.com/robots.txt" }
  },
  "Portas Abertas": {
    "80": "HTTP",
    "443": "HTTPS"
  }
}
```

---

## 🤝 **Contribuições**
Contribuições são bem-vindas! Para sugerir melhorias ou corrigir bugs:  
1. Faça um **fork** do repositório  
2. Crie um **branch** com sua feature: `git checkout -b minha-feature`  
3. Faça um **commit** das mudanças: `git commit -m "Adicionada nova funcionalidade"`  
4. Envie para análise: `git push origin minha-feature`  
5. Abra um **Pull Request** ✨  

---

## 📜 **Licença**
Este projeto está sob a licença **MIT**. Veja o arquivo [`LICENSE`](LICENSE) para mais detalhes.

🔗 **Criado por [joaolimareis](https://github.com/joaolimareis)**
![image](https://github.com/user-attachments/assets/d8108228-e738-4260-97b7-63f545d2b97d)
![image](https://github.com/user-attachments/assets/a8819105-34e9-443f-b850-7ad6815a10d2)


