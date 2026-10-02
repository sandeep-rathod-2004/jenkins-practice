pipeline {
    agent any

    stages {

        stage('System Check') {
            steps {
                sh 'java -version'
                sh 'git --version'
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Build') {
            steps {
                sh 'echo "Building application..."'
            }
        }

        stage('Test') {
            steps {
                sh 'echo "Running tests..."'
            }
        }

        stage('Finish') {
            steps {
                sh 'echo "CI pipeline completed successfully!"'
            }
        }
    }
}
