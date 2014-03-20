import re
from pymongo import MongoClient
from parse import Parse

db = MongoClient().sohu

urls = db.url.find()
parse = Parse()

pattern = re.compile('http://.*tv.sohu.com/(us/)?\d{8}/n?\d.shtml')
for url in urls:

    parse.parse(url['url'])
    # print(url)

