#!/bin/sh
export INFISICAL_TOKEN=$(cat /run/secrets/infisical_token)
infisical run --env=dev --path="/To-do-app/docker" -- sh -c 'pg_isready -U "$POSTGRES_USER" -d "$POSTGRES_DB" || { echo "pg_isready failed with exit code $?" >&2; exit 1; }'