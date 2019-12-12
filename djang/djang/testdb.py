from django.http import HttpResponse
from myapp.models import Test
from books.models import Book,Publisher

#插入数据
def testdb(request):
    test1 = Test(name='geijia')
    test1.save()
    return HttpResponse('<p>数据添加成功</p>')

def bookDb(request):
    return
    p1 = Publisher(name='Apress', address='2855 Telegraph Avenue',city='Berkeley', state_province='CA', country='U.S.A.',website='http://www.apress.com/')
    p1.save()
    p2 = Publisher(name="O'Reilly", address='10 Fawcett St.',city = 'Cambridge', state_province = 'MA', country = 'U.S.A.',website = 'http://www.oreilly.com/')
    p2.save()
    return HttpResponse('<p>数据添加成功</p>')

#查询数据操作
def testdb2(request):
    response = ''
    response1 = ''
    list = Test.objects.all()
    response2 = Test.objects.filter(id=3)
    response3 = Test.objects.get(id=1)
    response4 = Test.objects.order_by('id')[0:2]
    for var in response2:
        response1 += var.name + "\n"
    response = response1
    return HttpResponse('<p> response2' + response + '</p>')

#修改数据库
def testdb3(request):
    test1 = Test.objects.get(id=3)
    test1.name = 'test'
    test1.save()
    Test.objects.filter(id=3).update(name='geijia')
    return HttpResponse('<p>数据修改成功1</p>')

#删除数据
def testdb4(request):
    test1 = Test.objects.get(id=3)
    test1.delete()
    return HttpResponse('<p>删除数据成功</p>')
