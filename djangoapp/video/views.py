import json

import requests
from django.shortcuts import render

from video.models import Video
from youtubeapp.settings import config
from .forms import searchForm


def search_view(request):
    def get_search_list_from_youtube(keyword):

        YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'
        KEY_par = config['youtube']['API_KEY_YOUTUBE']
        PART_Par = 'snippet'
        Q_par = keyword
        MaxResults = 10
        TYPE_Par = 'video'

        params = {
            'key': KEY_par,
            'part': PART_Par,
            'maxResults': MaxResults,
            'q': Q_par,
            # 'type': TYPE_Par
        }

        r = requests.get(YOUTUBE_URL, params=params)
        result = r.text
        result_dict = json.loads(result)

        items = result_dict['items']

        for index, item in enumerate(items):
            # if item['id']['videoId']:
            #
            # else:
            #     video_id = ''
            video_id = item['id']['videoId']
            title = item['snippet']['title']
            channelId = item['snippet']['channelId']
            description = item['snippet']['description']
            # published_date_str = item['snippet']['publishedAt']
            # published_date = parse(published_date_str)
            Video.objects.create(title=title, video_id=video_id, description=description, ch_id=channelId)

        return items

    if request.method == 'POST':
        form = searchForm(data=request.POST)

        if form.is_valid():
            keyword = request.POST['search_keyword']
            items = get_search_list_from_youtube(keyword)
            # for 를 이용하여 items을 돌려줌
            get_search_list_from_youtube(keyword)
            # items = Video.objects.all()

            context = {
                'form': form,
                'items2': items,
            }
            return render(request, 'video/search.html', context)

        else:
            form.add_error(None, '실패')

    else:
        form = searchForm()
        items = Video.objects.all()

    context = {
        'form': form,
        'items': items,
    }
    return render(request, 'video/search.html', context)
