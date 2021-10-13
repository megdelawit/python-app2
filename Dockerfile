FROM python

COPY weather_code.py .

COPY requirements.txt .

RUN pip3 install -r requirements.txt