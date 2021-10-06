pipeline {
    agent any
    stages {
        stage('git pull '){
            steps{
                sh 'aws --version'
                
            }
        }
        stage('eb deploy'){
            steps{
                sh 'eb deploy -l fromjenkins'
            }
        }        
    }
}
