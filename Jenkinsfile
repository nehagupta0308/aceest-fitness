pipeline {
  agent any
  environment {
    IMAGE = "nehag0308/aceest-fitness"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    // === TESTS stage using docker agent ===
    stage('Run tests (in python container)') {
      // use the python image as the agent for this stage
      agent {
        docker {
          image 'python:3.10-slim'
          // reuse host network if needed: args '-v /var/run/docker.sock:/var/run/docker.sock'
          // args '' 
        }
      }
      steps {
        sh '''
          pip install --no-cache-dir -r requirements.txt
          mkdir -p reports
          pytest --junitxml=reports/junit-report.xml || true
        '''
      }
      post {
        always {
          junit 'reports/junit-report.xml'
        }
      }
    }

    stage('Build Docker image') {
      steps {
        sh "docker build -t ${IMAGE}:${BUILD_NUMBER} ."
      }
    }

    stage('Push to Docker Hub') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh '''
            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
            docker push ${IMAGE}:${BUILD_NUMBER}
            docker tag ${IMAGE}:${BUILD_NUMBER} ${IMAGE}:latest
            docker push ${IMAGE}:latest
          '''
        }
      }
    }
  }

  post {
    always {
      echo "Pipeline finished. Build #${env.BUILD_NUMBER}"
    }
    success { echo "Build succeeded." }
    failure { echo "Build failed." }
  }
}
