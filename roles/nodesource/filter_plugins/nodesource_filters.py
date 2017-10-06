class FilterModule(object):
    def filters(self):
        return {
            'nodesource_apt_repo': self.nodesource_apt_repo,
            'nodesource_yum_repo': self.nodesource_yum_repo,
        }

    def nodesource_version(self, nodejs_version):
        if nodejs_version.startswith('0'):
            return nodejs_version
        else:
            return '%s.x' % nodejs_version.split('.')[0]
    
    def nodesource_apt_repo(self, nodejs_version):
        return 'node_%s' % self.nodesource_version(nodejs_version) 

    def nodesource_yum_repo(self, nodejs_version):
        return 'pub_%s' % self.nodesource_version(nodejs_version)
