FROM node:18-alpine

WORKDIR /app

# package.json ve package-lock.json'ı kopyala
COPY frontend/package*.json ./

# Bağımlılıkları yükle
RUN npm ci

# Uygulama kodunu kopyala
COPY frontend/ .

# Port
EXPOSE 3000

# Varsayılan komut
CMD ["npm", "run", "dev"]

