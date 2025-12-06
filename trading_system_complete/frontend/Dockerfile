FROM node:20-alpine
WORKDIR /app

# Copy package files
COPY package.json package-lock.json ./

# Install dependencies
RUN npm ci

# Copy all other frontend files
COPY . .

# Expose port
EXPOSE 5173

# Run the development server
CMD ["npm", "run", "dev", "--", "--host"]