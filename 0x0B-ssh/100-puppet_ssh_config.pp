# using puppet to configure ssh to use the private key ~/.ssh/school and no password authentication
file { '/etc/ssh/ssh_config':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "Host *\n User ubuntu\n IdentityFile ~/.ssh/id_rsa_school\n PasswordAuthentication no\n",
}
