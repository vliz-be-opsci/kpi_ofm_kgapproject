# todo: python script to add labels to publications text
import requests
import rdflib

OSDGTOOL_URL = "http://osdg-tool:5000/tag"

def mi_data(marine_uri: str):

    """
    get linked data from marine_uri
    """

    if not marine_uri.endswith(".ttl") or not :
        data = requests("")



    return data 

def mi_odsg(marine_uri: str):

    """
    get SDG labels for given marine_uri
    """

    # get ttl from marine_uri & load into graph
    linked_data = 
    # single out text ~ title, english abstract
    data = 
    # api call 
    try:
        data = {'text': pub_info_df_12_24.loc[i, "text"] , 'detailed': False}
        response = requests.post(OSDGTOOL_URL, json=data)
        result = response.json()
        if result['result']:
            pub_info_df_12_24.at[i,'sdgs'] = {item['sdg']: 1 for item in list(result['result'])}
            pub_info_df_12_24.at[i,'result'] = result['result']
        else:
            pub_info_df_12_24.at[i,'result'] = result['result']
            
    except:
        pass
    


