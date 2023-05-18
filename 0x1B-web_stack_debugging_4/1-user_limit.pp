# Configure nginx limit

exec { 'configure hard file':
  path    => '/bin',
  command => "sed -i '/holberton hard/s/5/30000/' /etc/security/limits.conf"
}

exec { 'configure hard file':
  path    => '/bin',
  command => "sed -i '/holberton soft/s/4/30000/' /etc/security/limits.conf"
}
