FROM python:3.7-slim
RUN mkdir /app
COPY  requirement.txt ./app
WORKDIR /app
RUN pip3 install -r requirement.txt
RUN cd ..
RUN rm -r /app

#RUN python3 app.py