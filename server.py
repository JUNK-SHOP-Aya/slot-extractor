'''
author:
date: 2023/09/06
description: Flask 服务主入口
'''

from flask import Flask, request, jsonify

import month_extractor

app = Flask(__name__)


@app.route('/month', methods=['POST'])
def extract_month():
    '''
    /month 接口
    '''
    text = request.json.get('text', '')
    result = month_extractor.month_extract(text)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
