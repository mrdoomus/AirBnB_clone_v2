#Executes task #0 but in puppet mode ;)
exec { 'Update':
  command  => 'apt-get -y update',
  provider => shell,
}
exec { 'Get nginx':
  command  => 'apt-get -y install nginx',
  provider => shell,
}
exec { 'create data folder':
  command  => 'mkdir -p /data/',
  provider => shell,
}
exec { 'create web_static folder in data':
  command  => 'mkdir -p /data/web_static/',
  provider => shell,
}
exec { 'create releases folder in web_static':
  command  => 'mkdir -p /data/web_static/releases/',
  provider => shell,
}
exec { 'create shared folder in web_static':
  command  => 'mkdir -p /data/web_static/shared/',
  provider => shell,
}
exec { 'create test folder in releases':
  command  => 'mkdir -p /data/web_static/releases/test/',
  provider => shell,
}
exec { 'Writes "hope it works" in tests index.html':
  command  => 'echo "hope it works" > /data/web_static/releases/test/index.html',
  provider => shell,
}
exec { 'creates symbolic link between test and current':
  command  => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
  provider => shell,
}
exec { 'changes owner and group to data':
  command  => 'chown -R ubuntu:ubuntu /data/',
  provider => shell,
}
exec { 'adds alias to location':
  command  => 'sed -i "/listen 80 default_server;/a location /hbnb_static/ {\n\talias /data/web_static/current/;\n}"
  /etc/nginx/sites-available/default',
  provider => shell,
}
exec { 'restarts nginx service':
  command  => 'service nginx restart',
  provider => shell,
}
