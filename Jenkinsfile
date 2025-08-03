pipeline {
    agent any

    environment {
        AWS_SHARED_CREDENTIALS_FILE = '/home/jenkins/.aws/credentials'
        AWS_CONFIG_FILE = '/home/jenkins/.aws/config'
        VENV_DIR = "ci-cd-env"
    }

    stages {
        stage('Prepare Environment') {
            steps {
                sh 'python3 -m venv $VENV_DIR'
                sh 'bash -c ". $VENV_DIR/bin/activate && pip install -r requirements.txt"'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'bash -c ". $VENV_DIR/bin/activate && pytest --html=report.html --self-contained-html"'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', fingerprint: true
            sh '''
                if [ -f report.html ]; then
                    echo "Parsing report with GPT..."
                    ./ci-cd-env/bin/python3 gpt_log_parser.py

                    DATE=$(date +%Y-%m-%d_%H-%M-%S)
                    aws s3 cp report.html s3://jenkins-html-report-ralex/report_$DATE.html
                fi
            '''
        }
    }
}

