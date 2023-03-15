from names import generate_name


def test_length():
    assert len(generate_name(15, 15)) == 15


def test_randomness():
    assert generate_name() != generate_name()
