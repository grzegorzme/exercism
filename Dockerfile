FROM python:3.5-slim

ADD ./exercism_cli /exercism_cli

WORKDIR /exercism_cli

RUN apt-get update \
 && apt-get upgrade -y

RUN . /exercism_cli/vars.env && export $(cut -d= -f1 vars.env) \
 && apt-get install git -y \
 && git config --global user.email "$GIT_EMAIL" \
 && git config --global user.name "$GIT_NAME" \
 && tar -xzvf exercism-linux-64bit.tgz \
 && mkdir ~/bin \
 && mv exercism ~/bin/ \
 && export PATH=$HOME/bin:$PATH \
 && echo "export PATH=$HOME/bin:$PATH" >> ~/.bashrc \
 && exercism configure --key=$EXERCISM_KEY --dir=/code/exercism \
 && pip install -r requirements.txt
