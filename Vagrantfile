Vagrant.configure('2') do |config|
  config.vm.define 'centos7', primary: true do |centos7|
    centos7.vm.box = 'hoot/centos7-minimal'
    centos7.vm.hostname = 'hoot-centos7'
    centos7.vm.synced_folder '.', '/vagrant', disabled: true
  end

  config.vm.provision :ansible do |ansible|
    ansible.playbook = 'hootenanny.yml'
  end
end
