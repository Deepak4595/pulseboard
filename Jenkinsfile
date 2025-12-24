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
                python3 -m venv venv
                source venv/bin/activate
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Application') {
        steps {
            sh '''
            cd /var/lib/jenkins/workspace/pulseboard-pipeline
            pkill -f app.py || true
            nohup ./venv/bin/python app.py > app.log 2>&1 &
            '''
           }
       }
    } 
}
