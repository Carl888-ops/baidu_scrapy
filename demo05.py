'''
通过浏览器模拟向百度发送请求
'''
import urllib.request
import urllib.parse

word = input('请输入您想要查询的内容')
url = 'http://www.baidu.com/s?'

#参数写成一个字典
data = {
    'ie':'utf-8',
    'wd':word,
}
#urllib.parse
    #quote   url编码格式  ，将中文转化文%xxxxx
    #unquote url解码函数  ，将%xxxx转换为中文
    #urlencode  给一个字典，将字典拼接为query_string
query_string = urllib.parse.urlencode(data)
url += query_string

#向url发送请求
response = urllib.request.urlopen(url)

filename = word+'.html'
with open(filename,'wb') as f:
    f.write(response.read())
