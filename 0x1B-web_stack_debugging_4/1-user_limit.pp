# Configure nginx limit

exec { 'configure hard file':
  path    => '/bin',
  command => "sed -i '/holberton hard/s/5/4096/' /etc/security/limits.conf"
}

exec { 'configure hard file':
  path    => '/bin',
  command => "sed -i '/holberton soft/s/4/4096/' /etc/security/limits.conf"
}
