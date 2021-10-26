# Exercise 01: 基本操作：數值

'''
1-1 數值之比較：
(1) Input : 使用者自由輸入兩個數字
    Output: 顯示數字一大、小或等於數字二
'''

# input 預設為字串，需轉為 int 型態
# 使用者可能輸入小數：float 搭配 %s 輸出
number1=float(input("請輸入數字一:"))
number2=float(input("請輸入數字二:"))

if number1>number2:
    # 格式化輸出，等同 number1, ">", number2
    print("%s>%s"%(number1, number2))
elif number1==number2:
    print("%s=%s"%(number1, number2))
else:
    print("%s<%s"%(number1, number2))

'''
(2) Input : 使用者自由輸入學期成績
    Output: 顯示成績之轉換等第 (90 分以上 A、80 分以上 B、70 分以上 C、餘則為 F)
'''