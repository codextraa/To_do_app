#!/bin/bash
export INFISICAL_TOKEN=$(cat /run/secrets/infisical_token)
infisical run --env=dev --path="/To-do-app/docker" -- sh -c "/usr/local/bin/docker-entrypoint.sh postgres"
