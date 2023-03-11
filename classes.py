import datetime
import os
import json
from googleapiclient.discovery import build
import isodate


class Youtube:
    """Класс API youtube"""

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с API youtube"""
        # YoutubeAPI_key скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.getenv('YoutubeAPI_key')
        # создает специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube


class Channel(Youtube):
    """Класс канала Youtube"""

    def __init__(self, channel_id: str):
        self.__channel_id = channel_id
        # получает данные о канале по его ID
        self.info = self.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = self.info["items"][0]["snippet"]["title"]
        self.description = self.info["items"][0]["snippet"]["description"]
        self.url = "https://www.youtube.com/channel/" + self.__channel_id
        self.subscriber_count = self.info["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.info["items"][0]["statistics"]["videoCount"]
        self.view_count = self.info["items"][0]["statistics"]["viewCount"]

    def __str__(self):
        return f'Youtube-канал: {self.title}'

    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __gt__(self, other):
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __lt__(self, other):
        return int(self.subscriber_count) < int(other.subscriber_count)

    @property
    def channel_id(self) -> str:
        """Возвращает ID канала"""
        return self.__channel_id

    def print_info(self):
        """Выводит в консоль информации о канале Youtube"""
        print(json.dumps(self.info, indent=2, ensure_ascii=False))

    def to_json(self, file_name: str):
        """Сохраняет информацию по каналу, хранящуюся в атрибутах экземпляра класса Channel, в json-файл"""
        data = {
            "id": self.__channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriberCount": self.subscriber_count,
            "videoCount": self.video_count,
            "viewCount": self.view_count
        }
        with open(file_name, "w", encoding="UTF-8") as file:
            json.dump(data, file, ensure_ascii=False, indent='\t')


class Video(Youtube):
    """Класс видео с Youtube"""

    def __init__(self, video_id: str):
        self.video_id = video_id
        self.info = self.get_service().videos().list(part='snippet,statistics', id=self.video_id).execute()
        self.title = self.info["items"][0]["snippet"]["title"]
        self.view_count = self.info["items"][0]["statistics"]["viewCount"]
        self.like_count = self.info["items"][0]["statistics"]["likeCount"]

    def __str__(self):
        return self.title


class PLVideo(Video):
    """Класс видео из play-листа Youtube"""

    def __init__(self, video_id: str, pl_id: str):
        super().__init__(video_id)
        self.pl_id = pl_id
        self.pl_info = self.get_service().playlists().list(part='snippet', id=self.pl_id).execute()
        self.pl_title = self.pl_info["items"][0]["snippet"]["title"]

    def __str__(self):
        return f'{self.title} ({self.pl_title})'


class PlayList(Youtube):
    """Класс play-листа Youtube"""

    def __init__(self, pl_id: str):
        self.pl_id = pl_id
        self.pl_info = self.get_service().playlists().list(part='snippet', id=self.pl_id).execute()
        self.pl_items_info = self.get_service().playlistItems().list(playlistId=pl_id, part='contentDetails',
                                                                     maxResults=50).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.pl_items_info['items']]
        self.pl_videos_info = self.get_service().videos().list(part='contentDetails,statistics',
                                                               id=','.join(video_ids)).execute()
        self.pl_title = self.pl_info["items"][0]["snippet"]["title"]
        self.url = "https://www.youtube.com/playlist?list=" + self.pl_id

    def __str__(self):
        return f'{self.pl_title}'

    @property
    def total_duration(self) -> datetime.timedelta:
        """Возвращает суммарную длительность play-листа ч:м:с"""
        total_duration = datetime.timedelta()

        for video in self.pl_videos_info['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration

        return total_duration

    def show_best_video(self) -> str:
        """Возвращает ссылку на самое популярное видео из play-листа"""
        best_video_url = ''
        like_count = 0

        for video in self.pl_videos_info['items']:
            if int(video['statistics']['likeCount']) > like_count:
                like_count = int(video['statistics']['likeCount'])
                best_video_url = "https://youtu.be/" + video['id']

        return best_video_url
