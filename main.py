from classes import Channel


def main():
    shulman_channel = Channel('UCL1rJ0ROIw9V1qFeIN0ZTZQ')  # Екатерина Шульман
    vdud_channel = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')  # вДудь

    shulman_channel.print_info()
    vdud_channel.print_info()


if __name__ == "__main__":
    main()
