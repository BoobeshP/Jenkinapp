pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                python3 --version

                if python3 -m venv --help > /dev/null 2>&1; then
                    echo "Using virtual environment"
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                else
                    echo "python3-venv not available, using system Python"
                    pip3 install --user -r requirements.txt
                fi
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                if [ -d "venv" ]; then
                    . venv/bin/activate
                fi
                python3 -m unittest test_app.py
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
            echo "✅ Pipeline completed successfully"
        }
        failure {
            echo "❌ Pipeline failed"
        }
        always {
            cleanWs()
        }
    }
}
