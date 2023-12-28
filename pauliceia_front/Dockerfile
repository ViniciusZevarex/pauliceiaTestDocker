# Use a imagem do Node.js na versão 8.17.0
FROM node:8.17.0

# Diretório de trabalho dentro do contêiner
WORKDIR /app/pauliceia_front

# Copiar o arquivo package.json e package-lock.json para o diretório de trabalho
COPY package*.json ./

# Instalar as dependências
RUN npm install -g npm@6.13.4
RUN npm install

# Copiar todo o código fonte para o contêiner
COPY . .

# Criar arquivo de variáveis de ambiente
RUN cp ./config/prod.env.js.EXAMPLE ./config/prod.env.js

# Porta em que a aplicação Vue.js está rodando
EXPOSE 8080

# Comando para iniciar a aplicação
CMD ["npm", "run", "dev"]
