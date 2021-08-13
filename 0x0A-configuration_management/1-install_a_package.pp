# This manifest installs puppet-lint on your terminal
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}
