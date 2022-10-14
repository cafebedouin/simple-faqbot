FROM python:3.7
WORKDIR /app
COPY ./ ./
RUN pip install --upgrade pip
RUN pip install discord python-dotenv
CMD python3 bot.py
