from abc import ABC
from typing import Any, Dict, List


class GeneralService(ABC):
    _dao = None

    def find_all(self) -> List[object]:
        return self._dao.find_all()

    def find_by_id(self, key: Any) -> object:
        return self._dao.find_by_id(key)

    def create(self, obj: object) -> object:
        return self._dao.create(obj)

    def update(self, key: Any, obj: object) -> object:
        return self._dao.update(key, obj)

    def patch(self, key: Any, data: Dict[str, Any]) -> object:
        return self._dao.patch(key, data)

    def delete(self, key: Any) -> bool:
        return self._dao.delete(key)
