from abc import ABC
from http import HTTPStatus
from typing import Any, Dict, List

from flask import abort


class GeneralController(ABC):
    _service = None

    @staticmethod
    def _to_dto_list(objects) -> List[Dict[str, Any]]:
        return [obj.put_into_dto() for obj in objects]

    @staticmethod
    def _check_found(result):
        if result is None:
            abort(HTTPStatus.NOT_FOUND)
        return result

    def find_all(self) -> List[Dict[str, Any]]:
        return self._to_dto_list(self._service.find_all())

    def find_by_id(self, key: Any) -> Dict[str, Any]:
        return self._check_found(self._service.find_by_id(key)).put_into_dto()

    def create(self, obj: object) -> Dict[str, Any]:
        return self._service.create(obj).put_into_dto()

    def update(self, key: Any, obj: object) -> Dict[str, Any]:
        return self._check_found(self._service.update(key, obj)).put_into_dto()

    def patch(self, key: Any, data: Dict[str, Any]) -> Dict[str, Any]:
        return self._check_found(self._service.patch(key, data)).put_into_dto()

    def delete(self, key: Any) -> None:
        if not self._service.delete(key):
            abort(HTTPStatus.NOT_FOUND)
