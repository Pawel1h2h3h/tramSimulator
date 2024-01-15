import pytest
from PySide6.QtCore import QPointF
from data_structure.tram_stop import TramStop  

@pytest.fixture
def tram_stop():
    return TramStop(id=1, position=(100, 200))

def test_initialization(tram_stop):
    assert tram_stop.id() == 1
    assert tram_stop.pos() == QPointF(100, 200)


def test_bounding_rect(tram_stop):
    rect = tram_stop.boundingRect()
    assert rect.width() == 20
    assert rect.height() == 10

def test_name_methods(tram_stop):
    tram_stop.set_name("New Stop")
    assert tram_stop.name() == "New Stop"

def test_id_method(tram_stop):
    assert tram_stop.id() == 1

def test_info_method(tram_stop):
    info = tram_stop.info()
    expected_info = f"Stop 1 at {tram_stop.pos()}"
    assert info == expected_info

def test_to_json(tram_stop):
    json_data = tram_stop.to_json()
    assert json_data == {"id": 1, "position": (100, 200)}



