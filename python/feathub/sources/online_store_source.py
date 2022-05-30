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

from typing import List

from feathub.sources.source import Source


class OnlineStoreSource(Source):
    """
    A sink corresponding to a table in an online feature store.
    """

    def __init__(
        self,
        name: str,
        keys: List[str],
        store_type: str,
        table_name: str,
    ):
        """
        :param name: The name that uniquely identifies this source in a registry.
        :param keys: The keys of the table in the online feature store.
        :param table_name: The name of the table in the online feature store.
        :param store_type: A string that uniquely identifies a store class.
        """
        super().__init__(
            name=name,
            keys=keys,
            timestamp_field=None,
            timestamp_format="epoch",
        )
        self.store_type = store_type
        self.table_name = table_name

    def to_json(self):
        return {
            "type": "OnlineStoreSource",
            "name": self.name,
            "keys": self.keys,
            "store_type": self.store_type,
            "table_name": self.table_name,
        }
