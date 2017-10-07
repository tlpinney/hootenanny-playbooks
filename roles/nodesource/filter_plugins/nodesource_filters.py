class FilterModule(object):
    def filters(self):
        return {
            'nodesource_apt_repo': self.nodesource_apt_repo,
            'nodesource_yum_repo': self.nodesource_yum_repo,
        }

    def nodesource_version(self, nodejs_version):
        major, minor = nodejs_version.split('.')[:2]
        if nodejs_version.startswith('0'):
            return '.'.join([major, minor])
        else:
            return '%s.x' % major
    
    def nodesource_apt_repo(self, nodejs_version):
        return 'node_%s' % self.nodesource_version(nodejs_version) 

    def nodesource_yum_repo(self, nodejs_version):
        return 'pub_%s' % self.nodesource_version(nodejs_version)
