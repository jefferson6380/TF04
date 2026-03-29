# Funcionamento do arquivo nginx.conf

## 🧠 Objetivo

- Distribuir requisições entre múltiplos servidores backend  
- Melhorar desempenho e escalabilidade  
- Simular ambiente real com containers Docker  
- Utilizar Nginx como proxy reverso e load balancer  


## 🏗️ Arquitetura

- 🌐 **Nginx** → Proxy reverso + Load Balancer  
- ⚙️ **Backend (múltiplos containers)**  
- 🎨 **Frontend**  
- 🐳 **Docker Compose** para orquestração  

---

## ⚖️ Load Balancer (`load-balancer.conf`)

Este arquivo configura o balanceamento de carga utilizando o Nginx.

### 🔁 Cluster de servidores

upstream backend_cluster {
    server backend1:3000;
    server backend2:3000;
    server backend3:3000;
}

## 📊 Logs

O Nginx registra informações como:

IP do cliente
Data e hora
Requisição
Status HTTP
Navegador
Servidor que respondeu (upstream)
🚀 Resumo

O Nginx neste projeto atua como:

⚖️ Balanceador de carga
🌐 Proxy reverso
🗜️ Compressor de dados
📊 Gerador de logs
🧩 Gerenciador modular de configurações