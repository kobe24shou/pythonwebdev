#!/usr/bin/env python
# -*-coding:utf-8-*-

tuple1 = ('you', 456, 'English', 9.34)				# ���� ��Բ���ű�ʾ����ͬԪ��֮���ö��Ÿ���
print tuple1[2]								# ��ȡԪ��
print tuple1[1:]								# ��ȡ��Ԫ��

# tuple1[2]='France'							#���󣡲����޸�Ԫ������
# Ԫ�� �Ĵ�С�����е�Ԫ���ڳ�ʼ�������޸ģ�Ԫ��ȿ��޸ĵ�list �����ٶȿ� 
# �����Ҫ����һ��ֵ�ǳ���ֵ������ΨһҪ���������ǲ��ϵĶ�ȡ --������Ԫ��ĳ���
tuple2 = (3, 'you and me')
tuple1 = tuple1 + tuple2						# ���Զ�Ԫ��������¸�ֵ

print tuple1
print len(tuple2)								# �ú���len()���Ԫ�鳤��
