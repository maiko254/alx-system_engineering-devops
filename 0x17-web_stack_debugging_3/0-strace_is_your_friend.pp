# Fixing file name in wordpress settings file causing 500 server error
exec {  'modify-file':
  command => 'sed -i s/"class-wp-locale.phpp"/"class-wp-locale.php"/ /var/www/html/wp-settings.php',
  path    => '/usr/bin:/bin'
}
