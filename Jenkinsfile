```groovy
pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Test') {
            steps {
                sh 'python3 -m pip install --user -r requirements.txt --break-system-packages'
                sh 'python3 -m unittest -v'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
                        /var/jenkins_home/tools/hudson.plugins.sonar.SonarRunnerInstallation/SonarScanner/bin/sonar-scanner \
                        -Dsonar.projectKey=dvp-week12-sonarqube-docker \
                        -Dsonar.python.version=3.12 \
                        -Dsonar.tests=. \
                        -Dsonar.test.inclusions=test_*.py
                    '''
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    script {
                        def qg = waitForQualityGate()
                        if (qg.status != 'OK') {
                            error "Quality Gate failed: ${qg.status}"
                        }
                    }
                }
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t dvp-week12-app:latest .'
            }
        }

        stage('DockerHub Push') {
            steps {
                echo 'DockerHub credentials will be configured in Jenkins.'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Local deployment will be configured next.'
            }
        }
    }
}
```
