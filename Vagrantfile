Vagrant.configure('2') do |config|
  config.vm.define 'centos7', primary: true do |centos7|
    centos7.vm.box = 'hoot/centos7-minimal'
  end

  config.vm.define 'trusty' do |trusty|
    trusty.vm.box = 'hoot/trusty-minimal'
  end

  config.vm.provision :ansible do |ansible|
    ansible.playbook = 'hootenanny.yml'
  end
end
