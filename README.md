# <h1> AutoTerminateInstance 

<h4> Prerequisite </h4> To install the python & boto3 modules 

* Here’s the details of required modules which needs to be installed to execute the python script successfully. <br>
	⁃	<i> boto3		- sudo pip install boto3 <br>
	⁃	datetime 	- sudo pip install DateTime <br>
	⁃	gitpython 	- sudo pip install gitpython </i> <br>
		
* You would need to install the awscli package to connect with AWS API. 

	Command to configure the Access & Secret access key. 

	⁃	<i> AWS config </i> 

	Note - It will prompt you to enter Access key, Secret access key, Output & Default region

* Specify the local path of git clone repository where you want to verify the latest committed version. 

	⁃	<i> self.repo = git.Repo('/home/ec2-user/gitrepo/helloword-chef') </i>


<h4> Troubleshooting Steps </h4>

If you are getting permission denied error message while executing the python script, please check user permissions. User should have the required permission to terminate the AWS instance.  

