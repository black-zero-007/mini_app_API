# Author:JZW
import redis
conn = redis.Redis(host='192.168.40.10',port=6379,password='jzw15840665319')
conn.set('foo','Bar')
result = conn.get('foo')
print(result)