# Kills a process named killmenow
exec {  'pkill -f killmenow':
  path   => '/usr/bin:/bin'
  onlyif => 'pgrep -f killmenow'
}
