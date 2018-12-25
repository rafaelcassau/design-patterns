"""
Proxy is a structural design pattern that provides an object 
that acts as a substitute for a real service object used by a 
client. Proxy receives client requests, does some work 
(access control, caching, etc.) and then passes request to a 
service object.
"""

import time
import random


class Video:

    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.data = 'Random video.'


class ThirdPartyYoutubeLibInterface:

    def popular_videos(self) -> dict:
        raise NotImplementedError()

    def get_video(self, video_id: str) -> Video:
        raise NotImplementedError()


class ThirdPartyYoutubeClass(ThirdPartyYoutubeLibInterface):

    def popular_videos(self) -> dict:
        self._conect_to_server('https://youtube.com')
        return self._get_random_videos()

    def get_video(self, video_id: str) -> Video:
        self._conect_to_server('https://youtube.com/{}/'.format(video_id))
        return self._get_some_video(video_id)

    # Fake methods to simulate network activity. They are slow as a real life.

    def _experience_network_latency(self):
        random_latency = random.randint(5, 10)
        time.sleep(random_latency)

    def _conect_to_server(self, server: str):
        print(f'Connecting to {server} ...')
        self._experience_network_latency()
        print('Connected! \n')

    def _get_random_videos(self) -> dict:
        print('Downloading populars...')

        self._experience_network_latency()

        videos = {}
        videos['catzzzzzzzzz'] = Video('sadgahasgdas', 'Catzzzz.avi')
        videos['mkafksangasj'] = Video('mkafksangasj', 'Dog play with ball.mp4')
        videos['dancesvideoo'] = Video('asdfas3ffasd', 'Dancing video.mpq')
        videos['dlsdk5jfslaf'] = Video('dlsdk5jfslaf', 'Barcelona vs RealM.mov')
        videos['3sdfgsd1j333'] = Video('3sdfgsd1j333', 'Programing lesson#1.avi')

        print('Done! \n')
        return videos

    def _get_some_video(self, video_id: str) -> Video:
        print('Downloading video...')

        self._experience_network_latency()
        video = Video(video_id, 'Some video title')

        print('Done! \n')
        return video


class YoutubeCacheProxy(ThirdPartyYoutubeLibInterface):
    
    def __init__(self):
        self.youtube_service = ThirdPartyYoutubeClass()
        self.cache_popular = {}
        self.cache_all = {}

    def popular_videos(self) -> dict:
        if not self.cache_popular:
            self.cache_popular = self.youtube_service.popular_videos()
        else:
            print('Retrieved list from cache.')

        return self.cache_popular

    def get_video(self, video_id: str) -> Video:
        video = self.cache_all.get(video_id)
        if not video:
            video = self.youtube_service.get_video(video_id)
            self.cache_all[video_id] = video
        else:
            print(f'Retrieved video {video_id} from cache.')

        return video

    def reset(self):
        self.cache_all.clear()
        self.cache_popular.clear()


class YoutubeDownloader:

    def __init__(self, api: ThirdPartyYoutubeLibInterface):
        self.api = api

    def render_video_page(self, video_id: str):
        video = self.api.get_video(video_id)
        print('\n-------------------------------')
        print('Video page (imagine fancy HTML)')
        print(f'ID: {video_id}')
        print(f'Title: {video.title}')
        print(f'VIdeo: {video.data}')
        print('-------------------------------\n')

    def render_popular_videos(self):
        videos = self.api.popular_videos()
        print('\n-------------------------------')
        print('Most popular videos on Youtube (imagine fancy HTML)')
        for video in videos.values():
            print(f'ID: {video.id} / Title: {video.title}')
        print('-------------------------------\n')


# Demo (Client Code)

class Demo:

    def run(self):
        naive_downloader = YoutubeDownloader(ThirdPartyYoutubeClass())
        smart_downloader = YoutubeDownloader(YoutubeCacheProxy())

        naive = self.test(naive_downloader)
        smart = self.test(smart_downloader)
        result = naive - smart
        print(f'Time saved by caching proxy: {result} ms.')

    def test(self, downloader: YoutubeDownloader) -> int:
        start_time = time.time()

        # User behavior in our app
        downloader.render_popular_videos()
        downloader.render_video_page('catzzzzzzzzz')
        downloader.render_popular_videos()
        downloader.render_video_page('dancesvideoo')
        # Users might visit the same page quite often.
        downloader.render_video_page('catzzzzzzzzz')
        downloader.render_video_page('someothervid')

        end_time = time.time()
        estimated_time = end_time - start_time
        print(f'Time elapsed {estimated_time} ms. \n')

        return estimated_time


demo_client = Demo()
demo_client.run()