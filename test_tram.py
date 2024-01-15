import pytest
from PySide6.QtCore import QPointF
from data_structure.tram_stop import TramStop

@pytest.fixture
def tram_stop():
    return TramStop(id=1, position=(100, 200))

def test_initialization(tram_stop):
    assert tram_stop.id() == 1
    assert tram_stop.pos() == QPointF(100, 200)
    assert tram_stop.line() is None


def test_bounding_rect(tram_stop):
    rect = tram_stop.boundingRect()
    assert rect.width() == 20
    assert rect.height() == 10

def test_name_methods(tram_stop):
    tram_stop.set_name("New Name")
    assert tram_stop.name() == "New Name"

def test_id_method(tram_stop):
    assert tram_stop.id() == 1


def test_info_str_methods(tram_stop):
    info = tram_stop.info()
    assert str(tram_stop) in info

def test_to_json(tram_stop):
    json_representation = tram_stop.to_json()
    assert json_representation['id'] == 1
    assert json_representation['position'] == (100, 200)

