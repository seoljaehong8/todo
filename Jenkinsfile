pipeline {
    agent any
    stages {
        stage('git pull '){
            steps{
                sh 'aws --version'
                sh 'aws s3 ls'
                sh 'pwd'
                sh 'ls -al'
                
            }
        }
        stage('eb deploy'){
            steps{
                sh 'eb deploy -l fromjenkins'
            }
        }        
    }
}
