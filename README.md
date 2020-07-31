### Project Setup 

##### To Launch the project use run.sh, Run this script from linux shell :

$ ./run.sh

###### Make sure file run.sh file have execute permissions.

$ ls -ltr run.sh 

###### Ir -rwx is not in the first 4 places run below command to update access.

$ chmod u+x run.sh

###### Application will run on localhost:8000 by default

##### Run nginx server

$ sudo apt-get install nginx

$ sudo unlink /etc/nginx/sites-enabled/default

$ cd /etc/nginx/sites-available

$ sudo nano reverse-proxy.conf

##### copy below in the file and save 

    server {
        listen 80;
        listen [::]:80;

        access_log /var/log/nginx/reverse-access.log;
        error_log /var/log/nginx/reverse-error.log;

        location / {
                    proxy_pass http://127.0.0.1:8000;
        }
    }

$ sudo ln -s /etc/nginx/sites-available/reverse-proxy.conf /etc/nginx/sites-enabled/reverse-proxy.conf

##### Test server 

$ sudo nginx -t

##### Start/Restart/Stop commands 

$ sudo service nginx start
$ sudo service nginx stop
$ sudo service nginx restart

##### Once server is up hit localhost and site should be available