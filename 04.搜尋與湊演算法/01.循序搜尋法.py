'''
使用這輸入陣列長度
產生一個 " " 陣列
陣列中每一個數值介於 1-150 之間

讓使用者 輸入 一個 數值
假如使用者輸入不等於 -1
{
搜尋該 數值 是否在 陣列 當中
假如 在數列當中
印出 數值在陣列當中的位置
假如 不在陣列當中
印出 沒有找到該數值
}

假如使用者輸入不等於 -1
列出所有的資料

'''

import random

# 生成隨機陣列
length = int(input("請輸入陣列長度:"))
data = [0] * length
for i in range(length):
    data[i] = random.randint(1, 150)

val = 0
# 只要使用這輸入的值不是-1，就無限重複該迴圈
while val != -1:
    # 判斷該數值有沒有在陣列當中(預設沒有)
    find = False
    val = int(input("請輸入(1-150)的數值，輸入-1離開："))

    # 使用者輸入不再範圍內的數值
    if val < 1 or val > 150:
        print("===請輸入範圍內的數值===")
    else:
        # 在陣列中有找到該數值
        for i in range(length):
            if val == data[i]:
                print("===在 %2d 的位置找到鍵值 [%3d]===" % (i + 1, data[i]))
                find = True
        # 在陣列中沒找到該數值
        if val != -1 and not find:
            print("===沒有找到鍵值 [%3d]===" % val)
# 當使用者輸入-1，顯示所有資料內容
print("\n-------------------------------------------------------------------------------")
print("\n資料內容：")
for i in range(10):
    for j in range(int(length/10)):
        print("%2d[%3d]" % (i * int(length / 10) + j + 1, data[i * int(length / 10) + j]), end=",")
    print("\n")