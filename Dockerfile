# ---- Base image ----
FROM python:3.10-slim

# ---- Set working directory ----
WORKDIR /app

# ---- Copy and install dependencies ----
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- Copy the rest of the application ----
COPY . .

# ---- Environment variables ----
ENV FLASK_APP=app
ENV PORT=5000

# ---- Expose port 5000 ----
EXPOSE 5000

# ---- Run the app with Gunicorn ----
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()"]
