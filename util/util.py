# -*- coding: utf-8 -*-

from datetime import datetime

def Util():
    """工具类"""
    
    def d_strptime(self, t_str):
        format = format = '%a %b %d %H:%M:%S %Y'
        offset_str = re.search(r'\+\d{4}', t_str).group(0)
        r_t_str = t_str.sub(r'\+\d{4}', '', t_str)
        offset = int(offset_str[1:])
        naive_dt = datetime.strptime(r_t_str, format)
        
        if offset_str[0] == '-':
            offset = -offset
            
        naive_dt.replace(t)