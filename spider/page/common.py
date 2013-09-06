import hashlib
import struct

def getTextContent(list):
    rstr = ''
    for item in list:
        rstr += item.strip()

    return rstr

def md5(input):
    md5sign = hashlib.md5()
    md5sign.update(input)
    str = md5sign.digest()
    data = struct.unpack("IIII", str)
    md5value = data[0] << 96 | data[1] << 64 | data[2] << 32 | data[3]
    return md5value


def encode_string_with_gbk(rstr):
    if rstr == None or len(rstr) <= 0:
        return ''

    try:
        return rstr.encode('gbk')
    except:
        return ''

class NewsItemInfo:
    def __init__(self, refer):
        self.id = ''
        self.url = ''
        self.title = ''
        self.tag = ''
        self.refer = refer
    

    def info_to_str(self):
        rstr = '%s\t%s\t%s\t%s\t%s' %(
                self.id,
                encode_string_with_gbk(self.url), 
                encode_string_with_gbk(self.title),
                encode_string_with_gbk(self.tag),
                encode_string_with_gbk(self.refer)
                )
        return rstr


