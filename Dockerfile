FROM python:3.7
WORKDIR /app
COPY ./ ./
RUN apt install python3 python3-pip -y
RUN pip install discord python-dotenv
CMD python3 bot.py
