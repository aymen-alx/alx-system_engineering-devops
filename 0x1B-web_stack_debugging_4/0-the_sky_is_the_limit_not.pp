# Configure nginx limit and restart it

$file_path = '/etc/default/nginx'
$replacement = 'ULIMIT="-n 4096"'

file { $file_path:
  ensure  => present,
  content => file($file_path).content.gsub(/ULIMIT='-n \d+'/, $replacement),
}

exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}
