#!/usr/bin/python 
# -*- coding: utf-8 -*-
from sys import exit


#终值计算器
def finalassets():
	print("信息输入样式举例")
	print("""
		请输入本金<元>：10000
		请输入年化收益率<如5%>：5%
		请输入每月追加投入金额<元>：1000
		请输入投资年限：30
		""")

	A=int(input("请输入本金<元>："))
	r=input("请输入年化收益率<如5%>：")
	m=int(input("请输入每月追加投入金额<元>："))
	n=int(input("请输入投资年限："))

	for i in range(1,12*n+1):
		A=int((A+m)*(1+float(r.strip('%'))/100/12))
		if i%12==0:
			print(f"第{int(i/12)}年总资产:{A}")


#达到目标的最低年化收益率
def yield_rate():
	print("年化收益率以0.05%递增")
	print("信息输入样式举例")
	print("""
		请输入理财目标<万元>：100
		请输入本金<元>：10000
		请输入每月追加投入金额<元>：1000
		请输入投资年限：30
	""")

	g=int(input("请输入理财目标<万元>："))
	AA=int(input("请输入本金<元>："))
	m=int(input("请输入每月追加投入金额<元>："))
	n=int(input("请输入投资年限："))

	r=0.005
	A=AA

	while A<g*10000:
		A=AA
		for i in range(1,12*n+1):
			A=int((A+m)*(1+r/12))
		r=r+0.005

	print(f"最终总资产：{A}")
	print(f"最低年化收益率：{round((r-0.005)*100,1)}%")


#达到目标的最低月投入金额
def monthly_invest():
	print("月投入金额以100元递增")
	print("信息输入样式举例")
	print("""
		请输入理财目标<万元>：100
		请输入本金<元>：10000
		请输入年化收益率<如5%>：5%
		请输入投资年限：30
		""")

	g=int(input("请输入理财目标<万元>："))
	AA=int(input("请输入本金<元>："))
	r=input("请输入年化收益率<如5%>：")
	n=int(input("请输入投资年限："))

	m=100
	A=AA

	while A<g*10000:
		A=AA
		for i in range(1,12*n+1):
			A=int((A+m)*(1+float(r.strip('%'))/100/12))
		m=m+100

	print(f"最终总资产：{A}")
	print(f"最低月投入金额：{m-100}")


def expenditure():
	income=int(input("请输入您的月可支配收入: "))

	exp={}
	n=int(input("请输入支出项目数量: "))

	print("\n请逐个输入项目及权重(权重之和如超过1,将按占比重新分配)")
	print("""
		举例：
		项目1：投资
		权重1：0.4
		""")


	for i in range(1,n+1):
		item=input(f"项目{i}: ")
		weight=float(input(f"权重{i}: "))
		exp[item]=weight

	print("\n以下为您各项支出及权重")    
	print(exp)    

	sum=0
	for value in exp.values():
		sum=sum+value

	print("\n以下为您各项支出的分配金额：")
	for key in exp:
		print(f"{key}:{int(exp[key]/sum*income)}")

	print("\n")


def start():
	print("欢迎使用理财小助手！")
	print("希望能够帮助您达成理财目标，优化支出结构，实现财务自由！")
	print("""
		理财小助手能够帮助您：
		1. 计算固定投资下，最终获得的总资产
		2. 计算达成既定理财目标，每月需要的最低投入的金额
		3. 计算达成既定理财目标，需要的最低年化收益率
		4. 按既定权重，分配月可支配收入
		"""
		)


	while True:
		print("请输入您想咨询的问题编号，输入其他任意内容退出")
		q=input("> ")
		if q=='1':
			finalassets()
		elif q=='2':
			monthly_invest()
		elif q=='3':
			yield_rate()
		elif q=='4':
			expenditure()
		else:
			exit(0)

start()