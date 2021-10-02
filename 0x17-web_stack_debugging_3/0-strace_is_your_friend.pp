# Fix Apache 500 error

exec { 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php':
  path => '/usr/bin:/usr/sbin:/bin',
}
