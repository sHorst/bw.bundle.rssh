rush_conf = [
    '# Sample configuration file for rush, patterned on Debian habits,',
    '# and developed by the Debian package maintainer.',
    '#',
    '# Lines beginning with # and empty lines are ignored.',
    '# See `info rush\' for a detailed description.',
    '#',
    '# $Rev: 61 $',
    '#',
    '# Set verbosity level.',
    'debug 1',
    '',
    '#',
    '# Default settings',
    '#',
    '',
    'rule default',
    '  acct on',
    '  limits t10r20',
    '  umask 002',
    '  env - USER LOGNAME HOME PATH',
    '  fall-through',
    '',
    '',
    '# Sftp-server requests: chroot to the virtual server, change to the user\'s',
    '#                       home directory, set umask to 002 and execute only',
    '#                       /usr/lib/sftp-server.',
    '#',
    '# Setting for a chroot directory created using \'debootstrap\'.',
    '#',
    '# Remark: The location \'/usr/lib/\' is inherited.',
    'rule sftp-rush',
    '  command ^.*/sftp-server',
    '  uid >= 1000',
    '  set[0] /usr/lib/sftp-server',
    '  umask 002',
    # TODO: make chroot here
    '  chdir ~',

    '',
    '# Rsync server version, will be used by bw to check if restic',
    'rule rsync-version',
    ' command ^rsync --server --version',
    ' uid >= 1000',
    ' set[0] /usr/bin/rsync',
    '',
    '# Rsync service: chroot to the virtual server, move to home directory,',
    '#                and check paths, not to backtrack.',
    'rule rsync-home',
    ' command ^rsync --server',
    ' uid >= 1000',
    ' set[0] /usr/bin/rsync',
    ' match[$] ^([^/].*|~/.*)',
    ' match[$] ! \.\.',
    ' transform[$] s,^~/,./,',
    ' umask 002',
    ' chdir ~',

]

# for username, user_attrs in sorted(node.metadata.get('users', {}).items()):
#     if user_attrs.get('shell', None) == '/usr/bin/rssh':
#         umask = user_attrs.get('rssh', {}).get('umask', '022')
#         accessbits = user_attrs.get('rssh', {}).get('accessbits', '000000')  # disallow everything
#         path = user_attrs.get('rssh', {}).get('path', '')
#         rush_conf += [f'user={username}:{umask}:{accessbits}:{path}']  # TODO: make this configurable

rush_conf += node.metadata.get('rssh', {}).get('add_config', [])

files = {
    '/etc/rush.rc': {
        'content': '\n'.join(rush_conf) + '\n',
    }
}
