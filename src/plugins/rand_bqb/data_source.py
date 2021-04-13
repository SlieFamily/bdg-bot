import httpx

async def get_image(key:str):
    '''
    根据关键词在图床中提取image的url
    '''
    # 调取表情包链接api
    async with httpx.AsyncClient() as client:
        resp = await client.get('https://my-json-server.typicode.com/sliefamily/bdg-bot/db')
        # logger.debug(resp.json())
        json_data = resp.json()['detail']
    for i in range(0,len(json_data)):
        if json_data[i]["key"] == key:
            return json_data[i]["url"]
    return None