# Logs-Analysis-Project
This is created to upload the code for Logs Analysis Project in Udacity. 
This report is being extracted based on the data from the below tables. 
The database includes three tables:

The `authors` table includes information about the authors of articles.
The `articles` table includes the articles themselves.
The `log` table includes one entry for each time a user has accessed the site.

# Files
This Project consists of three files that you will see in the repository. 
### Source.py : 
_This is the file needs to be executed inorder to see the results of the Logs Analysis_
### output.txt: 
_This file has the sample output returned one executing the Source.py_


# Instructions to Operate Code
* Install the VM setup from this [link](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0)
* Install Vagrant from [here](https://www.vagrantup.com/downloads.html)
* Use Github to fork and clone this [Repo](https://github.com/udacity/fullstack-nanodegree-vm) for VM configuration
* Start Virtual Machine with these commands 'vagrant.up' and 'vagrant.ssh'
* Download the data from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) for importing the necessary tables and data.
You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.
To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.
* Check this [link](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/262a84d7-86dc-487d-98f9-648aa7ca5a0f/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91) for more info on how to complete the setup
* After the setup is done, Run the `Source.py` python file in the command line. This will bring up the results. 
