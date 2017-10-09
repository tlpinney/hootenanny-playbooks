class FilterModule(object):
    def filters(self):
        return {
            'pg_dotless_version': self.pg_dotless_version,
            'pg_short_version': self.pg_short_version,
        }

    def pg_major_minor(self, version):
        return version.split('.')[:2]

    def pg_dotless_version(self, version):
        return ''.join(self.pg_major_minor(version))

    def pg_short_version(self, version):
        return '.'.join(self.pg_major_minor(version))
