pipeline {
    agent any
    stages {
        stage('git pull'){
            steps{
                sh 'git pull origin2 master' 
            }
        }
        stage('eb deploy'){
            steps{
                sh 'eb deploy -l fromjenkins'
            }
        }        
    }
}