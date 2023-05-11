# puppet code to correct a line in a file on a server

$file_to_edit = '/var/www/html/wp-settings.php'

# change the line containing "phpp" with "php"

exec { 'change_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin']
}
