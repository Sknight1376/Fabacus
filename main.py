import json
import os
import pandas as pd

fpath = 'Data/listings_0.json'


def item_details(items):

    all_rows = []

    for item in items:

        # Iterating across all items in dict, assuming possibility of multiple values in product_type
        rows = map(lambda a,b,c,d,e : {'item_id' : a,
                        'country' : b,
                        'domain_name' : c,
                        'marketplace' : d,
                        'product_type' : e['value']}, 
                            [item['item_id']]*len(item['product_type'])
                            ,[item['country']]*len(item['product_type'])
                            ,[item['domain_name']]*len(item['product_type'])
                            ,[item['marketplace']]*len(item['product_type'])
                            ,item['product_type'])
        
        all_rows = all_rows+[i for i in rows]

    return all_rows

def item_name(items):

    all_rows = []

    for item in items:

        # Iterating across all items in dict, assuming possibility of multiple values item_name
        rows = map(lambda a,b : {'item_id' : a,
                        'item_name' : b['value'],
                        'item_name_language' : b['language_tag']}, [item['item_id']]*len(item['item_name']),item['item_name'])
        
        all_rows = all_rows+[i for i in rows]


    return all_rows

def item_keywords(items):

    all_rows = []

    for item in items:
        if 'item_keywords' in item.keys():

             # Iterating across all items in dict, assuming possibility of multiple values item_keywords
            rows = map(lambda a,b : {'item_id' : a,
                            'keywords_name' : b['value'],
                            'item_keywords_language' : b['language_tag']}, [item['item_id']]*len(item['item_keywords']),item['item_keywords'])
            
            all_rows = all_rows+[i for i in rows]


    return all_rows



if __name__ == '__main__':
    try:
        with open(fpath) as file:
            constructed_json = json.load(file)

    except:
        with open(fpath) as file:
            file_list= []
            for line in file:
                file_list.append(line)
        constructed_json = json.loads('['+','.join(file_list)+']')


    item_details_dataframe  = pd.DataFrame(item_details(constructed_json))
    item_details_dataframe.to_csv('Output/item_details.csv', index=False)

    item_names_dataframe  = pd.DataFrame(item_name(constructed_json))
    item_names_dataframe.to_csv('Output/item_names.csv', index=False)

    item_keywords_dataframe  = pd.DataFrame(item_keywords(constructed_json))
    item_keywords_dataframe.to_csv('Output/item_keywords.csv', index=False)