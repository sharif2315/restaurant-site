# Use Node.js LTS version as the base image
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files to the working directory
COPY . .

RUN npm run build

# Expose port 3000 for serving the application
EXPOSE 3000

# Command to start the development server
CMD ["npm", "run", "dev"]
