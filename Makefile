DC = docker-compose

# Build the Docker images
build:
	$(DC) build
	pip install --no-cache-dir -r requirements.txt

# Bring up the services in the background
up:
	$(DC) up -d

# Bring down the services
down:
	$(DC) down

# View logs
logs:
	$(DC) logs

# Rebuild and restart services
rebuild:
	$(DC) down
	$(DC) build
	$(DC) up -d


# Target for making sure Makefile runs correctly
.PHONY: build up down logs rebuild
