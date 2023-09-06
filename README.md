# slot-extractor

基于 LAC 和正则表达式的槽位提取

## Host a server

### Dev

```bash
python server.py
```

### Product

```bash
gunicorn -w 4 -b 0.0.0.0:8000 server:app
```

## Client requests

### /month

```bash
curl -X POST -H "Content-Type: application/json" -d '{"text":"上个月"}' http://localhost:5000/month
```
