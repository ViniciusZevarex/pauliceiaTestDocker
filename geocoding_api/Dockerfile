# Use a imagem mais recente do Node.js
FROM node:latest

# Set the working directory
WORKDIR /usr/src/app/geocoding_api

# Copiar o arquivo package.json e package-lock.json para o diretório de trabalho
COPY package*.json ./

# Instalar as dependências
RUN npm install

# Install Supervisor
RUN npm install -g supervisor

# Copiar todo o código fonte para o contêiner
COPY . .

# Porta em que a aplicação Vue.js está rodando
EXPOSE 3000

# Comando para iniciar a aplicação
CMD ["npm", "start"]
