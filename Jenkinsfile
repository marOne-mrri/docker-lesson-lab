pipeline {
    agent any

    environment {
        IMAGE_NAME = 'my-web-app'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ./docker-build/static-app"
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Stop and remove existing container if exists
                    sh "docker rm -f ${IMAGE_NAME}-container || true"
                    // Run the new container
                    sh "docker run -d --name ${IMAGE_NAME}-container -p 8080:80 ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }
    }

    post {
        success {
            echo '✅ Build and deployment successful!'
        }
        failure {
            echo '❌ Build failed. Check logs for errors.'
        }
    }
}
