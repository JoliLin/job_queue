.DEFAULT_GOAL := help # Sets default action to be help

define PRINT_HELP_PYSCRIPT # start of Python section
import re, sys

output = []
# Loop through the lines in this file
for line in sys.stdin:
	# if the line has a command and a comment start with
    	#   two pound signs, add it to the output
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		output.append("%-10s %s" % (target, help))
# Sort the output in alphanumeric order
output.sort()
# Print the help result
print('\n'.join(output))
endef
export PRINT_HELP_PYSCRIPT 
# End of python section

#NAME=rxys
THIS_FILE := $(lastword $(MAKEFILE_LIST))

.PHONY: help build up down logs

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

build:	## make build c=CONTAINER_NAME 
	docker build --no-cache -t $(c)
	

up_all: ## make up_all 
	docker-compose -f docker-compose.yml up --force-recreate --no-deps --build -d


up:	## make up c=CONTAINER_NAME
	docker-compose -f docker-compose.yml build --no-cache $(c)
	docker-compose -f docker-compose.yml up -d $(c) 

down:	## make down
	docker-compose down

rm: 	## rm target c=SERVICE_NAME
	docker-compose rm -s -v $(c)

logs:	## make logs
	docker-compose logs --tail=100 -f $(c)

ps:	## make ps
	docker-compose ps

prune: 	## 
	docker image prune
