pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                sh 'pytest --html=report.html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', fingerprint: true
            // Отправка в S3
            sh '''
                if [ -f report.html ]; then
                  aws s3 cp report.html s3://jenkins-html-report-ralex/report.html
                fi
            '''
        }
    }
}
