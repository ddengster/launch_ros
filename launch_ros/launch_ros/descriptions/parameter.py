# Copyright 2019 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module for a description of a Parameter."""

import collections.abc

from typing import Any
from typing import Optional

from launch import SomeSubstitutionsType
from launch import Substitution
from launch import LaunchContext
from launch.utilities import normalize_to_list_of_substitutions
from launch.utilities import perform_substitutions

if typing.TYPE_CHECKING:
    from ..parameters_type import SomeParameterValue


class Parameter:
    """Describes a ROS Parameter."""

    def __init__(
        self,
        *,
        name: SomeSubstitutionsType,
        value: SomeParameterValue,
        value_type: Any = None
    ) -> None:
        self.__name = normalize_to_list_of_substitutions(name)
        self.__value = value
        self.__value_type = value_type
        self.__evaluated_parameter_rule: Optional[Text] = None

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value

    @property
    def value_type(self):
        return self.__type

    def evaluate(self, context: LaunchContext):
        name = perform_substitutions(context, self.name)
        value_is_substitution = (
            isinstance(value, Substitution) or
            (
                isinstance(collections.abc.Iterable) and
                len(value) > 0 and
                isinstance(value[0], Substitution)
            )
        )
        if value_is_substitution:
            value = perform_substitutions(
                context,
                normalize_to_list_of_substitutions(value))
            
