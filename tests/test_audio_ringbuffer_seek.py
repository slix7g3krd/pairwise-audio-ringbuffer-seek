import pytest
import math
from media import audio_ringbuffer_seek as mod

CASES = [
    ("advance", 'm.advance(7, 5, 10) == 2'),
    ("readable", 'm.readable(8, 3, 10) == 5'),
    ("flag", 'm.seek_flag(1, 10) is True'),
    ("decoder", 'm.reset_decoder({"a": 1}) == {}'),
    ("version", 'm.version_key("seek", 2) == "seek:2"'),
    ("frame", 'm.frame_bytes(2, 2) == 4'),
    ("clock", 'm.reset_clock(5) == 5'),
    ("pad", 'm.pad_tail([1], 2) == [1, 0, 0]'),
    ("silence", 'm.is_silence((0, 0)) is True'),
    ("copy", 'm.copy_frame((1, 2, 3), 2) == (1, 2)'),
    ("capacity", 'm.capacity(4, 2) == 8'),
    ("wrap", 'm.wrap_dist(8, 3, 10) == 5'),
    ("ptr", 'm.valid_ptr(10, 10) is False'),
    ("target", 'm.seek_target(15, 10) == 10'),
    ("key", 'm.buffer_key(1) == "buf:1"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
