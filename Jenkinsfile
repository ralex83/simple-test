pipeline {
    agent any

    environment {
        AWS_SHARED_CREDENTIALS_FILE = '/home/jenkins/.aws/credentials'
        AWS_CONFIG_FILE = '/home/jenkins/.aws/config'
    }

    stages {
        stage('Prepare Environment') {
            steps {
                sh '''
                    python3 -m venv ci-cd-env
                    bash -c "source ci-cd-env/bin/activate && pip install -r requirements.txt"
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    bash -c "source ci-cd-env/bin/activate && pytest --html=report.html --self-contained-html"
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', fingerprint: true
            sh '''
                if [ -f report.html ]; then
                    DATE=$(date +%Y-%m-%d_%H-%M-%S)
                    aws s3 cp report.html s3://jenkins-html-report-ralex/report_$DATE.html
                fi
            '''
        }
    }
}
