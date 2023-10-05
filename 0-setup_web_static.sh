#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

if ! which nginx > /dev/null 2>&1; then
	sudo apt-get update
	sudo apt-get -y install nginx
fi

dir1="/data/"
dir2="/data/web_static/"
dir3="/data/web_static/releases"
dir4="/data/web_static/shared"
dir5="/data/web_static/releases/test/"
fake_html_file="/data/web_static/releases/test/index.html"
sn_dir="/data/web_static/current"

for dir in "$dir1" "$dir2" "$dir3" "$dir4" "$dir5"; do
    if [ ! -d "$dir" ];
    then
        sudo mkdir -p "$dir"
    fi
done

html_content=\
"<html>
    <head>
        <body>
            Holberton School
        </body>
    </head>
</html>"

if [ ! -f "$fake_html_file" ];
then
    echo "$html_content" | sudo tee "$fake_html_file"
fi

if [ ! -d "$sn_dir" ];
then
	sudo ln -s "$dir5" "$sn_dir"
fi

sudo chown -R ubuntu:ubuntu "$dir1"

server_config=\
"server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name _;
	add_header X-Served-By \$hostname;

        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }

        location /hbnb_static {
                alias /data/web_static/current/;
        }

	location / {
		try_files \$uri \$uri/ =404;
	}
	error_page 404 /404.html;
	location = /404.html {
		internal;
	}
}"

echo "$server_config" | sudo tee /etc/nginx/sites-available/default

sudo service nginx restart
