# Logs Analysis

## Project Description
- This projects looks at extracting information from a database using SQL.
- This script log_queries.py answers three questions useful for real-life situations.

## Requirements
- Get Virtual Box - https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
- Get Vagrant - https://www.vagrantup.com/downloads.html
- Get the vagrantfile - https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip
- Start the vagrant VM by running 'vagrant up' from inside the vagrant sub directory
- You can now get in to the VM by running 'vagrant ssh'

## Database Set-up
- Download the files here -  https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
- Put the file 'newsdata.sql' into the vagrant directory
- From that directory, run 'psql -d news -f newsdata.sql' to build the database

## How to run
Execute using a python3 interpreter the log_queries.py script: python log_queries.py