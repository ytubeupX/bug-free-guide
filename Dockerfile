FROM anasty17/mltb:latest

COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["bash", "start.sh"]
