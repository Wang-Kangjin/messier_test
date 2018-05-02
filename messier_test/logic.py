import os
import random
# 自定义函数
# 计算MD5
def getmd5of(str): 
	pass

# 播放图片
def displaypictureof(str):
	print(str)

# 数据定义
# 每道题的答案
# [0]第一题：姓名、生日、选项
# [1]第二题：入学年份、选项
# [2-6]第三到七题：选项
answers = [['noinput', 'noinput', 'B'], [2016, 'C'], 'A','A','A','A','A']
# 每道题的归类结果
# 第一题：0->根据MD5完全随机  1->输出喵星人结果
# 第二题：0->天狼星  1->牛郎星  2->织女星 3->南门二 4->需要重新随机
# 第三到七题：0->结果是冷色调图片  1->结果是暖色调图片
types = [0,0,0,0,0,0,0]

# 封面
print('你的星遇奇缘')

# 题目
os.system('pause')
print('问题一')
print('你的姓名和生日？')
print('''A输入
B我是喵星人，这些都是机密我也没办法┐（─__─）┌''')
option = input('输入选项')
answers[0][2] = option
if option == 'A':
	answers[0][0] = input('输入姓名')
	answers[0][1] = input('输入生日')
	name_md5 = getmd5of(answers[0][0])
	types[0] = 0
elif option == 'B':
	types[0] = 1

os.system('pause')
print('问题二')
print('你的入学年份？')
print('''A输入
B我是准萌新，提前来给北大献礼
C都是燕园有缘人，何必在意这些细节？''')
option = input('输入选项')
answers[1][1] = option
if option == 'A':
	answers[1][0] = int(input('入学年份'))
	if answers[1][0] == 2010:
		types[1] = 0
	elif answers[1][0] == 2002:
		types[1] = 1
	elif answers[1][0] == 1993:
		types[1] = 2
	elif answers[1][0] == 2014:
		types[1] = 3
elif option == 'B' or option == 'C':
	types[1] = 4

os.system('pause')
print('问题三')
displaypictureof('王靖翔 月')
print('当你看到这样的月亮挂在天上，你首先想到的是：')
print('''A广寒
B婵娟
C玉盘''')
option = input('输入选项')
answers[2] = option
if option == 'A':
	types[2] = 0
elif option == 'B' or option == 'C':
	types[2] = 1
	
os.system('pause')
print('问题四')
displaypictureof('冥王星')
print('还记得曾经刷了大家屏的冥王星吗？想起它，你的第一印象是：')
print('''A大大的爱心
B柯伊伯带
C冥界首领普鲁托''')
option = input('输入选项')
answers[3] = option
if option == 'A':
	types[3] = 1
elif option == 'B' or option == 'C':
	types[3] = 0
	
os.system('pause')
print('问题五')
displaypictureof('北京大学星')
print('这颗小行星名为“北京大学星”，看到它，你想到了：')
print('''A一组神秘的数字：7072，20
B厉害了我的大学
C未名湖''')
option = input('输入选项')
answers[4] = option
if option == 'A':
	types[4] = 0
elif option == 'B' or option == 'C':
	types[4] = 1
	
os.system('pause')
print('问题六')
displaypictureof('天狼星')
print('看到这颗星，你的感觉是：')
print('''A炽热而光明
B冰冷而遥远
C神秘而渺小''')
option = input('输入选项')
answers[5] = option
if option == 'A':
	types[5] = 1
elif option == 'B' or option == 'C':
	types[5] = 0
	
os.system('pause')
print('问题七')
displaypictureof('M51')
print('你觉得这个天体最像：')
print('''A可爱的伴侣
B恐怖的漩涡
C深情的双眸''')
option = input('输入选项')
answers[6] = option
if option == 'B':
	types[6] = 0
elif option == 'A' or option == 'C':
	types[6] = 1

# 输出测试
print(answers)
print(types)

# 决定结果
# 最终结果
# [0]整体分为0,1,2,3四类  0->喵星人  1->冷色调  2->暖色调  3->特定天体（第二题结果，如天狼星）
# [1]图片输出：      0->第0张图
# [2]第一句话输出：  0->第0句
# [3]第二句话输出：  0->第0句
# [4]第三句话输出：  0->第0句
result = [0,0,0,0,0]
# 选择根据哪道题的答案作为最终结果
if types[0] == 0:
	random.seed(name_md5)
else:
	random.seed()

while True:
	questionNum = random.randint(0,6)
	if questionNum == 0:
		if types[0] == 1:
			result = [0,0,0,0,0]
		elif types[0] == 0:
			result = [random.ranint(1,2), random.randint(0,19), random.randint(0,2), random.randint(0,2), random.randint(0,2)]
	elif questionNum == 1:
		if types[1] == 4:
			continue
		else:
			result = [3,types[1],0,0,0]
	elif 1 < questionNum and questionNum < 7:
		result = [types[questionNum] + 1, random.randint(0,19), random.randint(0,2), random.randint(0,2), random.randint(0,2)]
	break

print(result)