#!/bin/sh
export INFISICAL_TOKEN=$(cat /run/secrets/infisical_token)
infisical run --env=dev --path="/To-do-app/frontend" -- sh -c '
    echo "$local_ca" > /tmp/local-ca.pem && 
    export NODE_EXTRA_CA_CERTS=/tmp/local-ca.pem && 
    npm run dev
'