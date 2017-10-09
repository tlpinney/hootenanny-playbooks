Vagrant.configure('2') do |config|
  config.vm.define 'centos7', primary: true do |centos7|
    centos7.vm.box = 'hoot/centos7-minimal'
    centos7.vm.hostname = 'hoot-centos7'
    centos7.vm.synced_folder '.', '/vagrant', disabled: true
  end

  config.vm.define 'trusty' do |trusty|
    trusty.vm.box = 'hoot/trusty-minimal'
    trusty.vm.hostname = 'hoot-trusty'
    trusty.vm.synced_folder '.', '/vagrant', disabled: true
  end

  config.vm.provision :ansible do |ansible|
    ansible.playbook = 'hootenanny.yml'
  end

  config.vm.provider :aws do |aws|
    aws.instance_type = ENV.fetch('AWS_INSTANCE_TYPE', 'm3.xlarge')
    aws.block_device_mapping = [
      { 'DeviceName' => '/dev/sda1', 'Ebs.VolumeSize' => 40 }
    ]

    if ENV.key?('AWS_KEYPAIR_NAME')
      aws.keypair_name = ENV['AWS_KEYPAIR_NAME']
    end

    if ENV.key?('AWS_SECURITY_GROUP')
      aws.security_groups = ENV['AWS_SECURITY_GROUP']
    end

    aws.tags = {
      'Contact' => 'justin.bronn@digitalglobe.com',
      'Name'    => 'hootenanny-playbooks',
      'URL'     => 'https://github.com/jbronn/hootenanny-playbooks',
    }
  end
end
