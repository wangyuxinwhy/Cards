# -*- coding: utf-8 -*-
from pathlib import Path
from typing import TYPE_CHECKING

import tinydb


class DB:
    def __init__(self, db_path: Path, db_file_prefix: str):
        self._db = tinydb.TinyDB(db_path / f"{db_file_prefix}.json", create_dirs=True)

    def create(self, item: dict):
        id_ = self._db.insert(item)
        return id_

    def read(self, id_: int):
        item = self._db.get(doc_id=id_)
        return item

    def update(self, id_: int, update_fields: dict) -> None:
        changes = {k: v for k, v in update_fields.items() if v is not None}
        self._db.update(changes, doc_ids=[id_])

    def delete(self, id_: int) -> None:
        self._db.remove(doc_ids=[id_])

    def delete_all(self) -> None:
        self._db.truncate()

    def count(self) -> int:
        return len(self._db)

    def close(self):
        self._db.close()
