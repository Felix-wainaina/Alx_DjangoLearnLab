# Deployment Configuration

This document outlines the basic Nginx configuration required to serve the Django application over HTTPS, as required by Task 3.

## Nginx Configuration for HTTPS

To deploy this project with HTTPS, a web server like Nginx is used as a reverse proxy. It will handle SSL/TLS termination and forward requests to the Gunicorn application server.

**Prerequisites:**
1.  A domain name.
2.  An SSL/TLS certificate (e.g., from Let's Encrypt).
3.  Gunicorn installed and configured.

### Example `nginx.conf`

This configuration listens on port 443 (HTTPS), serves static and media files directly, and proxies all other requests to Gunicorn. It also includes the HSTS header, although Django also provides this.

```nginx
server {
    listen 80;
    server_name your_domain.com www.your_domain.com;
    
    # Redirect all HTTP traffic to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    server_name your_domain.com www.your_domain.com;

    # SSL Certificate Paths
    ssl_certificate /path/to/your/fullchain.pem;
    ssl_certificate_key /path/to/your/privkey.pem;

    # Security Headers
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
    
    # Serve static files
    location /static/ {
        alias /path/to/your/project/staticfiles/;
    }

    # Serve media files
    location /media/ {
        alias /path/to/your/project/media/;
    }

    # Proxy requests to Gunicorn
    location / {
        proxy_pass http://unix:/path/to/your/project/gunicorn.sock;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}