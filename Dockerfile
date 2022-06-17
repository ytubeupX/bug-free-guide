FROM anasty17/mltb:heroku

COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["bash", "start.sh"]
