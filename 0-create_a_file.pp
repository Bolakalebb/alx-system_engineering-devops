# manifest to create file in tmp directory
file { '/tmp/schoo':
  ensure  => file,
  path    => '/tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'ww-data',
  content => 'I love Puppet',
}
