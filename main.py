from classes import Channel


def main():
    shulman = Channel('UCL1rJ0ROIw9V1qFeIN0ZTZQ')  # Екатерина Шульман
    vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')  # вДудь

    print(shulman)
    print(vdud)

    print(vdud.subscriber_count)
    print(shulman.subscriber_count)
    print(shulman + vdud)
    print(vdud > shulman)
    print(vdud < shulman)


if __name__ == "__main__":
    main()
