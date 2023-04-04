# Task 2

exec { 'apt update':
        command => '/usr/bin/apt-get update',
}

exec { 'command':
  command  => 'apt-get -y install nginx;
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  service nginx restart',
  provider => shell,
  require => Exec['apt update']
}
