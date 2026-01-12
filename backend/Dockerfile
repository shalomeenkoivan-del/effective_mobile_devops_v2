FROM python:3.12.12-slim AS build
WORKDIR /app
COPY app.py .
RUN pip3 install flask --no-cache

FROM build
RUN useradd user && chown user /app/app.py
USER user
EXPOSE 8080
CMD python3 app.py