# This manifest creates a file in /tmp with specific requirements
file { 'holberton':
  ensure  => 'present',
  path    => '/tmp/holberton',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
