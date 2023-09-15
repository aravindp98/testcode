import jenkins
import os


jenkins_url = jenkins.Jenkins("http://172.31.10.31:8080/", username=os.environ.get('new_jenkins_usr'), password=os.environ.get('new_jenkins_pass'))


def trigger_build():
    job_name = 'sonarqube_gitlab'
    parameter_name = 'repository1'
    parameter_description = 'gitlab repository url'
    choices = 'https://gitlab.com/aravindp98/build_trigger.git, https://gitlab.com/dev-ops24/Demo-test.git'
    default_value = 'https://gitlab.com/aravindp98/build_trigger.git'

    job_config = jenkins_url.get_job_config(job_name)

    new_parameter_xml = f'''
    <hudson.model.ChoiceParameterDefinition>
        <name>{parameter_name}</name>
        <description>{parameter_description}</description>
        <choices class="java.lang.String">{choices}</choices>
        <defaultValue>{default_value}</defaultValue>
    </hudson.model.ChoiceParameterDefinition>
    '''

    new_config = job_config.replace('</parameterDefinitions>', f'{new_parameter_xml}</parameterDefinitions>')

    jenkins_url.reconfig_job(job_name, new_config)
    parameter = {'repository': 'https://gitlab.com/dev-ops24/Demo-test.git'}
    jenkins_jobs = jenkins_url.build_job(name="sonarqube_gitlab", parameters=parameter)


trigger_build()