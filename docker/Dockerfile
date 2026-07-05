FROM python:3.8

RUN pip install \
    ansible==2.9.9 \
    netmiko==3.1.1 \
    ncclient==0.6.7 \
    paramiko==2.7.1 \
    jinja2==2.10.3 \
    markupsafe==1.1.1 \
    lxml \
    cryptography==2.8

WORKDIR /app

# copy requirements
COPY requirements.yml /app/requirements.yml

# install collections
RUN ansible-galaxy collection install -r /app/requirements.yml

CMD ["/bin/bash"]