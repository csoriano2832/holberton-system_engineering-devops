# This manifest creates a file in /tmp with specific requirements
file { 'holberton':
  path    => '/tmp/holberton',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  ensure  => 'present',
  content => 'I love Puppet',
}
