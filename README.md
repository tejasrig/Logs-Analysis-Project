# Logs-Analysis-Project
This is created to upload the code for Logs Analysis Project in Udacity. We are using PostgreSQL database for a fictional news website for extracting the Report
This report is being extracted based on the data from the below tables. The database includes the below three tables:

  * The `authors` table includes information about the authors of articles.
  * The `articles` table includes the articles themselves.
  * The `log` table includes one entry for each time a user has accessed the site.
  
Below is the data that is primarily being extracted using this code. 
  * What are the most popular three articles of all time? 
  * Who are the most popular article authors of all time?
  * On which days did more than 1% of requests lead to errors? 
  
# Files
This Project consists of three files that you will see in the repository. 
### Source.py : 
_This is the file needs to be executed inorder to see the results of the Logs Analysis_
### output.txt: 
_This file shows the sample output returned on executing the Source.py_


# Instructions to Operate Code
* VM set up has to be installed first inorder to execute this code. We're using tools called Vagrant and VirtualBox to install and manage the VM
* Install Vagrant from [here](https://www.vagrantup.com/downloads.html)
* Install Virtualbox from [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* Use the terminal to execute the scripts and commands. If you are using a Mac or Linux system, your regular terminal program will do just fine. On Windows, we recommend using the Git Bash terminal that comes with the Git software. If you don't already have Git installed, download Git from [git-scm.com](https://git-scm.com/downloads)
* Start Virtual Machine with these commands `vagrant up` and `vagrant ssh`
* Download the data from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) for importing the necessary tables and data.
You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.
To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.
* Run `psql <databasename>` to execute the SQL scripts
* To Run the python file, change directory by running `cd /vagrant` and execute the python file with the command `python Source.py`. This will bring up the results. 
