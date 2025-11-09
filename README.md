\# ACEest Fitness — CI/CD Assignment Submission



\*\*Student:\*\* Neha Gupta  

\*\*BITS ID:\*\* 2024ht66038  

\*\*Date:\*\* November 2025  



---



\## 📘 Project Overview

ACEest Fitness is a simple Flask-based microservice built to demonstrate a complete DevOps CI/CD pipeline.  

The goal of this assignment is to showcase continuous integration, containerization, automated testing, and deployment using popular DevOps tools.



This project includes:

\- Continuous Integration with \*\*pytest\*\* and \*\*Jenkins\*\*

\- Continuous Delivery with \*\*Docker\*\* and \*\*Docker Hub\*\*

\- Continuous Deployment using \*\*Kubernetes (Minikube)\*\*

\- Code Quality Analysis with \*\*SonarQube\*\*



---



\## 🗂️ Folder Structure

aceest-fitness/

│

├── ACEest\_Fitness.py # Flask app entry point

├── requirements.txt

├── Dockerfile

├── .dockerignore

├── Jenkinsfile

├── README.md

│

├── app/

│ ├── init.py

│ └── routes.py

│

├── tests/

│ └── test\_routes.py

│

├── k8s/

│ ├── deployment.yaml

│ ├── service.yaml

│ ├── ingress.yaml

│ ├── deploy-green.yaml

│ └── canary.yaml

│







\## ⚙️ Setup Instructions (Windows PowerShell)



\### 1️⃣ Create a Virtual Environment

```powershell

cd "E:\\aceest-fitness"

python -m venv venv

.\\venv\\Scripts\\Activate.ps1

pip install --upgrade pip

pip install -r requirements.txt



2️⃣ Run Flask App Locally

python ACEest\_Fitness.py

Now visit:



http://127.0.0.1:5000/



http://127.0.0.1:5000/health



Expected Output:

{"message": "ACEest Fitness API running"}



3️⃣ Run Unit Tests (CI Validation)

powershell

pytest -q

pytest --junitxml=reports/junit-report.xml

✅ Expected Output:

3 passed in ... seconds



4️⃣ Build and Run Docker Image

powershell

docker build -t aceest-fitness:local .

docker run --rm -p 5000:5000 aceest-fitness:local

Now open http://127.0.0.1:5000/ to confirm it runs inside a container.



5️⃣ Tag and Push to Docker Hub

powershell

docker tag aceest-fitness:local nehag0308/aceest-fitness:v1.0

docker login

docker push nehag0308/aceest-fitness:v1.0

docker push nehag0308/aceest-fitness:latest



6️⃣ Deploy to Kubernetes (Minikube)

powershell

minikube start --driver=docker

kubectl apply -f k8s/deployment.yaml

kubectl apply -f k8s/service.yaml

kubectl get pods

minikube service aceest-svc --url

Use the URL printed to access the deployed Flask app.



7️⃣ Deployment Strategies

Rolling Update

powershell

kubectl set image deployment/aceest-fitness aceest-fitness=<your-dockerhub-username>/aceest-fitness:v1.1 --record

kubectl rollout status deployment/aceest-fitness



Blue-Green Deployment

powershell

kubectl apply -f k8s/deploy-green.yaml

kubectl patch svc aceest-svc -p '{"spec":{"selector":{"app":"aceest-fitness","version":"green"}}}'



Canary Deployment

powershell

kubectl apply -f k8s/canary.yaml



8️⃣ Run SonarQube for Code Quality

powershell

docker run -d --name sonarqube -p 9000:9000 sonarqube:community

Then open http://localhost:9000, create a project, and run:

docker run --rm -e SONAR\_HOST\_URL="http://host.docker.internal:9000" -v "${PWD}":/usr/src sonarsource/sonar-scanner-cli -Dsonar.login=<SONAR\_TOKEN>









