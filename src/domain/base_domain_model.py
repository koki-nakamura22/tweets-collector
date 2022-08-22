from dataclasses import dataclass
from typing import List


class BaseDomainModel:
    def values_as_list(self) -> List:
        member_var_names = [attr for attr in dir(self) if not callable(getattr(self,attr)) and not attr.startswith("__")]
        val_list = list()
        for member_var_name in member_var_names:
            val_list.append(getattr(self, member_var_name))
        return val_list
