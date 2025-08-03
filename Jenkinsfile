pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                sh '''
                    source ci-cd-env/bin/activate
                    pytest --html=report.html
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', fingerprint: true
            sh '''
                if [ -f report.html ]; then
                  aws s3 cp report.html s3://jenkins-html-report-ralex/report.html
                fi
            '''
        }
    }
}
