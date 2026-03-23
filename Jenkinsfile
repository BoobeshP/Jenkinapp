pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install OS Dependencies') {
            steps {
                sh '''
                sudo apt update
                sudo apt install -y python3.10-venv python3-pip
                '''
            }
        }

        stage('Setup Python Virtual Environment') {
            steps {
                sh '''
                python3 --version
                python3 -m venv ${VENV}
                . ${VENV}/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                . ${VENV}/bin/activate
                python -m unittest test_app.py
                '''
            }
        }

        stage('Package Application') {
            steps {
                sh '''
                tar -czf flask-app.tar.gz app.py requirements.txt
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Flask CI pipeline completed successfully'
        }
        failure {
            echo '❌ Flask CI pipeline failed'
        }
        always {
            cleanWs()
        }
    }
}
