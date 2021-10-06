pipeline {
    agent any
    stages {
        stage('delete origin zip file'){
            steps{
                sh 'rm -rf beanstalk-deploy.zip'
            }
        }
        stage('make zip file'){
            steps{
                sh 'zip beanstalk-deploy.zip ./*'
            }
        }
        stage('upload to S3'){
            steps{
                sh 'aws s3 cp beanstalk-deploy.zip s3://elasticbeanstalk-ap-northeast-1-090274807648 --region ap-northeast-1'
                
            }
        }
        stage('deploy'){
            steps{
                sh 'aws elasticbeanstalk create-application-version --region ap-northeast-1 --application-name django-tutorial --version-label from_s3_awscli --source-bundle S3Bucket="elasticbeanstalk-ap-northeast-1-090274807648",S3Key="beanstalk-deploy.zip"'
                sh 'aws elasticbeanstalk update-environment --region ap-northeast-1 --environment-name django-env --version-label from_s3_awscli'
            }
        }        
    }
}
