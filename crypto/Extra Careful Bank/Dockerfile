FROM ubuntu:18.04
MAINTAINER unknonwn
LABEL Description="Extra Careful Bank" VERSION='1.0'

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
COPY Extra_Careful_Bank.py /home/crypto
COPY flag.txt /home/crypto

#Setting perm..
RUN chown root:crypto /home/crypto/flag.txt
RUN chmod +x /home/crypto/Extra_Careful_Bank.py
RUN chmod 440 /home/crypto/flag.txt

EXPOSE 7331

#Run the program with socat
CMD su crypto -c "socat TCP-LISTEN:7331,reuseaddr,fork EXEC:/home/crypto/Extra_Careful_Bank.py"
