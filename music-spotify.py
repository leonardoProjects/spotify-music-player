from webbrowser import open
import requests
import json
from time import sleep
import spotify_token as st

def get_music(query, username, password):  #coloque seu email ou username e sua senha do spotify para pegar o token 
    data = st.start_session(username, password)
    access_token = data[0]
  
    header = {"Authorization":f"Bearer {access_token}"} 

    url = f'https://spclient.wg.spotify.com/searchview/android/v4/search/{query}?&locale=pt-br&username=danisosigan&country=BR&catalogue=premium&limit=1'
 
    resp = requests.get(url, headers=header) 
   # print(resp.text)
    if 'target' in resp.text:
        data = json.loads(resp.text)
        id = data['body'][0]['children'][0]['target']['uri']
        id = id.split(':')[-1]    
        url = f'https://open.spotify.com/track/{id}'
        print(url)
        print('Abrindo música...')
        sleep(2)
        open(url)
    else:
    	print('Música não encontrada!')
	
query = input('Qual música quer escutar? ')

get_music(query)