#!/usr/bin/env python
# -*-coding:utf-8-*-

# list �б���������[] ��ʾ����ͬԪ��֮���Զ��Ÿ���
# list �Ĵ�С������ ��Ԫ�� �ڳ�ʼ������Ա��ٴ��޸� ������list ��Ԫ�� ��Ҫ����
# ��� ������һ��ֵ��������֮�� ��Ҫ���϶�������� ɾ �� ��Ȳ�������Ӧ��ʹ��list

myList = ['you', 456, 'English', 9.34]				# ����

print myList[2]								# ��ȡԪ��
print myList[1:]								# ��ȡ���б�

myList[2] = 'France'							# �����޸�����
print myList
print len(myList)								# �ú���len()����б���

numList = [2, 8, 16, 1, -6, 52, -1]					# ����
print sorted(myList)							# ����
print myList								# sorted��myList�������ı�
print sum(numList)							# ���


numList = [2, 8, 16, 8, -6, 52, -1]					#����
print numList.count(8)							# count ����������б��г��ֵĴ���
numList.insert(1, 9)							# ��λ��1����Ԫ��9
print numList
