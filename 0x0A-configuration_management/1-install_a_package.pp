# Install pip
Package { 'python3-pip':
  ensure => 'installed'
}

# Install flask ver 2.1.0 from pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
