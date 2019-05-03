#!groovy
import hudson.EnvVars
import jenkins.model.*

node {
    stage('Fetch'){
        echo "PARAMETERS"
        echo "=========="
        echo "$params.first_commit"
        git branch: 'master',
            url: 'https://github.com/hussopa/SWD4TA002-3001/'
    }
    
    stage('Bisect'){
        gitbisect
    }
    
    stage('Build'){
        
    }
    
    stage('Load'){
        
    }
    
    stage('Test'){
        
    }
    
    stage('Postbuild actions'){
        
    }
}
