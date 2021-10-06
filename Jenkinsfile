pipeline {
    agent any
    stages {
        stage('git pull '){
            steps{
		sh 'whoami'
		sh 'pwd'
		sh 'ls -l'
		sh 'python3 -V'
		sh 'python3 -m pip install awsebcli'
		sh 'python3 -m pip list'
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
