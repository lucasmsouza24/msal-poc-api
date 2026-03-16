# MSAL POC API

![Python](https://img.shields.io/badge/python-3.14+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/docker-containerized-2496ED?logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-orchestration-326CE5?logo=kubernetes&logoColor=white)

This repository contains a simple API used to test authentication with Microsoft Identity Platform using MSAL.

The goal of this project is purely educational: to understand how MSAL authentication works in a real application and how it can be integrated with a backend service. Every successful authentication event is stored in a PostgreSQL database for logging purposes.

This repository contains only the backend API. The frontend used to trigger the authentication flow can be found here:

Frontend repository:
https://github.com/lucasmsouza24/msal-poc-frontend

The system can be executed locally using either **Docker** or **Kubernetes (Minikube)**.

---

# Architecture

The project is composed of two repositories:

Frontend  
React application responsible for starting the MSAL authentication flow.

Backend (this repository)  
FastAPI application responsible for:

- Handling MSAL authentication callback
- Validating authentication responses
- Persisting authentication events into PostgreSQL

Database  
PostgreSQL database used to store authentication logs.

---

# Requirements

This project was developed and tested on **Linux (Zorin OS 18)**. Other Linux distributions should work as well.

In addition to the local runtime environment, you must have a **Microsoft Entra ID (Azure AD) App Registration** configured for MSAL authentication.

The App Registration must include:

- A **Client ID**
- A **Client Secret**
- A configured **Redirect URI** that matches the backend callback endpoint

These values are required to populate the `.env` file used by the API.

To run the project you need one of the following environments:

### Option 1 — Docker

Required tools:

- Docker
- GNU Make

You must also have permission to run Docker commands.  
If Docker requires `sudo` on your system, you may need to modify the Makefile to prefix docker commands with `sudo`.

---

### Option 2 — Kubernetes (Minikube)

Required tools:

- Minikube (or any local Kubernetes cluster)
- kubectl
- GNU Make

Before running the Kubernetes build, make sure a cluster is already running:

~~~bash
minikube start
~~~


---

# Environment Variables

Create a `.env` file in the project root based on `.env.example`.

~~~bash
cp .env.example .env
~~~

You must configure the following MSAL values from your Azure App Registration:

- MSAL_CLIENT_ID
- MSAL_CLIENT_SECRET
- MSAL_AUTHORITY


The remaining variables depend on the runtime environment (Docker or Kubernetes).

The `.env.example` file already contains default values for both environments to make setup easier.

After copying the file, remember to **enable the configuration that matches your environment**:

- If you run the project with **Docker**, keep the Docker variables enabled and comment out the Kubernetes section.
- If you run the project with **Kubernetes**, keep the Kubernetes variables enabled and comment out the Docker section.

---

# Running with Docker

Start the full environment with:

~~~bash
make docker-build
~~~

This command will:

1. Create a Docker network
2. Build the PostgreSQL container
3. Build the API container
4. Start both services

The API will be available at:

~~~
http://localhost:8000/api
~~~

---

# Running with Kubernetes (Minikube)

Make sure a cluster is running:

~~~bash
minikube start
~~~

Then run:

~~~bash
make k8s-build
~~~

This command will:

1. Build container images using Minikube
2. Deploy PostgreSQL
3. Deploy the API
4. Create Kubernetes services

The API will be exposed through a local DNS:

~~~
https://msal.local/api
~~~

This DNS is configured through a Kubernetes **Ingress** defined in the frontend repository.

---

# Authentication Flow

The authentication process works as follows:

1. The user accesses the frontend application
2. The frontend triggers the Microsoft login using MSAL
3. Microsoft redirects the user back to the backend callback endpoint
4. The backend validates the authentication response
5. The authentication event is stored in PostgreSQL

---

# Notes

- This project is intended for learning and experimentation.
- It is not designed for production use.
- Secrets are loaded via environment variables.

---

# Related Repository

Frontend application used to start the authentication flow and configure the local Ingress (`msal.local`):

https://github.com/lucasmsouza24/msal-poc-frontend
