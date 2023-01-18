pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '10'))
    }
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('H/30 * * * *')])])
                }
                git branch: 'main', url: 'https://github.com/YfatZ/Python_Frontend_and_Backend_Stack.git'
            }
        }
        stage('run python') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'python 1.py'
                    } else {
                        sh 'python 1.py'
                    }
                }
            }
        }
        stage('run backend server') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'start /min python rest_app.py'
                    } else {
                        sh 'start /min python rest_app.py'
                    }
                }
            }
        }
        stage('run frontend server') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'start /min python web_app.py'
                    } else {
                        sh 'start /min python web_app.py'
                    }
                }
            }
        }
        stage('run backend_testing') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'python backend_testing.py'
                    } else {
                        sh 'python backend_testing.py'
                    }
                }
            }
        }
        stage('run frontend_testing') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'python frontend_testing.py'
                    } else {
                        sh 'python frontend_testing.py'
                    }
                }
            }
        }
        stage('run combined_testing') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'python combined_testing.py'
                    } else {
                        sh 'python combined_testing.py'
                    }
                }
            }
        }
        stage('cleaning - stoping servers') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'python clean_environemnt.py'
                    } else {
                        sh 'python clean_environemnt.py'
                    }
                }
            }
        }
    }
}

def checkOs(){
    if (isUnix()) {
        def uname = sh script: 'uname', returnStdout: true
        if (uname.startsWith("Darwin")) {
            return "Macos"
        }
        else {
            return "Linux"
        }
    }
    else {
        return "Windows"
    }
}