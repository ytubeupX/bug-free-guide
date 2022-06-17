FROM mirrorultroid6/mltbspark:heroku

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

ADD requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["bash", "start.sh"]
