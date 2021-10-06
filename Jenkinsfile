pipeline {
    agent any
    stages {
        stage('delete origin zip file'){
            steps{
                sh 'cd server && ls -al && rm -rf *.zip'
            }
        }
        stage('make zip file'){
            steps{
                sh 'cd server && zip -r beanstalk_${BUILD_NUMBER}.zip .'
            }
        }
        stage('upload to S3'){
            steps{
                sh 'cd server && aws s3 cp beanstalk_${BUILD_NUMBER}.zip s3://elasticbeanstalk-ap-northeast-1-090274807648 --region ap-northeast-1'
                
            }
        }
        stage('deploy'){
            steps{
                sh 'aws elasticbeanstalk create-application-version --region ap-northeast-1 --application-name django-tutorial --version-label beanstalk_${BUILD_NUMBER} --source-bundle S3Bucket="elasticbeanstalk-ap-northeast-1-090274807648",S3Key="beanstalk_${BUILD_NUMBER}.zip"'
                sh 'aws elasticbeanstalk update-environment --region ap-northeast-1 --environment-name django-env --version-label beanstalk_${BUILD_NUMBER}'
            }
        }        
    }
}
