'''
建立一個陣列 [16, 25, 39, 27, 12, 8, 45, 63 ]
'''

data = [16, 25, 39, 27, 12, 8, 45, 63]
def showData(data):
    for i in range(8):
        print(" %2d" % data[i], end=" ")
    print("")

#  第一輪比較 (1 2) (2 3) (3 4) (4 5) (5 6) (6 7) (7 8)
#  經過第一輪的比較，最後一個數為最大的數值
#  因此第二輪開始只需比較 (1 2) (2 3) (3 4) (4 5) (5 6) (6 7) 的數
#  ...
#  到最後一輪只需比較 (1 2)
def bubble(data):
    for i in range(7, -1, -1):
        for j in range(i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

        print("第 %d 次的排序結果為：" % (8 - i), end=" ")
        for i in range(8):
            print(data[i], end=" ")
        print("")


print("===氣泡排序法===")
print("原始資料為：")
showData(data)
print("-------------------------------------------")
bubble(data)
print("-------------------------------------------")
print("排序後的結果為：")
showData(data)