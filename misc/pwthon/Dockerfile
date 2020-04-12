FROM ubuntu:18.04
MAINTAINER unknonwn
LABEL Description="pwthon" VERSION='1.0'

#installation
RUN apt upgrade
RUN apt update
RUN apt install -y socat 
RUN apt install -y python3

#user
RUN adduser --disabled-password --gecos '' pwn 
RUN chown -R root:pwn /home/pwn/
RUN chmod 750 /home/pwn

RUN touch /home/pwn/flag.txt

RUN export TERM=xterm

#Copying file
WORKDIR /home/pwn/
COPY server.py /home/pwn
COPY flag.txt /home/pwn

#Setting perm..
RUN chown root:pwn /home/pwn/flag.txt
RUN chmod +x /home/pwn/server.py
RUN chmod 440 /home/pwn/flag.txt

EXPOSE 5002

#Run the program with socat
CMD su pwn -c "socat TCP-LISTEN:5002,reuseaddr,fork EXEC:/home/pwn/server.py"

