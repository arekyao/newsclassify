#! /usr/bin/env python

import os
import time
import sys
import exceptions
import string
#import urllib2
from goose import Goose
from goose.text import StopWordsChinese
from common import md5
from common import getTextContent
from common import encode_string_with_gbk


def get_page_content(url):
    g = Goose({'stopwords_class': StopWordsChinese})
    try:
        article = g.extract(url=url)
    except Exception, e :
        print e
        article = None

    return article



def main(argv=sys.argv):

    src_news_url_list = open(argv[1],"r")
    page_db_dir = 'db.page/'
    
    url_id_hash = []

    cmd = "ls "+ page_db_dir 
    already_url_list = os.popen(cmd).readlines()
    for i in already_url_list:
        i = i.strip()
        url_id_hash.append(i)
        # print "++"+i+"++" 
        
    #print url_id_hash

    while 1:
        ### index line
        line = src_news_url_list.readline()

        if not line:
            break

        if line == "" or line == "\r" or line == "\r\n":
            print "there is a blank line"
            continue

        

        line_arr = line.split('\t')

        page_id = line_arr[0]
        print "page_id:"+page_id+"++"
        if page_id in url_id_hash:
            print page_id + "already crawled"
            continue

        url = line_arr[1]
        page_content = get_page_content(url)
        page_file_name = page_db_dir + "" + page_id


        print page_content


        page_file = open(page_file_name, "w" )

        if page_content != None:
            page_file.write(encode_string_with_gbk(page_content.cleaned_text))

        page_file.close()


	



if __name__ == "__main__":
	sys.exit(main())




	
