pipeline {
    agent {
        devopstest {
            label 'dev'
            // Run the pipeline in privileged mode
            customWorkspace '/home/ec2-user/jenkins-slave' // Change the path as needed
        }
    }
    
    environment {
        VERSION = '1.2.0'
        ARTIFACTORY_SERVER = 'http://3.84.26.167:8082/artifactory'
        ARTIFACTORY_USER = 'ciadmin'
        ARTIFACTORY_PASSWORD = 'Mani@12345'
        ARTIFACTORY_REPOSITORY = "store-artifacts/${VERSION}"
    }
    
    stages {
        stage('SCM Checkout') {
            steps{
            checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/devisettymanikanta/Radware-Task-Assignment.git']])
            }
        }
        stage('Build') {
            steps {
                sh 'echo "Building the application"'
                sh 'python3 zip_job.py'
            }
        }
        stage('Publish') {
            when {
                expression { currentBuild.result == 'SUCCESS' }
            }
            steps {
                sh 'echo "Deploying the application"'
                // Add your deployment commands here
                // Upload the zip files to Artifactory
                sh "curl -u ${env.ARTIFACTORY_USER}:${env.ARTIFACTORY_PASSWORD} -T *.zip ${env.ARTIFACTORY_SERVER}/${env.ARTIFACTORY_REPOSITORY}/"
            }
        }
    }
    
    post {
        success {
            sh 'echo "Pipeline succeeded"'
            // Send email notification for successful build
            emailext body: "The pipeline succeeded. Job: ${env.JOB_NAME} #${env.BUILD_NUMBER}\n\n${currentBuild.currentResult}",
                     subject: "Pipeline Success: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                     to: "${env.EMAIL_REQUESTOR}"
        }
        failure {
            sh 'echo "Pipeline failed"'
            // Send email notification for failed build
            emailext body: "The pipeline failed. Job: ${env.JOB_NAME} #${env.BUILD_NUMBER}\n\n${currentBuild.currentResult}",
                     subject: "Pipeline Failure: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                     to: "${env.EMAIL_REQUESTOR}"
        }
    }
    
    post {
        always {
            sh 'echo "Cleaning up workspace"'
            // Cleanup stage - delete the workspace
            cleanWs()
        }
    }
}
