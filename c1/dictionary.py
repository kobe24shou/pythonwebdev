#!/usr/bin/env python
# -*-coding:utf-8-*-

# �ֵ� ����һ����ֵ �洢�⣬�е���ӳ��� ������һ��key ���������ֵ�����������ü� ��Ӧ��ֵ
dict1 = {'Language': 'English', 'Title': 'Python book', 'Pages': 450}
print dict1['Title']									# ��ȡԪ��

dict1['Date'] = '2002-10-30'							# ֱ��ͨ���±������ֵ�����
print dict1

dict1['Language'] = 'Chinese'						# ֱ��ͨ���±�����ֵ�����
print dict1

dict2 = {'Language': 'English', 'Language':'Chinese'}
print dict2

dict1 = {'Language': 'English', 'Title': 'Python book', 'Pages': 450}
print dict1.get('Title', 'Todo')					# ��ȡԪ��
print dict1.get('Author', 'Anonymous')			# ��ȡ�����ڵļ�
print dict1.pop('Language')							# pop
print dict1										# ���pop����ֵ�����

dict2={'Author':'David', 'Price':32.00, 'Pages':409 }
dict1.update(dict2)								# �ϲ��ֵ�
print dict1
print dict1.values()								# ��ȡֵ�б�

