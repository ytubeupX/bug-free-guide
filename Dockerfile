FROM mirrorultroid6/mltbspark:heroku

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

ADD requirements.txt .
ADD start.sh .
ADD update.py .
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["bash", "start.sh"]
