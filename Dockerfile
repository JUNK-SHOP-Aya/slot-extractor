FROM paddlepaddle/paddle:2.5.1

WORKDIR /home/app
EXPOSE 13555

COPY . .
RUN pip install -r requirements.txt

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:13555", "server:app"]
