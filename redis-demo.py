__author__ = "Neil"
__time__ = "2017/12/26 15:24"

import redis

# ************
#redis第一种连接方法
#************
#
r = redis.Redis(host='127.0.0.1', port=6379)
# r.set('name', 'zhangsan')   #添加
# print (r.get('name'))   #获取


# ************
#redis第二种连接方法，利用连接池
#************

# import redis
# pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
# r = redis.Redis(connection_pool=pool)
# pipe = r.pipeline(transaction=True)
# r.set('name', 'zhangsan')
# r.set('name', 'lisi')
# pipe.execute()

# ************
#redis string操作
#************

# r.set('name', 'zhangsan',ex=5)
# '''参数：
#      set(name, value, ex=None, px=None, nx=False, xx=False)
#      ex，过期时间（秒）
#      px，过期时间（毫秒）
#      nx，如果设置为True，则只有name不存在时，当前set操作才执行,同setnx(name, value)
#      xx，如果设置为True，则只有name存在时，当前set操作才执行'''
# print(r.get('name'))
# #批量设置与获取
# r.mset(name1='zhangsan', name2='lisi')
# #或
# r.mset({"name1":'zhangsan', "name2":'lisi'})
# print(r.mget("name1","name2"))
# #或
# li=["name1","name2"]
# print(r.mget(li))
#得到一个列表


# ************
#redis hash操作(一个name对应一个字典)
#************
#name对应的hash中设置一个键值对（不存在，则创建，否则，修改）
#
# r.hset("dic_name","a1","aa")
# #print(r.hget("dic_name","a1"))
# #一次性设置获取多个键值对
# dic={"a1":"aa","b1":"bb"}
# r.hmset("dic_name",dic)
# print(r.hget("dic_name","a1"))
#
# #删除
# r.hdel("dic_name","a1")

# ************
#redis list操作(一个name对应一个列表)
#************

# r.lpush("list_name",2)
# r.lpush("list_name",3,4,5)#保存在列表中的顺序为5，4，3，2
# r.lset("list_name",0,"bbb")
#
# r.linsert("list_name","BEFORE","2","SS")#在列表内找到第一个元素2，在它前面插入SS
#
#
# '''参数：
#      name: redis的name
#      where: BEFORE（前）或AFTER（后）
#      refvalue: 列表内的值
#      value: 要插入的数据
# '''
#
# r.lrem("list_name","SS")
#
# ''' 参数：
#     name:  redis的name
#     value: 要删除的值
#     num:   num=0 删除列表中所有的指定值；
#            num=2 从前到后，删除2个；
#            num=-2 从后向前，删除2个'''
# print(r.lrange("list_name",0,-1))
# print(r.blpop("list_name"))#pop出来是一个元组，第二个才是所需要的