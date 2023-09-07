FROM paddlepaddle/paddle:2.5.1

COPY . .
RUN pip install -r requirements.txt

EXPOSE 13555

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:13555", "server:app"]
