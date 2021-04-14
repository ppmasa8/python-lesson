# print('hello,world!')
# print(1 + 2)

# for i in range(5):
    # print(i)
    
# for i in range(5):
#     if i == 3:
#         break
#     print(i)

# for i in range(3):
#     for j in range(3):
#         print(i,j, sep="-")

# arr = [2,4,6,8,10]
# sum = 0
# for i in arr:
#     sum += i
#     print(sum)

# def say_hello(greeting):
#     print(greeting)

# hello = say_hello
# hello("Good Morning")

# class Student:

#     def __init__(self,name):
#         self.name = name

#     def avg(self,math,eng):
#         print((math + eng)/2)

# a001 = Student("sato")
# print(a001.name)

# a002 = Student("tanaka")
# print(a002.name)

# class Student:

#     def __init__(self,name):
#         self.name = name

#     def calculate_avg(self,data):
#         sum = 0

#         for num in data:
#             sum += num

#         avg =sum/len(data)
#         return avg

#     def judge(self,avg):

#         if(avg >= 60):
#             result="passed"
#         else:
#             result="failed"
#         return result

# a001 = Student("sato")
# data = [70,65,50,90,30]
# avg = a001.calculate_avg(data)
# result = a001.judge(avg)

# print(avg)
# print(a001.name+" "+result)

# SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
#             1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

# def approximate_size(size, a_kilobyte_is_1024_bytes=True):
#     '''Convert a file size to human-readable form.

#     Keyword arguments:
#     size -- file size in bytes
#     a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
#                                 if False, use multiples of 1000

#     Returns: string

#     '''
#     if size < 0:
#         raise ValueError('number must be non-negative')

#     multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
#     for suffix in SUFFIXES[multiple]:
#         size /= multiple
#         if size < multiple:
#             return '{0:.1f} {1}'.format(size, suffix)

#     raise ValueError('number too large')

# if __name__ == '__main__':
#     print(approximate_size(1000000000000, False))
#     print(approximate_size(1000000000000))

# import requests
# from bs4 import BeautifulSoup

# r = requests.get('https://news.yahoo.co.jp')

# soup = BeautifulSoup(r.content,"html.parser")

# print(soup.find("ul","newsFeed_list").text)

