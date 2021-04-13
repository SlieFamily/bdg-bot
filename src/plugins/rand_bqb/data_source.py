import httpx
import json
async def get_image(key:str):
    '''
    根据关键词在图床中提取image的url
    '''
    with open('rand_bqb/BQkeys.json','r',encoding='utf8')as fp:
        json_data = json.load(fp)
    for i in range(0,len(json_data)):
        if json_data[i]["key"] == key:
            await json_data[i]["url"]
    await None