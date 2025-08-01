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
        }
    }
}
