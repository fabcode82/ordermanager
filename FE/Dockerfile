# #dev
# FROM node:23 
# WORKDIR /app

# # Copy package files and install dependencies
# COPY package*.json /app/
# RUN npm install

# # Copy source code and build the application
# COPY . /app/
# RUN npm run build




# --- STAGE 1: BUILD ---
# Use a Node image to build the Vue application

FROM node:23 as build-stage
WORKDIR /app

# Copy package files and install dependencies
COPY package*.json /app/
RUN npm install

# Copy source code and build the application
COPY . /app/
RUN npm run build

# --- STAGE 2: PRODUCTION/SERVE ---
# Use a lightweight Nginx image to serve the static files
FROM nginx:alpine as production-stage

# Copy Nginx configuration (must be present in FE/nginx.conf)
# This is crucial for Vue Router's history mode (SPA routing)
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy the static files from the build stage to Nginx's web root
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Expose the standard HTTP port
EXPOSE 80

# Command to start Nginx
CMD ["nginx", "-g", "daemon off;"]
