# Puppet manifest that installs and configures nginx to serve a custom header with the hostname
exec {  'apt-update':
  command => '/usr/bin/apt-get update',
  path    => ['/usr/bin', '/usr/sbin'],
}

package {  'nginx':
  ensure  => installed,
  require => Exec['apt-update']
}

file {  '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    location / {
        add_header X-Served-By $hostname;
        try_files $uri $uri/ =404;
    }
}
",
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
}
