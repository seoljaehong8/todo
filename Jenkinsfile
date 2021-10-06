pipeline {
    agent any
    stages {
        stage('git pull '){
            steps{
		sh 'eb --version'
		sh 'git config --list'
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
