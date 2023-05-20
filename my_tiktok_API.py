from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

app = Flask(__name__)

@app.route('/tiktok/<username>', methods=['GET'])
def get_tiktok_data(username):
    try:
        source = requests.get(f'https://www.tiktok.com/@{username}')
        source.raise_for_status()

        soup = BeautifulSoup(source.text, 'html.parser')
        user_info = soup.find('h3', class_="tiktok-12ijsdd-H3CountInfos e1457k4r0").find_all('div')
        user_total_following = user_info[0].find('strong').text
        user_total_followers = user_info[1].find('strong').text
        user_total_likes = user_info[2].find('strong').text

        user_data = {
            'Username': username,
            'Total Followers': user_total_followers,
            'Total Following': user_total_following,
            'Total Likes': user_total_likes
        }

        video_container = soup.find('div', class_="tiktok-yvmafn-DivVideoFeedV2 ecyq5ls0")
        videos = video_container.find_all('div', class_="tiktok-x6y88p-DivItemContainerV2 e19c29qe7")

        video_data = []
        for video in videos:
            title = video.find('img', {'class': 'tiktok-1itcwxg-ImgPoster'}).get('alt')
            link = video.find('a', {'href': True}).get('href')

            views_elem = video.find('div', {'class': 'tiktok-11u47i-DivCardFooter e148ts220'}).strong
            views = views_elem.get_text(strip=True) if views_elem else None

            likes_elem = video.find('div', {'class': 'tiktok-11u47i-DivCardFooter e148ts220'})
            likes = likes_elem.get_text(strip=True) if likes_elem else None

            video_data.append({'Video_title': title, 'Views': views, 'Likes': likes, 'Link': link})

        response = {
            'User Information': user_data,
            'Videos Information': video_data
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
