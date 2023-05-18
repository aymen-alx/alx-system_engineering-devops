# Configure nginx limit

exec { 'hard':
  command => "sed -i '/holberton hard/s/5/30000/' /etc/security/limits.conf",
  path    => '/bin'
}

exec { 'soft':
  command => "sed -i '/holberton soft/s/4/30000/' /etc/security/limits.conf",
  path    => '/bin'
}
