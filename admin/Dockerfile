FROM nginx:alpine

# Remove configuração padrão (opcional)
RUN rm -rf /usr/share/nginx/html/*

# Copia seus arquivos HTML
COPY . /usr/share/nginx/html

# Expõe a porta 80
EXPOSE 80

# Inicia o nginx
CMD ["nginx", "-g", "daemon off;"]