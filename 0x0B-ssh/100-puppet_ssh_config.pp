# Setup client configuration for use with private key

file { 'file exists':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
}

file_line { 'use private key':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'disable password':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}
