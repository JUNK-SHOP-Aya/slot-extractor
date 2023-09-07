'''
author:
date: 2023/09/06
description: 提取日期中月份（包含年份）
'''

from datetime import datetime
from typing import Dict
import re

from lac_utils import lac


def month_extract(text: str) -> Dict[str, int]:
    '''
    text: 包含日期的字符串
    return: { 'year': 2023, 'month': 9 }
    '''
    now = datetime.now()
    year, month = now.year, now.month
    lac_result = lac.run(text)
    for time_text, _ in (filter(lambda x: x[1] in ['TIME', 'm'], zip(lac_result[0], lac_result[1]))):
        _year, _month = y_parse(time_text, now.year), m_parse(time_text, now.month)
        if _year:
            year = _year
        if _month:
            month = _month
    return {
        'year': year,
        'month': month,
    }


y_keywords_0 = ['去年', '上一年', '上年']
y_keywords_1 = ['今年', '本年']
y_keywords_2 = re.compile(r'(?P<year>((19)?9[5-9]|(20)?[0-4][0-9]))年')


def y_parse(text: str, year: int) -> int:
    '''
    年份解析
    text: 包含日期的字符串
    year: 当前年份
    return: 2023
    '''
    # ['去年', '上一年', '上年']
    for y_keyword in y_keywords_0:
        if y_keyword in text:
            return year - 1
    # ['今年', '本年']
    for y_keyword in y_keywords_1:
        if y_keyword in text:
            return year
    # 23 年，2023 年
    match_result = y_keywords_2.search(text)
    if match_result:
        try:
            year = int(match_result.group('year'))
            if year < 50:
                return 2000 + year
            elif 50 < year < 100:
                return 1900 + year
            else:
                return year
        except ValueError:
            return None
    return None


m_keywords_0 = ['上月', '上个月', '上一个月']
m_keywords_1 = ['当月', '本月', '这个月', '这一个月']
m_keywords_2 = re.compile(r'(?P<month>(1[012]|0?[1-9]))月')
m_keywords_3 = {
    '一月': 1,
    '二月': 2,
    '三月': 3,
    '四月': 4,
    '五月': 5,
    '六月': 6,
    '七月': 7,
    '八月': 8,
    '九月': 9,
    '十月': 10,
    '十一月': 11,
    '十二月': 12,
}


def m_minus_1(month: int) -> int:
    '''
    众所周知 1 月的上个月是 12 月
    '''
    if month == 1:
        return 12
    return month - 1


def m_parse(text: str, month: int) -> int:
    '''
    月份解析
    text: 包含日期的字符串
    month: 当前月份
    return: 9
    '''
    # ['上月', '上个月', '上一个月']
    for m_keyword in m_keywords_0:
        if m_keyword in text:
            return m_minus_1(month)
    # ['当月', '本月', '这个月', '这一个月']
    for m_keyword in m_keywords_1:
        if m_keyword in text:
            return month
    # 9 月， 12 月
    match_result = m_keywords_2.search(text)
    if match_result:
        try:
            return int(match_result.group('month'))
        except ValueError:
            return None
    # 九月
    for k, v in m_keywords_3.items():
        if k in text:
            return v
    return None


if __name__ == '__main__':
    assert month_extract('上个月') == {
        'year': 2023,
        'month': 8,
    }
    assert month_extract('19年') == {
        'year': 2019,
        'month': 9,
    }
    assert month_extract('2023年') == {
        'year': 2023,
        'month': 9,
    }
    assert month_extract('这个月') == {
        'year': 2023,
        'month': 9,
    }
    assert month_extract('23年8月') == {
        'year': 2023,
        'month': 8,
    }
