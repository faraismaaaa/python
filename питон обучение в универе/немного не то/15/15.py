# def main():
#     str = input('Ввод строки: ')
#     new_str = ''
#     ls = str.split()
#     for x in ls:
#         if len(x)%2==0:
#             new_str += x + ' '
#     return new_str
# print(main())

# def main(k):
#     with open('text_0.txt', encoding='utf8') as ls:
#         string = ls.readline()
#     string = string.split()
#     return string[k::]
# print(*main(int(input('Сколько слов удаляем?: '))))

def main():
    with open('text_1.txt') as ls:
        string = ls.readline()
    tmp_str = []
    for x in string.split():
        count = 0
        for chr in x.lower():
            if chr == 'ж' or chr == 'ш' or chr == 'щ' or chr == 'ч':
                count += 1
        if count != 0:
            tmp_str.append([count,x])
    return tmp_str

def bubble_sort(array):
    for j in range(len(array)-1):
        for i in range(len(array)-1):
            if (array[i][0] < array[i+1][0]):
                array[i], array[i+1] = array[i+1], array[i]
    tmp_ls = ''
    count = array[0][0]
    for x in array[0][1]:
        if x == 'ж' or x == 'ш' or x == 'щ' or x == 'ч':
            tmp_ls += '&'
        else:
            tmp_ls += x
    array[0] = [count, tmp_ls]
    return array[0]
print(*bubble_sort(main()))
