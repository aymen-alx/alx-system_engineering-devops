# Task 2

exec { 'update':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
    ensure  => 'installed',
    require => Exec['update']
}


exec { 'custom':
    command  => 'sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
    service nginx restart',
    provider => shell,
}


service {'nginx':
    ensure  => running,
    require => Package['nginx']
}
