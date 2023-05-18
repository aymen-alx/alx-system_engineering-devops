# Configure nginx limit and restart it

exec { 'replace_ulimit':
  command => "sed -i 's/^ULIMIT=\"-n 15\"$/ULIMIT=\"-n 4096\"/' /etc/default/nginx",
}

exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}
