from youtube_api import YouTubeDataAPI
import time
import pandas as pd
from client import api_key
yt = YouTubeDataAPI(api_key)

playlists = {'Nectar':'OLAK5uy_nq9PSQZCORK_TXwQuv6OL6pFIR_JuMfNM','Ballads 1':'OLAK5uy_mjAOCotH4qLPkVZdozo80M-H6jGLyhz7I','In Tongues':'OLAK5uy_mgqGb-owbElA7d0Mzx0xv2ZP52ykeVvFY'}

def joji(play_id):
    metadata = {}
    videos = yt.get_videos_from_playlist_id(play_id)
    for vid in videos:
        meta = yt.get_video_metadata(video_id=vid['video_id'])
        metadata[meta['video_title']] = {'title':meta['video_title'],'date':meta['video_publish_date'],'view count':meta['video_view_count'],'Like count':meta['video_like_count'], 'dislike count':meta['video_dislike_count'],'comments count':meta['video_comment_count']}
        

    return(metadata)

# print(joji(playlists['Nectar']))
# time.sleep(2)
# print(joji(playlists['Ballads 1']))
# time.sleep(2)
print(joji(playlists['In Tongues']))