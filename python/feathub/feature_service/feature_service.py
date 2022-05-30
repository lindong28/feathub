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

from __future__ import annotations

import pandas as pd
from abc import ABC, abstractmethod
from typing import Optional, List, Union, Dict

from feathub.online_stores.online_store import OnlineStore
from feathub.registries.registry import Registry
from feathub.feature_views.on_demand_feature_view import OnDemandFeatureView


class FeatureService(ABC):
    """
    A FeatureService implements APIs to compute on-demand feature view, which involves
    joining online request with features from tables in online stores, and performing
    per-row transformation after online request arrives.

    Unlike Processor, which computes features with offline or nearline latency,
    FeatureService computes features with online latency after online request arrives.
    """

    def __init__(self):
        pass

    @abstractmethod
    def get_online_features(
        self,
        request_df: pd.DataFrame,
        feature_view: Union[str, OnDemandFeatureView],
        feature_fields: Optional[List[str]] = None,
    ) -> pd.DataFrame:
        """
        Returns a DataFrame obtained by applying the given OnDemandFeatureView on the
        given input_data.

        :param request_df: A DataFrame where each row contains the keys of this table.
        :param feature_view: Describes the features to be included in the output. If it
                             is a string, it refers to the name of a OnDemandFeatureView
                             in the entity registry.
        :param feature_fields: Optional. The names of fields of values that should be
                               included in the output DataFrame. If it is None, all
                               fields of the specified table should be outputted.
        :return: A DataFrame obtained according to the specified criteria.
        """
        pass

    @staticmethod
    def instantiate(
        service_type: str,
        config: Dict,
        stores: Dict[str, OnlineStore],
        registry: Registry,
    ) -> FeatureService:
        """
        Instantiates a feature service using the given configuration and the store
        instances.
        """
        from feathub.feature_service.local_feature_service import LocalFeatureService

        if service_type == LocalFeatureService.SERVICE_TYPE:
            return LocalFeatureService(config=config, stores=stores, registry=registry)

        raise RuntimeError(
            f"Failed to instantiate feature service with config={config}"
        )
