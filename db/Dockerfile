FROM postgres:16

ENV POSTGRES_USER=user
ENV POSTGRES_PASSWORD=urubu100
ENV POSTGRES_DB=msal_app

COPY ./init /docker-entrypoint-initdb.d

EXPOSE 5432
