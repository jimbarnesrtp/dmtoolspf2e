import csv
import os
from bs4 import BeautifulSoup
import re

class ShopLoader():
    
    link_list = ['name','source', 'rarity', 'category', 'subcategory']
    
    def load_items_from_csv(self):
        item_rows = []
        directory_path = os.getcwd()
        with open(directory_path+"/csvs/raw-aon2-export.csv") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
               item_rows.append(row)
        good_item_rows = []
        for item in item_rows:
            good_item_row = {}
            for key in item.keys():
                good_item_row[key.replace("\ufeff","").replace('"','').lower()] = item[key]
            good_item_rows.append(good_item_row)
        return good_item_rows
    
    def normalize_data(self, data_list):
        norm_data = []

        for data in data_list:
            #print(data)
            keys = list(data.keys())
            new_data = {}
            for key in keys:
                if key in self.link_list:
                    new_data[key] = self.norm_link(data[key])
                elif key == 'pfs':
                    new_data[key] = self.norm_pfs(data[key])
                elif key == 'level':
                   new_data[key] = self.norm_possible_number(data[key])
                elif key =='price':
                    new_data[key] = data[key]
                elif key == 'traits':
                    new_data[key] = self.norm_multi(data[key])
                    
            new_data['link'] = self.norm_url(data['name'])
            norm_data.append(new_data)

        return norm_data

    def norm_link(self, name):
        #print("norm link:", name)
        if name == "—" or name == "":
            return name
        else:
            soup = BeautifulSoup(name, 'html5lib')
            href = soup.find_all("a")
            return href[0].text
    
    def norm_pfs(self, pfs):
        soup = BeautifulSoup(pfs, 'html5lib')
        img = soup.find_all("img")
        if(len(img) == 0):
            return "Excluded"
        else:
            return img[0]['alt']
    
    def norm_url(self, url):

        #print("URL:", url)
        soup = BeautifulSoup(url, 'html5lib')
        href = soup.find_all("a")
        return "https://2e.aonprd.com/"+href[0]['href']

    def norm_multi(self, multi):
        #print("Multi:", multi)
        if multi == "—" or multi == "":
            return multi
        ret_multi = []
        found_list = re.finditer("<u>(.*?)</u>", multi)
        for match in found_list:
            ret_multi.append(self.norm_link(match.group()))
        
        return ret_multi

    def norm_possible_number(self, input):
        
        if "—" in input:
            return input
        else:
            return int(input)
