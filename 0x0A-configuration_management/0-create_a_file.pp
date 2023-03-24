# creates a file school in tmp directory using puppet
file { 'school':
  path    => '/tmp/school',
  ensure  => 'present',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
