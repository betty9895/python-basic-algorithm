'''

'''
data = [16, 25, 39, 27, 12, 8, 45, 63]
def showData(data):
    for i in range(8):
        print(" %2d" % data[i], end=" ")

# 排好(1 2)的順序後，再將3跟前面的元素做比較，放入正確的位置後，將後面的元素往後移一個位置
# 排好(1 2 3)的順序後，再將4跟前面的元素做比較，放入正確的位置後，將後面的元素往後移一個位置
# ...
# 排好(1 2 3 4 5 6 7)的順序後，再將8跟前面的元素做比較，放入正確的位置後，將後面的元素往後移一個位置
# 須建立一個temp去承接目前要比較的元素
# 建立一 ln 為 tamp 前一個元素
# temp 需走訪 ln 前每一個數字跟其作比較並找出其整確的位置
# 將地的 ln 全部往後移一個次序

def insert(data):
    for i in range(1, 8):
        temp = data[i]
        ln = i-1
        while temp < data[ln] and ln >= 0:
            data[ln+1] = data[ln]
            ln -= 1
            data[ln+1] = temp

print("===插入排序法===")
print("原始資料為：")
showData(data)
insert(data)
print("\n----------------------------------------")
print("排序後的資料為：")
showData(data)
