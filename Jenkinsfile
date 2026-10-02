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
                sh 'docker build -t jenkins-practice:latest .'
            }
        }

        stage('Docker Test') {
            steps {
                sh 'docker run --rm jenkins-practice:latest'
            }
        }

        stage('Finish') {
            steps {
                echo 'CI + Docker pipeline completed successfully!'
            }
        }
    }
}
