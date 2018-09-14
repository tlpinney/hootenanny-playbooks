FROM centos:7

COPY get-pip.py .
COPY hootenanny-docker.yml .
COPY roles . 

RUN python get-pip.py

RUN pip install ansible 

RUN ansible-playbook hootenanny-docker.yml

RUN yum install hootenanny-core -y

# Debugging tools 
RUN yum install lsof tmux -y

#CMD /usr/bin/hoot

RUN yum install hootenanny-services-ui -y 

ENTRYPOINT ["/usr/libexec/tomcat8/server", "start"]


