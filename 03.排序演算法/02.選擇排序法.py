'''
建立原始陣列
建立顯示資料的函數
{
逐一顯示陣列中每個元素
}
建立選擇排序演算法
{
選擇陣列中最小的元素放到第一個位置
選擇陣列中第二小的元素放到第二個位置
...
選擇陣列中第七小的元素放到第七個位置

(選擇 1 - 7)     比較兩者的大小   走訪(i+1 - 8)
}

'''

data = [16, 25, 39, 27, 12, 8, 45, 63]
def showData(data):
    for i in range(8):
        print(" %2d" % data[i], end=" ")

# 走訪陣列中2-8的數，選擇陣列中最小的數和第1個數較換位置
# 走訪陣列中3-8的數，選擇陣列中第二小的數和第2個數較換位置
# ....
# 走訪陣列中7-8的數，選擇陣列中第七小的數和第8個數較換位置
def select(data):
    for i in range(7):
        for j in range(i+1, 8):
            if data[j] < data[i]:
                data[i], data[j] = data[j], data[i]




print("===選擇排序法===")
print("原始資料為：")
showData(data)
select(data)
print("\n----------------------------------------")
print("排序後的資料為：")
showData(data)

