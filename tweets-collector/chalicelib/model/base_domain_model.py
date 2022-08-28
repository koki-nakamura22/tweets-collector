from abc import ABC, abstractmethod
import dataclasses
from dataclasses import dataclass
from typing import List


class BaseDomainModel(ABC):
    def values_as_list(self) -> List:
        # member_var_names = [attr for attr in dir(self) if not callable(
        #     getattr(self, attr)) and not attr.startswith("__") and attr != '_abc_impl']
        # val_list = list()
        # for member_var_name in member_var_names:
        #     val_list.append(getattr(self, member_var_name))
        # return val_list

        val_list = list()
        members = vars(self)
        for k in members:
            val_list.append(members[k])
        return val_list

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)
