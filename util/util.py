# -*- coding: utf-8 -*-

from datetime import datetime, tzinfo, timedelta
import re

class TimeUtil():
    """工具类"""

    @staticmethod
    def t_strptime(t_str):
        format = format = '%a %b %d %H:%M:%S %Y'
        offset_str = re.search(r'\+\d{4}', t_str).group(0)
        r_t_str = re.sub(r'\+\d{4}', '', t_str)
        offset = int(offset_str[1:])
        naive_dt = datetime.strptime(r_t_str, format)

        if offset_str[0] == '-':
            offset = -offset

        return naive_dt.replace(tzinfo=FixedOffset(offset))
        # print t.strftime('%Y-%m-%d %H:%M:%S')
        

class FixedOffset(tzinfo):
    """Fixed offset in minutes east from UTC.
        Official expample https://docs.python.org/3/library/datetime.html"""

    def __init__(self, offset):
        self.__offset = timedelta(minutes=offset)

    def utcoffset(self, dt):
        return self.__offset

    def dst(self, dt):
        return timedelta(0)