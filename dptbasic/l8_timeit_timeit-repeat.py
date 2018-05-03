#!/usr/bin/python3
# coding: utf-8

##################################################################
## timeit模块_为Python中的小块代码进行计时
'''
timeit模块定义了三个使用函数和一个公共类

timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000)
创建一个Timer实例，参数分别是stmt（需要测量的语句或函数），setup（初始化代码或构建环境的导入语句），timer（计时函数），number（每一次测量中语句被执行的次数）
注：由于timeit()正在执行语句，语句中如果存在返回值的话会阻止timeit()返回执行时间。timeit()会取代原语句中的返回值。

timeit.repeat(stmt='pass', setup='pass', timer=<default timer>, repeat=3, number=1000000)
创建一个Timer实例，参数分别是stmt（需要测量的语句或函数），setup（初始化代码或构建环境的导入语句），timer（计时函数），repeat（重复测量的次数），number（每一次测量中语句被执行的次数）

timeit.default_timer()
默认的计时器，一般是time.perf_counter()，time.perf_counter()方法能够在任一平台提供最高精度的计时器（它也只是记录了自然时间，记录自然时间会被很多其他因素影响，例如计算机的负载）

class timeit.Timer(stmt='pass', setup='pass', timer=<timer function>)

计算小段代码执行速度的类，构造函数需要的参数有stmt，setup，timer。前两个参数的默认值都是'pass'，timer参数是平台相关的；前两个参数都可以包含多个语句，多个语句间使用分号（;）或新行隔开。

第一次测试语句的时间，可以使用timeit()方法；repeat()方法相当于持续多次调用timeit()方法并将结果返回为一个列表。

stmt和setup参数也可以是可供调用但没有参数的对象，这将会在一个计时函数中嵌套调用它们，然后被timeit()所执行。注意，由于额外的调用，计时开销会相对略多。
'''

## timer_timer()
# 命令行
python -m timeit '"-".join(str(n) for n in range(100))'
>> 10000 loops, best of 3: 40.3 usec per loop
# 交互解释器
import timeit
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
# 脚本程序
def test():
	L = []
	for i in range(100):
		L.append(i)
def best_find():
    pass
if __name__ == '__main__':
	import timeit
	print timeit.timeit("test()", setup="from __main__ import test"))
    print timeit.timeit("best_find(string, text)", "from __main__ import best_find; string='lookforme'; text='look'")

## timeit_repeat
# repeat函数，指定整个试验的重复次数，返回一个包含了每次试验的执行时间的列表。
timeit.repeat('"-".join(str(n) for n in range(100))',repeat=3, number=10000)
>> [0.21938705444335938, 0.21767210960388184, 0.21688294410705566]
