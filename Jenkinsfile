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

    stage('Run tests (inside Python container)') {
      steps {
        sh '''
          docker run --rm -v "$PWD":/src -w /src python:3.10-slim /bin/sh -c "
            pip install --no-cache-dir -r requirements.txt &&
            mkdir -p reports &&
            pytest --junitxml=reports/junit-report.xml || true
          "
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
  } // stages

  post {
    always { echo "Finished build ${env.BUILD_NUMBER}" }
  }
}
