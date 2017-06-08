### Entorno de desarrollo
Para el entorno de desarrollo se ha de instalar Serverless Framework con npm:
RUN curl --silent --location https://rpm.nodesource.com/setup_6.x | bash -  
RUN yum install -y gcc-c++ make  
RUN yum -y install nodejs  
RUN npm install serverless -g  

### Ambiente de ejecución
Para poder ejecutar las librerías de python hay que instalar la siguiente librería:  

yum install -y atlas-devel