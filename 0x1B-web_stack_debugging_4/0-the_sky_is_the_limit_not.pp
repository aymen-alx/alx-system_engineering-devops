# Configure nginx limit and restart it

exec { 'change from 15 to 4096':
  path    => '/bin',
  command => "sed -i 's/15/4096/' /etc/default/nginx"
} ->

exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
