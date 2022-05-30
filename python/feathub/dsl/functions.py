# Copyright 2022 The Feathub Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import feathub.common.utils as utils


def _cast_float(value) -> float:
    return float(value)


def _cast_int(value) -> int:
    return int(value)


# TODO: add Flink's System (Built-in) Functions
_FUNCTIONS = {
    "unix_timestamp": utils.to_unix_timestamp,
    "cast_float": _cast_float,
    "cast_int": _cast_int,
}


def get_predefined_function(name: str):
    return _FUNCTIONS.get(name, None)
