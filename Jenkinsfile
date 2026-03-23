pipeline {
    agent any

    environment {
        VENV = "venv"
        APP_PORT = "5000"
        APP_NAME = "flask-jenkins-app"
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

        stage('Run Application (Browser Access)') {
            steps {
                sh '''
                echo "Stopping any existing app..."
                sudo pkill -f app.py || true

                echo "Starting Flask app..."
                . ${VENV}/bin/activate
                nohup python app.py > app.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully"
            echo "🌐 Access app at: http://<JENKINS_SERVER_IP>:5000/health"
        }
        failure {
            echo "❌ Pipeline failed"
        }
        always {
            archiveArtifacts artifacts: 'flask-app.tar.gz, app.log', fingerprint: true
        }
    }
}
