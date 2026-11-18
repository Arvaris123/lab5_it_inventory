from abc import ABC
from typing import Any, Dict, List

from sqlalchemy import inspect

from my_project import db


class GeneralDAO(ABC):
    _domain_type = None

    @property
    def _session(self):
        return db.session

    def find_all(self) -> List[object]:
        primary_key = inspect(self._domain_type).primary_key
        return self._session.query(self._domain_type).order_by(*primary_key).all()

    def find_by_id(self, key: Any) -> object:
        return self._session.get(self._domain_type, key)

    def create(self, obj: object) -> object:
        self._session.add(obj)
        self._session.commit()
        return obj

    def update(self, key: Any, new_obj: object) -> object:
        obj = self.find_by_id(key)
        if obj is None:
            return None
        for column in inspect(self._domain_type).columns:
            if not column.primary_key:
                setattr(obj, column.key, getattr(new_obj, column.key))
        self._session.commit()
        return obj

    def patch(self, key: Any, data: Dict[str, Any]) -> object:
        obj = self.find_by_id(key)
        if obj is None:
            return None
        columns = {c.key for c in inspect(self._domain_type).columns if not c.primary_key}
        for field, value in data.items():
            if field in columns:
                setattr(obj, field, value)
        self._session.commit()
        return obj

    def delete(self, key: Any) -> bool:
        obj = self.find_by_id(key)
        if obj is None:
            return False
        self._session.delete(obj)
        self._session.commit()
        return True
