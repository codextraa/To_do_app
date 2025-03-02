#!/bin/sh
export INFISICAL_TOKEN=$(cat /run/secrets/infisical_token)
infisical run --env=dev --path="/To-do-app/frontend" -- npm run dev
