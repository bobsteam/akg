# Copyright 2020 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""addn"""
import akg
from akg.topi.cuda.injective_single_kernel import schedule_injective
from akg.ops.math_gpu import addn

@akg.schedule(schedule_injective)
def addn_manual(x):
    """AddN with manual schedule."""
    return addn.addn(x)

def addn_auto(x):
    """AddN with auto poly."""
    return addn.addn(x)
