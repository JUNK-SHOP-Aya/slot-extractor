# slot-extractor

基于 LAC 和正则表达式的槽位提取

## Host a server

### Dev

```bash
python server.py
```

### Product

```bash
gunicorn -w 4 -b 0.0.0.0:13555 server:app
```

### Docker

build env image

```bash
docker build -t slot_extractor:{version} .
```

run server

```bash
docker run --name slot_extractor -p 13555:13555 slot_extractor:{version}
```

the workdir is `/home/app`

```bash
docker run \
    --name slot_extractor \
    -p 13555:13555 \
    -v {/path/to/project}:/home/app \
    slot_extractor:{version}
```

## Client requests

### /month

```bash
$ curl -X POST -H "Content-Type: application/json" -d '{"text":"上个月"}' http://localhost:13555/month
{"month":8,"year":2023}
```
