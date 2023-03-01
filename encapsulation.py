import csv
import ast
import configparser
import glob
import os
import pandas as pd
import requests
import yaml


def download_img(url, num):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        # 将内容写入图片
        open(f'./{num}.jpg', 'wb').write(r.content)
    del r

# 写入title
def wri_tit(csv_name, tit_list):
    if os.access(csv_name, os.F_OK):
        df = pd.read_csv(csv_name, header=None, names=tit_list)
        df.to_csv(csv_name, index=False)


# csv合并
def merge():
    csv_list = glob.glob('F:/*.csv')
    print(u'共发现%s个CSV文件'% len(csv_list))
    print(u'正在处理............')
    for i in csv_list:
        fr = open(i,'r').read()
        with open('F:/hebing.csv','a') as f:
            f.write(fr)
    print(u'合并完毕！')


def str_sub(string):
    new = []
    for s in string:
        new.append(s)
    if new[1]==' ':
        del new[1]
    return ''.join(new)


# 写入csv
def write_csv(file_name, data_list_name):
    with open(file_name, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for row in data_list_name:
            writer.writerow(row)


def delete_file():
    file_list = ['trial_info', 'trial_pi_info', 'trial_site_info', 'trial_ec_info']
    for file_name in file_list:
        try:
            print('删除' + f'{file_name}')
            os.remove(f'data/{file_name}.csv')
        except OSError:
            print(f'{file_name}' + '不存在,跳过')
            pass


# 返回元素个数
def get_ele_number(ele):
    num = len(ele)
    return num



def yaml_load(path):
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    return data


def yaml_load_all(path):
    with open(path, mode='r', newline='', encoding='utf8') as file:
        data = yaml.safe_load_all(file, Loader=yaml.FullLoader)
    return data


def yaml_load_all_list(path):
    with open(path, "r") as f:
        data = list(yaml.safe_load_all(f, Loader=yaml.FullLoader))
    return data


def yaml_write_all(data, path):
    with open(path, mode='w', newline='', encoding='utf8') as file:
        yaml.safe_dump_all(data, file, encoding='utf-8', allow_unicode=True)


def yaml_write(data, path):
    with open(path, mode='w', newline='', encoding='utf8') as file:
        yaml.safe_dump(data, file, encoding='utf-8', allow_unicode=True)


'''
csv_lod:读取文件
filePath:文件路径及文件 示例* d:\\vsd\\csv\\123.csv
return: [["line1","data1"],["line2","data2"]]
'''


def csv_lod(filePath):
    with open(filePath, mode='r', newline='', encoding='utf8') as file:
        return list(csv.reader(file))


'''
csv_dict_lod:以字典的格式读取csv
filePath:文件路径及文件 示例* d:\\vsd\\csv\\123.csv
return:[{"head1":"zhangsan","head2":"lisi","head3":"wangwu"}] 
'''


def csv_dict_lod(filePath):
    with open(filePath, mode='r', newline='', encoding='utf8') as file:
        return list(csv.DictReader(filter))


'''
csv_writes:写入单行数据
filePath:文件路径及文件 示例* d:\\vsd\\csv\\123.csv
data:写入该文件的数据 示例* ['data1','data2'] 
'''


def csv_write(filePath, data):
    with open(filePath, mode='w', newline='', encoding='utf8') as file:
        fw = csv.writer(file)
        fw.writerow(data)


'''
csv_writes:写入多行数据
filePath:文件路径及文件 示例* d:\\vsd\\csv\\123.csv
data:写入该文件的数据 示例* [('data1','data2'),('data3','data4')] 
'''


def csv_writes(filePath, data):
    with open(filePath, mode='w', newline='', encoding='utf8') as file:
        fw = csv.writer(file)
        fw.writerows(data)
    pass


'''
csv_dict_write:写入单行数据
filePath:文件路径及文件 示例* d:\\vsd\\csv\\123.csv
file_head:写入的表头 示例* ['head1','head2','head3']
data:写入该文件的数据 示例* {"head1":"zhangsan","head2":"lisi","head3":"wangwu"}
'''


def csv_dict_write(filePath, file_head, data):
    with open(filePath, mode='w', newline='', encoding='utf8') as file:
        csv_dict = csv.DictWriter(file, fieldnames=file_head)
        csv_dict.writeheader()  # 写入表头
        csv_dict.writerow(data)  # 写入数据


'''
csv_dict_writes:写入多行数据
filePath:文件路径及文件 示例* d:\\vsd\\csv\\123.csv
file_head:写入的表头 示例* ['head1','head2','head3']
data:写入该文件的数据 示例* [{"head1":"zhangsan","head2":"lisi","head3":"wangwu"}] 
'''


def csv_dict_write_list(filePath, file_head, data):
    with open(filePath, mode='w', newline='', encoding='utf8') as file:
        csv_dict = csv.DictWriter(file, fieldnames=file_head)
        csv_dict.writeheader()  # 写入表头
        csv_dict.writerows(data)  # 写入数据


'''
json_load:读取json文件
return: json数据格式
'''


def json_load(filePath):
    with open(filePath, mode='r', newline='', encoding='utf8') as file:
        return json.load(file)


'''
json_dump:写入json文件
data： 写入的数据
filePath:文件路径及文件 示例* d:\\vsd\\csv\\123.json
'''


def json_dump(filePath, data):
    with open(filePath, mode='a', newline='', encoding='utf8',) as file:
        json.dump(data, file,ensure_ascii=False)


'''
json_dumps:将数据转换成字符串
data: [{'username':'zhangsan','sex':6},{'username':'lisi','sex':3}]
return: 返回为当前数据的字符串类型
'''


def json_dumps(data):
    return json.dumps(data)


'''
json_loads:将字符串数据解析为python数据格式
data： "['hello',{'username':'xiaoliu'}]"
return: python数据类型
'''


def json_loads(data):
    return json.loads(data)


'''
ini_load:将字符串数据解析为python数据格式
data： "['hello',{'username':'xiaoliu'}]"
return: python数据类型
'''


def ini_load(data):
    return json.loads(data)


'''
ini_write:将数据写入到ini文件中
key：uat
data： "{'ip':'192.168.1.101','port':'3000'}"

[uat]
ip = 192.168.1.101
port = 3000
'''


def ini_write(filePath, key, data):
    config = configparser.ConfigParser()
    config[key] = data
    with open(filePath, mode='w', newline='', encoding='utf8') as file:
        config.write(file)


'''
ini_load:将数据写入到ini文件中
return："{'ip':'192.168.1.101','port':'3000'}"
'''


def ini_load(filePath):
    config = configparser.ConfigParser()
    config.read(filePath)
    data = {}
    for section in config.sections():
        print(section, config[section])
        data[section] = {}
        for key in config[section]:
            data[section][key] = config[section][key]
            print(key, config[section].get(key))
    return data


'''
type : 
    # <class 'dict'>将表头作为key,将每列的值放在列表中,将列表作为value
    list----> {'学号': [1, 2, 3, 4, 5, 6, 7, 8], '姓名': ['李连杰', '甄子丹', '成龙', '洪金宝', '吴京', '李小龙', '赵文卓', '刘亦菲']}
    # 将行的索引值作为key,将存放数据的字典作为value
    index---> {0: {'学号': 1, '姓名': '李连杰', '年龄': 27, '攻击力': 96}, 1: {'学号': 2, '姓名': '甄子丹', '年龄': 27, '攻击力': 93}}
    # 大列表嵌套多字典,适合测试用例
    records-> [{'学号': 1, '姓名': '李连杰', '年龄': 27, '攻击力': 96}, {'学号': 2, '姓名': '甄子丹', '年龄': 27, '攻击力': 93}]
    dict----> {'学号': {0: 1, 1: 2, 2: 3}, '姓名': {0: '李连杰', 1: '甄子丹', 2: '成龙'}}
    split---> {'index': [0, 1, 2, 3, 4, 5, 6, 7], 'columns': ['学号', '姓名', '年龄', '攻击力'], 'data': [[1, '李连杰', 27, 96]}
'''


def excel_load(filePath, type):
    return_data = {'data': None}
    with open(filePath, mode='r', newline='', encoding='utf8') as file:
        return_data['data'] = pa.read_excel(file).to_dict(orient=type)
    return return_data
