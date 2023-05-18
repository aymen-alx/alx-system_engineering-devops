# Configure nginx limit

exec { 'configure hard file':
  path    => '/bin',
  command => "sed -i 's/5/4096/' /etc/security/limits.conf"
}

exec { 'configure hard file':
  path    => '/bin',
  command => "sed -i 's/4/4096/' /etc/security/limits.conf"
}
