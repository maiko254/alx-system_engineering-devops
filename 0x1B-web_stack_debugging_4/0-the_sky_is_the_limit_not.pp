# increasing the maximum number of files that can be opened by nginx process
exec { 'update_ulimit':
  command => "sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/g' /etc/default/nginx",
  path    => ['/bin', '/usr/bin'],
  onlyif  => "grep -q 'ULIMIT=\"-n 15\"' /etc/default/nginx",
}

# Restart nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => Exec['update_ulimit'],
}
