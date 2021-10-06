pipeline {
    agent any
    stages {
        stage('git pull '){
            steps{
                sh 'aws --version'
                sh 'aws s3 ls'
                
            }
        }
        stage('eb deploy'){
            steps{
                sh 'eb deploy -l fromjenkins'
            }
        }        
    }
}
