import os
import json
from googleapiclient.discovery import build


class Channel:
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

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с API youtube"""
        # YoutubeAPI_key скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.getenv('YoutubeAPI_key')
        # создает специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

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


class Video:
    """Класс видео с Youtube"""

    def __init__(self, video_id: str):
        self.video_id = video_id
        self.info = self.get_service().videos().list(part='snippet,statistics', id=self.video_id).execute()
        self.title = self.info["items"][0]["snippet"]["title"]
        self.view_count = self.info["items"][0]["statistics"]["viewCount"]
        self.like_count = self.info["items"][0]["statistics"]["likeCount"]

    def __str__(self):
        return self.title

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с API youtube"""
        # YoutubeAPI_key скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.getenv('YoutubeAPI_key')
        # создает специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube


class PLVideo(Video):
    """Класс видео из play-листа Youtube"""

    def __init__(self, video_id: str, pl_id: str):
        super().__init__(video_id)
        self.pl_id = pl_id
        self.pl_info = self.get_service().playlists().list(part='snippet', id=self.pl_id).execute()
        self.pl_title = self.pl_info["items"][0]["snippet"]["title"]

    def __str__(self):
        return f'{self.title} ({self.pl_title})'
