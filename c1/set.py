#!/usr/bin/env python
# -*-coding:utf-8-*-

# ���ϱ�ʾ�໥֮������ ��һ�����
# ���Ϸ�Ϊ���� ��ͨ���ϣ��ڳ�ʼ����֧�ֲ��������������������㣩 �� ���ɱ伯�ϣ���ʼ����Ͳ��ܸı䣩

sample1 = set('understand')					# ��string��ʼ��set
print sample1

myList = [ 4, 6, -1.1, 'English', 0, 'Python']
sample2 = set(myList)							# ��list��ʼ��set=��ͨ����
print sample2

sample3 = frozenset(myList)					# ��ʼ�� frozenset=���ɱ伯��
print sample3

myList = [ 4, 6, -1.1, 'English', 0, 'Python']
sample2 = set(myList)							# ��ʼ��set
sample3 = frozenset([ 6, 'English', 9])				# ��ʼ��frozenset

print 6 in sample2							# �жϰ�����ϵ
print sample2 >= sample3						# �ж��Ӽ���ϵ
print sample2 - sample3						# ������
print sample2 & sample3						# ������
sample3 |= sample2							# ���Զ�frozensetִ�� |= ���¸�ֵ
print sample3


sample2 = set([ 4, 6, -1.1, 'English', 0, 'Python'])		# ��ʼ��set

sample2.add('China')							# ����Ԫ��
print sample2

sample2.update('France')						# �����и���
print sample2

sample2.remove(-1.1)							# ɾ��Ԫ��
print sample2

sample3 = frozenset([ 6, 'English', 9])				# ��ʼ��frozenset

# sample3.add('China')							# ����frozenset�޷�����
