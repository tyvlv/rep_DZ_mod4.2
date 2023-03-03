def test_str(shulman):
    assert shulman.__str__() == "Youtube-канал: Екатерина Шульман"


def test_add(shulman, vdud):
    assert shulman.__add__(vdud) == 11380000


def test_gt(shulman, vdud):
    assert shulman.__gt__(vdud) is False


def test_lt(shulman, vdud):
    assert shulman.__lt__(vdud) is True


def test_str_video(video1):
    assert video1.__str__() == "Выполняем тестовое задание на Junior Python разработчика с зарплатой 70000р | PDF в MP3"


def test_str_plvideo(video2):
    assert video2.__str__() == "Dynoro & Gigi D’Agostino - In My Mind (Huge Dance Hits )"
