from classes import Channel


def main():
    shulman = Channel('UCL1rJ0ROIw9V1qFeIN0ZTZQ')  # Екатерина Шульман
    vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')  # вДудь

    shulman.print_info()
    vdud.print_info()

    print(vdud.title)
    print(vdud.description)
    print(vdud.url)
    print(vdud.subscriber_count)
    print(vdud.video_count)
    print(vdud.view_count)

    print(vdud.channel_id)
    # vdud.channel_id = "Новое название"

    print(Channel.get_service())

    vdud.to_json('vdud.json')
    shulman.to_json("shulman.json")


if __name__ == "__main__":
    main()
