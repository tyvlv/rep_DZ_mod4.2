def test_str(shulman):
    assert shulman.__str__() == "Youtube-канал: Екатерина Шульман"


def test_add(shulman, vdud):
    assert shulman.__add__(vdud) == 11380000


def test_gt(shulman, vdud):
    assert shulman.__gt__(vdud) is False


def test_lt(shulman, vdud):
    assert shulman.__lt__(vdud) is True
