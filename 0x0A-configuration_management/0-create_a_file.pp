# creates a file school in tmp directory using puppet
File { 'school':
  path    => '/tmp/school',
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
