#!groovy
import hudson.EnvVars
import jenkins.model.*

node {
    stage('Fetch'){
        echo "PARAMETERS"
        echo "=========="
        echo "$params.first_commit"
        git branch: 'master'
        git bisect: 'reset'
    }
    
    stage('Bisect'){
        gitbisect badEndCommit: "$params.last_commit", 
            continuesBuild: true, 
            gitCommand: 'git', 
            goodStartCommit: "$params.first_commit", 
            jobToRun: 'tester', 
            minSuccessfulIterations: 1, 
            overrideGitCommand: false, 
            retryCount: 0, 
            revisionParameterName: 'REVISION', 
            searchIdentifier: "$params.search"
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
