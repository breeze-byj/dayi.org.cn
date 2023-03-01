import requests
from lxml import etree
from encapsulation import json_dump, download_img


def get_disease():
    page_all = 826
    for page_number in range(page_all):
        url = f'https://www.dayi.org.cn/list/0?pageNo={page_number}'
        html=etree.HTML(requests.get(url=url,timeout=(5, 5)).text)
        link_list =html.xpath('.//div[@class="list-left"]/div/div//div[@class="text_name"]/a/@href')
        for link in link_list:
            if '/qa' in link:
                continue
            else:
                resp=requests.get(url=f'https://www.dayi.org.cn{link}', timeout=(5, 5)).text
                html = etree.HTML(resp,etree.HTMLParser())
                data_all = []
                disease_info = {}
                disease_info['疾病名称'] = html.xpath('.//span[@class="name"]')[0].text
                disease_info['疾病说明'] = html.xpath('.//p[@class="intro"]/following::p[1]')[0].text
                tit = html.xpath('.//div[@class="shortDiv"]/p[@class="short-field-title"]')
                sm = html.xpath('.//div[@class="shortDiv"]/span[@class="short-field-content"]')
                for i in range(len(tit)):
                    disease_info[tit[i].text] = sm[i].text
                data_all.append(disease_info)
                info_list = html.xpath('.//section[@class="long-item"]')
                item_all = {}
                for i in range(1, len(info_list)):
                    bt = html.xpath(f'.//section[@class="long-item"][{i}]//h2')[0].text
                    item = {}
                    this_item = html.xpath(f'.//section[@class="long-item"][{i}]//div[@class="two-title"]/span')
                    this_item_info = html.xpath(f'.//section[@class="long-item"][{i}]//div[@class="field-content"]')
                    for index in range(len(this_item)):
                        item[this_item[index].text] = this_item_info[index].xpath('string(.)')
                    item_all[bt] = item
                disease_info['详细说明'] = item_all
                json_dump('./data/疾病.json', data_all)


def get_herbal_medicine():
    page_all = 1070
    for page_number in range(page_all):
        url = f'https://www.dayi.org.cn/list/5?pageNo={page_number}'
        html = etree.HTML(requests.get(url=url, timeout=(5, 5)).text)
        link_list = html.xpath('.//div[@class="list-left"]/div/div//div[@class="text_name"]/a/@href')
        for link in link_list:
            url=f'https://www.dayi.org.cn{link}'
            html=etree.HTML(requests.get(url).text)
            data_all = []
            herbal_medicine_info = {}
            herbal_medicine_info['药材名称'] = html.xpath('.//span[@class="name"]')[0].text
            herbal_medicine_info['药材说明'] = html.xpath('.//p[@class="intro"]/following::p[1]')[0].text
            tit = html.xpath('.//div[@class="shortDiv"]/p[@class="short-field-title"]')
            sm = html.xpath('.//div[@class="shortDiv"]/span[@class="short-field-content"]')
            for i in range(len(tit)):
                herbal_medicine_info[tit[i].text] = sm[i].text
            data_all.append(herbal_medicine_info)
            info_list = html.xpath('.//section[@class="long-item"]')
            item_all = {}
            for i in range(1, len(info_list)):
                bt = html.xpath(f'.//section[@class="long-item"][{i}]//h2')[0].text
                item = {}
                this_item = html.xpath(f'.//section[@class="long-item"][{i}]//div[@class="two-title"]/span')
                this_item_info = html.xpath(f'.//section[@class="long-item"][{i}]//div[@class="field-content"]')
                for index in range(len(this_item)):
                    item[this_item[index].text] = this_item_info[index].xpath('string(.)')
                item_all[bt] = item

            zwx_item = {}
            this_item = html.xpath(
                f'.//div[@class="one-title" and @id="zhiwuxuexinxi"]/..//div[@class="two-title"]/span')
            this_item_info = html.xpath(
                f'.//div[@class="one-title" and @id="zhiwuxuexinxi"]/..//div[@class="field-content"]')
            for index in range(len(this_item)):
                zwx_item[this_item[index].text] = this_item_info[index].xpath('string(.)')
            item_all['植物学信息'] = zwx_item
            herbal_medicine_info['详细说明'] = item_all

            img_url = html.xpath('.//div[@class="thumb-container"]/img/@src')[0]
            img_name = html.xpath('.//div[@class="thumb-container"]/img/@alt')[0]
            download_img(img_url, img_name)

            json_dump('./data/中药材.json', data_all)


def get_symptom():
    page_all = 1070
    for page_number in range(page_all):
        print(f'第{page_number + 1}页')
        url = f'https://www.dayi.org.cn/list/1?pageNo={page_number}'
        html = etree.HTML(requests.get(url=url, timeout=(5, 5)).text)
        link_list = html.xpath('.//div[@class="list-left"]/div/div//div[@class="text_name"]/a/@href')
        for link in link_list:
            url = f'https://www.dayi.org.cn{link}'
            html = etree.HTML(requests.get(url).text)
            data_all = []
            herbal_medicine_info = {}
            herbal_medicine_info['症状名称'] = html.xpath('.//span[@class="name"]/text()')[0]
            herbal_medicine_info['症状说明'] = html.xpath('.//p[@class="intro"]/p')[0].text
            tit = html.xpath('.//div[@class="shortDiv"]/p[@class="short-field-title"]')
            sm = html.xpath('.//div[@class="shortDiv"]/span[@class="short-field-content"]')
            for i in range(len(tit)):
                herbal_medicine_info[tit[i].text] = sm[i].text
            data_all.append(herbal_medicine_info)
            info_list = html.xpath('.//section[@class="long-item"]')
            item_all = {}
            for i in range(1, len(info_list)):
                bt = html.xpath(f'.//section[@class="long-item"][{i}]//h2')[0].text
                item = {}
                this_item = html.xpath(f'.//section[@class="long-item"][{i}]//div[@class="two-title"]/span')
                this_item_info = html.xpath(f'.//section[@class="long-item"][{i}]//div[@class="field-content"]')
                for index in range(len(this_item)):
                    item[this_item[index].text] = this_item_info[index].xpath('string(.)')
                item_all[bt] = item
            item = {}
            this_item = html.xpath(
                f'.//div[@class="one-title" and @id="zhiwuxuexinxi"]/..//div[@class="two-title"]/span')
            this_item_info = html.xpath(
                f'.//div[@class="one-title" and @id="zhiwuxuexinxi"]/..//div[@class="field-content"]')
            for index in range(len(this_item)):
                item[this_item[index].text] = this_item_info[index].xpath('string(.)')
            item_all['检查'] = item

            herbal_medicine_info['详细信息'] = item_all

            img_url = html.xpath('.//div[@class="thumb-container"]/img/@src')[0]
            img_name = html.xpath('.//div[@class="thumb-container"]/img/@alt')[0]
            download_img(img_url, img_name)
            json_dump('./data/症状.json', data_all)