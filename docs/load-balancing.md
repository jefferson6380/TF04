# funcionamento do arquivo load-balancer.conf

    Esse arquivo é um balanceador de carga. 

    "upstream backend_cluster" cria um cluster de containers para serem usados de forma intercambiável caso algum venha a falhar.

    "least_conn" distribui os acessos para o coneiner com menos conexão.

    "Gzip" comprime os arquivos e diretórios para serem enviados mais rápidos para o navegador.

    "limit_req" limita a quantidade de requisições.

    Esse arquivo também faz o proxy para servir html estático e proxy reverso para acessar o backend
