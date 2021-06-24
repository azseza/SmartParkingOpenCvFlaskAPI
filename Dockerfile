FROM python:3.8.2
WORKDIR /code
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 3070
CMD [ "python", "app.py" ]