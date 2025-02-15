pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Sahil-bhagchandani/git-practice'
            }
        }

        stage('Build') {
            steps {
                echo 'Simulating Build Process...'
                bat 'echo "Build Successful" > build.log'
            }
        }

        stage('Test') {
            steps {
                echo 'Simulating Test Execution...'
                bat 'echo "All Tests Passed" > test.log'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Simulating Deployment...'
                bat 'echo "Deployment Successful" > deploy.log'
            }
        }
    }
}
