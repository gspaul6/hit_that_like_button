import pytest
from likeButton.hit_that_like_button import LikeState, hit_many

def test_empty_hit():
    assert hit_many(LikeState.empty, '') is LikeState.empty


def test_single_hit():
    assert hit_many(LikeState.empty, 'l') is LikeState.liked
    assert hit_many(LikeState.empty, 'd') is LikeState.disliked


@pytest.mark.parametrize("test_input,expected", [
    ('ll', LikeState.empty),
    ('dd', LikeState.empty),
    ('ld', LikeState.disliked),
    ('dl', LikeState.liked),
    ('ldd', LikeState.empty),
    ('lldd', LikeState.empty),
    ('ddl', LikeState.liked),
])
def test_multi_hit(test_input, expected):
    assert hit_many(LikeState.empty, test_input) is expected


@pytest.mark.skip(reason="regexes not supported yet")# for skipping a test
def test_regex_hit():
    assert hit_many(LikeState.empty, '[ld]*ddl') is LikeState.liked


@pytest.mark.xfail #expected fail, caution not to be used if you are expecting an exception
def test_divide_by_zero():
    assert 1 / 0 == 1


def test_invalid_hit():
    with pytest.raises(ValueError):
        hit_many(LikeState.empty, 'x')


@pytest.mark.xfail
def test_db_hit(db_conn):
    db_conn.read_hits()
    assert ...


def test_print(capture_stdout):
    print("hello")
    assert capture_stdout["stdout"] == "hello\n"