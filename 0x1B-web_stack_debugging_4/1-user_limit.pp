# Configure nginx limit

exec { 'configure hard file':
  command => "sed -i '/holberton hard/s/5/30000/' /etc/security/limits.conf",
  path    => '/bin'
}

exec { 'configure hard file':
  command => "sed -i '/holberton soft/s/4/30000/' /etc/security/limits.conf",
  path    => '/bin'
}
