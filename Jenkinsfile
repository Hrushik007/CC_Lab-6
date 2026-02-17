pipeline {
  agent any
  environment {
    REPO = "https://github.com/Hrushik007/CC_Lab-6.git"
  }
  stages {
    stage('Checkout') {
      steps {
        git url: env.REPO, branch: 'main'
      }
    }

    stage('Build Backend Image') {
      steps {
        sh '''
          cd backend
          docker build -t backend-app .
        '''
      }
    }

    stage('Deploy Backends') {
      steps {
        sh '''
          # remove any existing backends
          docker rm -f backend1 backend2 || true
          # run backends
          docker run -d --name backend1 --network lab-net -e BACKEND_NAME=backend1 backend-app
          sleep 3
          docker run -d --name backend2 --network lab-net -e BACKEND_NAME=backend2 backend-app || true
          sleep 3
        '''
      }
    }

    stage('Start NGINX LB') {
      steps {
        sh '''
          # clean old nginx
          docker rm -f nginx-lb || true
          docker run -d --name nginx-lb --network lab-net -p 80:80 nginx:latest
          sleep 2
          # copy nginx config and reload
          docker cp nginx/default.conf nginx-lb:/etc/nginx/conf.d/default.conf
          sleep 2
          docker exec nginx-lb nginx -s reload || true
        '''
      }
    }

    stage('Verify') {
      steps {
        sh '''
          echo "Listing running containers:"
          docker ps --format "{{.Names}}\t{{.Image}}\t{{.Status}}"
        '''
      }
    }
  }
  post {
    always {
      echo "Pipeline finished. Check http://localhost in your browser."
    }
  }
}
