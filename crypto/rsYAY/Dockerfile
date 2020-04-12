FROM ubuntu:18.04
Label Description = "chall" VERSION = '1.0'

RUN apt update && apt -y upgrade
RUN apt install -y python3 python3-pip socat
RUN pip3 install pycrypto

#user
RUN adduser --disabled-password --gecos '' crypto
RUN chown -R root:crypto /home/crypto/
RUN chmod 750 /home/crypto

RUN touch /home/crypto/flag.txt

RUN export TERM=xterm

WORKDIR /home/crypto/
COPY chall.py /home/crypto
COPY flag.py /home/crypto
COPY flag.txt /home/crypto

#Setting perm..
RUN chown root:crypto /home/crypto/flag.txt
RUN chmod +x /home/crypto/chall.py
RUN chmod 440 /home/crypto/flag.txt

EXPOSE 31337

CMD su crypto -c "socat TCP-LISTEN:31337,reuseaddr,fork EXEC:/home/crypto/chall.py"