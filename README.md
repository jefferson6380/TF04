# TF04 - E-commerce com Load Balancer Avançado

## Aluno
- **Nome:** Jefferson
- **RA:** 6324617
- **Curso:** Análise e Desenvolvimento de Sistemas

## Arquitetura
- **Nginx:** Load balancer com SSL e rate limiting
- **Backend:** 3 instâncias da API para alta disponibilidade
- **Frontend:** Loja virtual estática
- **Admin:** Painel administrativo

## Funcionalidades Implementadas
-  Load balancing com algoritmo least_conn
-  Health checks automáticos
-  Failover transparente
-  SSL/TLS com certificado self-signed
-  Rate limiting para proteção
-  Logs detalhados com upstream info
-  Compressão gzip
-  Virtual hosts

## Como Executar

### Pré-requisitos
- Docker e Docker Compose

### Execução

git clone [https://github.com/jefferson6380/TF04.git]

cd TF04

docker-compose up --build -d

## verifique os servicos (opcional):
  execute: docker compose config --services
  ou
  execute: docker compose ps

## Endpoints
Frontend: http://localhost ou https://localhost
API: http://localhost/api/
Admin: http://localhost/admin/
Status: http://localhost/nginx-status
Health: http://localhost/health


# Testes

### Load Balancing
  execute: curl http://localhost/api/
  
  ou:
  acesse  http://localhost/ e presione "Testar API" para alterar entre os containers backend

## Failover (simular queda)

derrube algum container, examplo: docker stop backend3
verifique os containers:
execute curl http://localhost/api/ algumas vezes ou click em "Teste API" para verificar on containers

## Simular limite de requisiçõse
  click varias vezes em "Testar API"
  
  ou:
  execute: for i in {1..10}; do curl -s http://localhost/api/; echo; done
  irá retornar um html de erro 503 com muitas requisiçoes

## verificar métricas
  acesse:  http://localhost/nginx-status

## verifique health
 acesse: http://localhost/health



