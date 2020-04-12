FROM ubuntu:18.04
MAINTAINER unknonwn
LABEL Description="AESy" VERSION='1.0'

#installation
RUN apt upgrade
RUN apt update
RUN apt install -y socat
RUN apt install -y python
RUN apt install -y python-pip
RUN python -m pip install pycrypto

#user
RUN adduser --disabled-password --gecos '' crypto
RUN chown -R root:crypto /home/crypto/
RUN chmod 750 /home/crypto

RUN touch /home/crypto/flag.txt

RUN export TERM=xterm

#Copying file
WORKDIR /home/crypto/
COPY AESy.py /home/crypto
COPY flag.txt /home/crypto

#Setting perm..
RUN chown root:crypto /home/crypto/flag.txt
RUN chmod +x /home/crypto/AESy.py
RUN chmod 440 /home/crypto/flag.txt

EXPOSE 1337

#Run the program with socat
CMD su crypto -c "socat TCP-LISTEN:1337,reuseaddr,fork EXEC:/home/crypto/AESy.py"
