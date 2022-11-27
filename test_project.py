import project

def test_get_athlete(monkeypatch):
    inputs = iter(["John", "Denver", 200.0, 100.0])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    athlete = project.get_athlete()
    assert athlete.first_name == "John"
    assert athlete.last_name == "Denver"
    assert athlete.pre_practice_weight == 200.0
    assert athlete.post_practice_weight == 100.0
    assert athlete.weight_change_absolute == 100.0
    assert athlete.relative_weight_change == 50


def test_get_weights(monkeypatch):
    inputs = iter([200, 100])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    test1 = project.get_weights()
    assert test1 == (200.0, 100.0)


def test_get_weight_change():
    absolute, relative = project.get_weight_change(pre=200, post=100)
    assert absolute == 100
    assert relative == 50


