from youtube_api import YouTubeDataAPI
import time
import pandas as pd
from client import api_key

# Set up youtube api connection
yt = YouTubeDataAPI(api_key)

# Create a dictionary containing the ids for the playlists
playlists = {'Nectar':'OLAK5uy_nq9PSQZCORK_TXwQuv6OL6pFIR_JuMfNM','Ballads 1':'OLAK5uy_mjAOCotH4qLPkVZdozo80M-H6jGLyhz7I','In Tongues':'OLAK5uy_mgqGb-owbElA7d0Mzx0xv2ZP52ykeVvFY'}

# Titles for the playlists
play_title = ['Nectar','Ballads 1','In Tongues']

# Create a function to request information from the youtube api
def joji(play_id):
    # Dictionary to hold collected data
    metadata = {}
    # Get each video in the playlist
    videos = yt.get_videos_from_playlist_id(play_id)
    # For each video in the playlist collect the title, view count, like/dislike count, comment count, and the date it was published
    for vid in videos:
        meta = yt.get_video_metadata(video_id=vid['video_id'])
        metadata[meta['video_title']] = {'date':meta['video_publish_date'],'view count':meta['video_view_count'],'Like count':meta['video_like_count'], 'dislike count':meta['video_dislike_count'],'comments count':meta['video_comment_count']}

    # Return the data we just collected    
    return(metadata)

# For each playlist title, create a pandas dataframe and export the data as a csv
for i in play_title:
    df = pd.DataFrame.from_dict(joji(playlists[i]),orient='index')
    df.to_csv(f'{i}.csv')
    time.sleep(2)