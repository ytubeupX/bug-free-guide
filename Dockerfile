FROM mirrorultroid6/mltbspark:heroku

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

COPY start.sh .

CMD ["bash", "start.sh"]
