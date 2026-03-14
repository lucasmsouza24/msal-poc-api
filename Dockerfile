FROM condaforge/miniforge3:latest

WORKDIR /app

COPY environment.yaml .

RUN mamba env update -n base -f environment.yaml && \
    mamba clean --all --yes

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
