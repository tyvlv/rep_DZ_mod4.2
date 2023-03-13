import json

from classes import Channel, Video, PLVideo, PlayList


def main():
    # shulman = Channel('UCL1rJ0ROIw9V1qFeIN0ZTZQ')  # Екатерина Шульман
    # vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')  # вДудь
    # #
    # print(shulman)
    # print(vdud)
    #
    # print(vdud.subscriber_count)
    # print(shulman.subscriber_count)
    # print(shulman + vdud)
    # print(vdud > shulman)
    # print(vdud < shulman)
    #
    # video1 = Video('Q0lHb-FCATk')
    # print(json.dumps(video1.info, indent=2, ensure_ascii=False))
    # print(video1.title)
    # print(video1.view_count)
    # print(video1.like_count)
    # print(video1)
    #
    # video2 = PLVideo('W9P_qUnMaFg', 'RDCLAK5uy_kWiJXUNLZM9EyS3GBGznl1ku8_cOos97U')
    # print(json.dumps(video2.pl_info, indent=2, ensure_ascii=False))
    # print(video2.title)
    # print(video2.view_count)
    # print(video2.like_count)
    # print(video2.pl_title)
    # print(video2)

    # video1 = Video('9lO06Zxhu88')
    # video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
    # print(video1)
    # print(video2)
    #
    # pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
    # print(pl)
    # print(pl.url)
    # print(json.dumps(pl.pl_videos_info, indent=2, ensure_ascii=False))
    # print(pl.total_duration)
    # print(type(pl.total_duration))
    # print(pl.total_duration.total_seconds())
    # print(pl.show_best_video())

    broken_video = Video('broken_video_id')
    print(broken_video.title)
    print(broken_video.like_count)


if __name__ == "__main__":
    main()
