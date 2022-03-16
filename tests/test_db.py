# -*- coding: utf-8 -*-

from cards import DB


def test_db(tmp_path):
    db = DB(tmp_path, "test")
    item1 = {"name": "tom", "age": 12}
    item2 = {"name": "alice", "age": 13}

    item1_id = db.create(item1)
    item2_id = db.create(item2)

    assert item1_id != item2_id
    assert db.count() == 2
    assert db.read(item1_id) == item1

    db.update(item1_id, {"name": "tom", "age": 13})
    assert db.read(item1_id) == {"name": "tom", "age": 13}

    db.delete(item1_id)
    assert db.read(item1_id) is None
    assert db.count() == 1

    db.delete_all()
    assert db.count() == 0

    db.close()
