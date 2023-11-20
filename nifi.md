# This files tells you like how to do make the enviroment setup

1. Downloading the nifi files from its official website and make sure that it was in latest version

       https://nifi.apache.org/

2. Now, do extract the file from the zip folder
   
4. After extracting the file do make the shell file as executing with the command such as by going to the bin folder:-

            chmod +x bin/nifi.sh

5. This will do generate the username and password for our nifi account

          nifi.sh set-single-user-credentials <username> <password>

6. Now lets start ours nifi and the command for it is

       bin/nifi.sh start
       bin/nifi.sh status

7. Do login into the nifi with the created credentials

       https://localhost:8443/nifi/

8. See the results.md for the last steps
