pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'GitHub source code is ready'
            }
        }

        stage('Build') {
            steps {
                echo 'Building application'
            }
        }

        stage('Test') {
            steps {
                echo 'Tests completed'
            }
        }

        stage('Finish') {
            steps {
                echo 'CI pipeline successful!'
            }
        }

    }
}
