import orm
from model import User,Blog,Comment

def test():
	yield from orm.create_pool(user='root',password='123456',database='python_blog')

	u=User(name='YueFang',email='1208954839@qq.com',passwd='123456',image='about:blank')

	yield from u.save()

for x in test():
	pass