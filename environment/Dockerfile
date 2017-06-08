FROM amazonlinux
RUN curl --silent --location https://rpm.nodesource.com/setup_6.x | bash -
RUN yum install -y gcc-c++ make
RUN yum -y install nodejs
RUN yum -y install vim
RUN npm install serverless -g
WORKDIR /home/