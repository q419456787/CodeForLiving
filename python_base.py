#python for 基础
names = ['Michael', 'Bob', 'Tracy']
for name in names:
	print(name)
	
#python list 基础  

list=[1,2,3]

print('list 数组倒数第一个是%d'%list[-1])
#在末尾加入4
list.append(4)
print('list 数组倒数第一个是%d'%list[-1])

list.insert(len(list),5);
print('list 数组倒数第一个是%d'%list[-1])
list.insert(0,0);
#超出list长度就在末尾加上
list.insert(len(list)+11,5);


for item in list:
	print(item)
print('list pop一个元素元素')
# list 弹出删除最后一个元素
list.pop()
for item in list:
	print(item)
	
#list里面的元素的数据类型也可以不同，比如：
multiList=['python','java', ['asp','php'], 'scheme']

NullL = []
print('一个空的数组',len(NullL))

# Hashtable  dictionary字典 键	
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

#判断某个键名是否在 dictionary字典 里面  这个会返回true
if('test' in d):
	print('the key named test is exited')
else:
	print('the key name test is not in dic')

#若没有该键可以设定一个返回值	
print(d.get('Thomas',-9999))

#dictionary字典 删除键 也是通过pop
d.pop('Bob')



# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
s = set([1, 2, 3])
#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(4)
s.add(4)
# 还是一样的
#通过remove(key)方法可以删除元素：
s.remove(4)
 
 # !!!!!set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
 # 以上传入的是一个 list  数组[1,2,3]
 #交集
intersection=s1&s2
 # 并集
UnionAssemble=s1|s2
  
 
 
 
 
# str是不变对象，而list是可变对象。
array = ['c', 'b', 'a']
array.sort()
for item in array:
	print(item)
	
#dictionary字典 d的键必须是不可变对象, 所以一般以string类型来作为,但是tuple也是不可变对象	
tuple=(1, 2, 3);	

#tuple 这个是不变的数组
d[tuple]='Test'
print(d[tuple])


#调用函数
#Built-in Functions  很多内置函数 查看 https://docs.python.org/3/library/functions.html
print('调试all 方法对一个 array')
print(all(array));
print('调试abs 方法对一个 -9999')
print(all(array));
#输出4 的二进制数 string
print(bin(4))

# max 输出最大的

#数据类型转换#
print(int('123'))
#取整
print(int(12.34))

# float('12.34')

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
abb=abs
print('abb=abs--使abs等于abb这个函数')
print(abb(-123))

#使用内置函数hex 返回 string
print(hex(255))  
print(hex(266))





#定义个一个空函数 pass 其实先让程序跑起来
def nondo():
	pass

#isinstance 用来判断x 是否某个类型int float
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
		
# my_abs('A') 这里会抛出操作数的异常

#返回多个值
#看看import 在这里还是没问题的
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
	
#原来返回值是一个tuple！ 按位置赋予对应的值
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

#函数的注意的细节
# 函数执行完毕也没有return语句时，自动return None。
# 函数可以同时返回多个值，但其实就是一个tuple。

def quadratic(a, b, c):
	if not isinstance(a,(int, float)):
		raise TypeError('bad operand type')
	if (b*b-4*a*c)>0:
		x1=	(-b+math.sqrt(b*b-4*a*c))/2*a
		x2=	(-b-math.sqrt(b*b-4*a*c))/2*a
		return x1,x2
	else:
		return 0

print(quadratic(2,-8,3))

#函数的默认参数跟C#基本一样  默认参数放最后, 两个默认参数需要传最后一个的时候，可以使用命名实参来确定是传递个哪个默认参数

# 为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。
# 此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象

##### 特殊参数 #####
#1.可变参数 参数个数是可以变得，不然 只能封装成list 或者tuple的形式传递过去 [1,2,3,4]  然而其实 多个参数传递过去会组装成tuple的形式的
def calc(*numbers):
	sum=0
	for item in numbers:
		sum=sum+item*item
	return sum

print(calc(1,2,3,4,5))

#问题来了，假如我已经有一个list 或者tuple 然后想调用上面的函数，但是可变参数，
#所以可以 *list来解决
list=[1,2,3]
print(calc(*list))

#2.关键字参数 允许你传入0个或任意个含 参数名 的参数 key-values的形式 这些关键字参数内部自动组装成一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('MR.CHEN',20,CITY='SHENZHEN',STREET='HUAQIAOXINCUN')
#也可以先组装出一个dict然后传递过去
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('MR.CHEN',20,**extra)


#3.命名关键字参数  这里就限定死是用 city为键 job 键的 用*隔开
def person1(name, age, *, city, job):
	 print(name, age, city, job)
def person2(name, age, *,city, job='Test'):
    print(name, age, city, job)
	
person2('Jack', 24, city='Engineer')
	
	




