FROM postgres:15

WORKDIR /app
RUN apt-get update && apt-get install -y curl && curl -1sLf 'https://dl.cloudsmith.io/public/infisical/infisical-cli/setup.deb.sh' | bash && apt-get install -y infisical
COPY . .
RUN chmod +x /app/run.sh
RUN chmod +x /app/test.sh