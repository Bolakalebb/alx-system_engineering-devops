# Using Puppet, install flask from pip3 

exec { 'flask':
  command => ./usr/bin/pip install flask',
}
