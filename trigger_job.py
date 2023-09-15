import jenkins
import os
import jenkinsapi

jenkins_url = jenkins.Jenkins("http://172.31.10.31:8080/", username=os.environ.get('new_jenkins_usr'), password=os.environ.get('new_jenkins_pass'))


def trigget_build():
    parameter = {'repository': 'https://gitlab.com/dev-ops24/Demo-test.git'}
    jenkins_jobs = jenkins_url.build_job(name="sonarqube_gitlab", parameters=parameter)

trigget_build()