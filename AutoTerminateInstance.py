import boto3
import logging
import git
from datetime import datetime
import sys


class termination:

    def __init__(self):
        self.client = boto3.resource('ec2')
        self.repo = git.Repo('/home/ec2-user/gitrepo/helloword-chef')
        self.version = ""
    
    def commit_version (self):

        # Fetching the latest committed version data
        # Passing  committed version value to ec2_termination function if it's older than 3 days
        master = self.repo.head.reference
        self.version =  master.commit.hexsha
        commit_date = datetime.fromtimestamp(master.commit.committed_date)
        print master.commit.author.email
        today_date = datetime.now()
        days = ((today_date-commit_date).days)
        if days > 3:
            print "Committed Version", self.version
        else:
            print self.version, "Committed version isn't older than 3 days"
            sys.exit(1)

    def ec2_termination(self):

        #logging for INFO
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        # Retrieve to running instances.
        filters = [{
            'Name': 'tag:Version',
            'Values': [self.version]
            },
            {
            'Name': 'instance-state-name', 
            'Values': ['running']
            }
            ]
                    
        #filter the instances
        instances = self.client.instances.filter(Filters=filters)
        #print instances

        #locate all running instances
        RunningInstances = [instance.id for instance in instances]
                    
                    
        #Terminate the specific version instance which's older than 3 days
        if len(RunningInstances) > 0:
            #Terminate the instance
            Terminate = self.client.instances.filter(InstanceIds=RunningInstances).terminate()
            print Terminate
        else:
            print self.version, "Version Not Found"
     

def main():
    aws = termination()
    aws.commit_version()
    aws.ec2_termination()

if __name__ == '__main__':
    main()
