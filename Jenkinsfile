pipeline {
    agent any
    stages {
        stage('git pull '){
            steps{
                sh 'git pull origin master' 
            }
        }
        stage('eb deploy'){
            steps{
                sh 'eb deploy -l fromjenkins'
            }
        }        
    }
}
