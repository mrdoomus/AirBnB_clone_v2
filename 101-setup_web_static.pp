#Executes task #0 but in puppet mode ;)
exec { 'Update':
  path    => '/usr/bin',
  command => 'apt-get -y update',
}
exec { 'Get nginx':
  path    => '/usr/bin',
  command => 'apt-get -y install nginx',
}
exec { 'create data folder':
  path    => '/usr/bin',
  command => 'mkdir -p /data/',
}
exec { 'create web_static folder in data':
  path    => '/usr/bin',
  command => 'mkdir -p /data/web_static/',
}
exec { 'create releases folder in web_static':
  path    => '/usr/bin',
  command => 'mkdir -p /data/web_static/releases/',
}
exec { 'create shared folder in web_static':
  path    => '/usr/bin',
  command => 'mkdir -p /data/web_static/shared/',
}
exec { 'create test folder in releases':
  path    => '/usr/bin',
  command => 'mkdir -p /data/web_static/releases/test/',
}
exec { 'Writes "hope it works" in tests index.html':
  path    => '/usr/bin',
  command => 'echo "hope it works" > /data/web_static/releases/test/index.html',
}
exec { 'creates symbolic link between test and current':
  path    => '/usr/bin',
  command => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
}
exec { 'changes owner and group to data':
  path    => '/usr/bin',
  command => 'chown -R ubuntu:ubuntu /data/',
}
exec { 'adds alias to location':
  path    => '/usr/bin',
  command => 'sed -i "/listen 80 default_server;/a location /hbnb_static/ {\n\talias /data/web_static/current/;\n}"
  /etc/nginx/sites-available/default',
}
exec { 'restarts nginx service':
  path    => '/usr/bin',
  command => 'service nginx restart',
}
