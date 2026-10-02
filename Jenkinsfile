pipeline {
    agent any

    stages {

        stage('Environment') {
            steps {
                sh 'echo "Job Name: $JOB_NAME"'
                sh 'echo "Build Number: $BUILD_NUMBER"'
                sh 'echo "Workspace: $WORKSPACE"'
                sh 'echo "Build URL: $BUILD_URL"'
            }
        }

        stage('Show Parameters') {
            steps {
                echo "Selected Environment: ${params.ENVIRONMENT}"
                echo "Run Tests: ${params.RUN_TESTS}"
            }
        }

        stage('Build') {
            steps {
                sh 'python3 --version'
                sh 'python3 -m py_compile app.py'
                echo 'Python application syntax check passed'
            }
        }

        stage('Test') {
            when {
                expression {
                    params.RUN_TESTS
                }
            }
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
                    docker rm -f jenkins-test 2>/dev/null || true

                    docker run -d \
                        --name jenkins-test \
                        -e APP_ENV=${ENVIRONMENT} \
                        sandeep352004/jenkins-practice:build-${BUILD_NUMBER}

                    sleep 3

                    docker exec jenkins-test \
                        python3 -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:5000').read().decode())"

                    docker rm -f jenkins-test
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
                        echo "$DOCKER_TOKEN" | docker login \
                            -u "$DOCKER_USER" \
                            --password-stdin

                        docker push \
                            sandeep352004/jenkins-practice:build-${BUILD_NUMBER}

                        docker push \
                            sandeep352004/jenkins-practice:latest

                        docker logout
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker rm -f jenkins-app 2>/dev/null || true

                    docker run -d \
                        --name jenkins-app \
                        -p 5000:5000 \
                        -e APP_ENV=${ENVIRONMENT} \
                        sandeep352004/jenkins-practice:build-${BUILD_NUMBER}

                    sleep 3

                    docker ps --filter "name=jenkins-app"
                '''
            }
        }

        stage('Deployment Test') {
            steps {
                sh '''
                    docker exec jenkins-app \
                        python3 -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:5000').read().decode())"
                '''
            }
        }

        stage('Finish') {
            steps {
                echo "======================================"
                echo "CI/CD PIPELINE COMPLETED"
                echo "======================================"
                echo "Build Number : ${BUILD_NUMBER}"
                echo "Environment  : ${params.ENVIRONMENT}"
                echo "Docker Image : sandeep352004/jenkins-practice:build-${BUILD_NUMBER}"
                echo "Application  : http://localhost:5000"
                echo "======================================"
            }
        }
    }
}
