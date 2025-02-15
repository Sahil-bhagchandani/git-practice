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
                sh 'echo "Build Successful" > build.log'
            }
        }

        stage('Test') {
            steps {
                echo 'Simulating Test Execution...'
                sh 'echo "All Tests Passed" > test.log'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Simulating Deployment...'
                sh 'echo "Deployment Successful" > deploy.log'
            }
        }
    }
}
