pipeline {
    agent any
    stages {
        stage('git pull '){
            steps{
		sh 'whoami'
		sh 'pwd'
		sh 'ls -l'
		sh 'python3 -V'
		sh 'sudo eb --version' 
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
