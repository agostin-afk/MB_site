#!/bin/sh

# O shell irá encerrar a execução do script quando um comando falhar
set -e

echo "Executando commands.sh"

wait_psql.sh
collectstatic.sh
migrate.sh
runserver.sh