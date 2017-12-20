# -*- coding: utf-8 -*-

from django.http import HttpResponse

# 数据库操作
from config.models import goods


def testdb(request):
  test1 = goods(id='1',name='3224',type='1232425')
  test1.save()
  return HttpResponse("<p>数据添加成功！</p>")