pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Deepak4595/pulseboard.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv venv || true
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                ./venv/bin/pip install --upgrade pip
                ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Restart PulseBoard Service') {
            steps {
                sh '''
                sudo systemctl restart pulseboard
                '''
            }
        }

    }
}

