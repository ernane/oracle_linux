# HOW TO BUILD THIS IMAGE
# -----------------------
#
# Run:
#      $ docker build -t oracle_python:3.6 .

FROM oraclelinux:7-slim

ARG release=19
ARG update=3

ADD requirements.txt /tmp/

RUN  yum -y install oracle-release-el7 oracle-epel-release-el7 python36 \
     && yum-config-manager --enable ol7_oracle_instantclient \ 
     && yum -y install oracle-instantclient${release}.${update}-basiclite \
     && pip3 install -r /tmp/requirements.txt \
     && rm -rf /var/cache/yum

CMD ["/bin/bash"]
