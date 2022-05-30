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

from abc import ABC, abstractmethod
from typing import Optional


class ProcessorJob(ABC):
    """
    Provides APIs to get or wait for a job's execution result.
    """

    def __init__(self):
        pass

    @abstractmethod
    def wait(self, timeout_ms: Optional[int] = None):
        """
        Waits for at most the given time (milliseconds) for the job termination.

        :param timeout_ms: If it is None, waits for the job termination indefinitely.
        """
        pass
