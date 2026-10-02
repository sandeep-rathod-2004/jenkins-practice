pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                sh 'python3 --version'
                sh 'python3 app.py'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pytest test_app.py'
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    docker build \
                      -t sandeep352004/jenkins-practice:build-${BUILD_NUMBER} \
                      -t sandeep352004/jenkins-practice:latest \
                      .
                '''
            }
        }

        stage('Docker Test') {
            steps {
                sh '''
                    docker run --rm sandeep352004/jenkins-practice:build-${BUILD_NUMBER}
                '''
            }
        }

        stage('Docker Push') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_TOKEN'
                    )
                ]) {
                    sh '''
                        echo "$DOCKER_TOKEN" | docker login -u "$DOCKER_USER" --password-stdin

                        docker push sandeep352004/jenkins-practice:build-${BUILD_NUMBER}
                        docker push sandeep352004/jenkins-practice:latest

                        docker logout
                    '''
                }
            }
        }

        stage('Finish') {
            steps {
                echo "CI/CD completed - Build ${BUILD_NUMBER}"
            }
        }
    }
}
