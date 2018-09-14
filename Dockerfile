FROM centos:7

COPY get-pip.py .
COPY hootenanny-docker.yml .
COPY roles . 

RUN python get-pip.py

RUN pip install ansible 

RUN ansible-playbook hootenanny-docker.yml

RUN yum install hootenanny-core -y

CMD /usr/bin/hoot


