# The basic syntax of python
## 1. Defined Function
**This is of the utmost importance**: you will be unable to run your program without any definition

### 1. A easy definition is like:
```python
   x = 1
   y = 3	# x , y are function name and '1','3' are value
```
### 2. You can assign multiple values at once:
```python
a , b , c = 1 , 2 , 3
```
### 3. You can assign value by using string:
```
name = 'LiHua'  	# '' or "" is indispensable
```
### 4. Generally, a function name can only store one value
```python
a = 1 , 2 , 'nihao' 
print(a)
	output: (1 , 2 , 'nihao')	#This is only one value
```
```python
a = 1
a = 2
print(a)
	output: 2		#The new value will overried the old value
```
### 5. Naming rules
- Only use number,alphabet and '_'
- Only take alphabet and '_' as opening
- Don't take builtins as opening
- Strictly distinguish between uppercase and lowercase letters
- You can use '_' separate the words
```python
student_name = 'Li Hua'
```
- **Upper camel case**: Each word must capitalize the first letter
```python
StudentName = 'LiHua'
```
- **Lower camel case**: The first letter of the first word is in lowercase
```python
studentName = 'LiHua'
```
- **The function is clear from the name**

## 2. Annotation
#### 1. '#'
```python
print('Hello World!')
# output a sentence: Hello World!
```
**Obviously, using'#'can only provide the annotation for one line**
#### 2. Three pairs of quotation marks——— ''' '''or""" """
```python
print('你好世界')
"""Output
a
chinese
sentence
:
你好世界
"""
```
** They can provide the annotation for more line**
## 3. print()
### 1. Introduction
- **This is a important command in many language**
```python
a = 1
b = 2
print(a)		output 1
print(b)		output 2
```
- ***"print()" can make founction visualized***
### 2. Basic format
```python
print(*value,sep='',end='\n')
```
#### 1. "*value" is what your function will output
- **It can be a effective function name**
```python
a = 1
print(a)		output 1  #'1' is the value of 'a'
print(b)		Error!	#'b' is ineffective
```
- **It can be a string enclosed in quotation marks**
```python
print('Hello World!')		output Hello World!
print("Hello World!")		output Hello World!
```
#### 2. "sep=''" means 'separator'
- **It is used to change the delimiter between the multiple output values**
```python
print('a','b','c',sep='-')		output a-b-c
```

- **The content in sep'' is a space symbol**
```python
print('a','b','c')				output a b c
print('a','b','c',sep='')		 output a b c
```
#### 3. "end=''" means 'ending'
- **It is used to change the delimiter at the end of the output values**
```python
print('a',end='!')			output a!
```
- **The content in end='' is '\n'**
### 3. If you want to output multiple lines of data####
- **Plase use there pairs of quotation marks**
```python
print('''Hello
World!''')
#output  Hello
#		World!
print("""你
好!""")
#output  你
#		好!
```
- **NOTICE : You can't use "sep''" in multi-line output**
