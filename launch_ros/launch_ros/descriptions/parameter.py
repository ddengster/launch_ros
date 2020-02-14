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

from typing import Any

from launch import SomeSubstitutionsType

if typing.TYPE_CHECKING:
    from ..parameters_type import SomeParameterValue


class Parameter:
    """Describes a ROS Parameter."""

    def __init__(
        self,
        *,
        name: SomeSubstitutionsType,
        value: SomeParameterValue,
        value_type: Any
    ) -> None:
        self.__name = name
        self.__value = value
        self.__value_type = value_type

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value

    @property
    def value_type(self):
        return self.__type
