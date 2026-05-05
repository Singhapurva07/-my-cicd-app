pipeline {
    agent any
    environment {
        DOCKERHUB_USERNAME = "apurva297"
        IMAGE_NAME = "my-app"
        IMAGE_TAG = "latest"
    }
    stages {
        stage('Code Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG} .'
            }
        }
        stage('Docker Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker push ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}'
                }
            }
        }
        stage('Kubernetes Deploy') {
            steps {
                sh 'kubectl apply -f deployment.yaml --validate=false'
                sh 'kubectl rollout status deployment/my-app --timeout=60s'
            }
        }
        stage('Verify') {
            steps {
                sh 'kubectl get pods'
                sh 'kubectl get services'
            }
        }
    }
    post {
        success {
            echo '✅ Pipeline Complete! App Deployed!'
        }
        failure {
            echo '❌ Pipeline Failed!'
        }
    }
}
