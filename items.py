rssh_conf = [
    '# This is the default rssh config file',
    '',
    '# set the log facility.  "LOG_USER" and "user" are equivalent.',
    'logfacility = LOG_USER ',
    '',
    '# Leave these all commented out to make the default action for rssh to lock',
    '# users out completely...',
    '',
    'allowscp',
    'allowsftp',
    '#allowcvs',
    '#allowrdist',
    'allowrsync',
    '#allowsvnserve',
    '',
    '# set the default umask',
    'umask = 022',
    '',
    '# If you want to chroot users, use this to set the directory where the root of',
    '# the chroot jail will be located.',
    '#',
    '# if you DO NOT want to chroot users, LEAVE THIS COMMENTED OUT.',
    '# chrootpath = /usr/local/chroot',
    '',
    '# You can quote anywhere, but quotes not required unless the path contains a',
    '# space... as in this example.',
    '#chrootpath = "/usr/local/my chroot"',
    '',
    '#',
    '#accessbits:   Six binary digits, which indicate whether the user is allowed to use rsync, rdist, cvs, sftp, '
    'scp and svnserve, in that order.  One means the command is allowed, zero means it is not.',
    '#',
]

for username, user_attrs in sorted(node.metadata.get('users', {}).items()):
    if user_attrs.get('shell', None) == '/usr/bin/rssh':
        umask = user_attrs.get('rssh', {}).get('umask', '022')
        accessbits = user_attrs.get('rssh', {}).get('accessbits', '000000')  # disallow everything
        path = user_attrs.get('rssh', {}).get('path', '')
        rssh_conf += [f'user={username}:{umask}:{accessbits}:{path}']  # TODO: make this configurable

rssh_conf += node.metadata.get('rssh', {}).get('add_config', [])

files = {
    '/etc/rssh.conf': {
        'content': '\n'.join(rssh_conf) + '\n',
    }
}
