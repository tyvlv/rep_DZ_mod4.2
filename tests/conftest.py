import pytest
from classes import Channel, Video, PLVideo


@pytest.fixture
def shulman():
    return Channel('UCL1rJ0ROIw9V1qFeIN0ZTZQ')


@pytest.fixture
def vdud():
    return Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')


@pytest.fixture
def video1():
    return Video('Q0lHb-FCATk')

@pytest.fixture
def video2():
    return PLVideo('W9P_qUnMaFg', 'RDCLAK5uy_kWiJXUNLZM9EyS3GBGznl1ku8_cOos97U')
