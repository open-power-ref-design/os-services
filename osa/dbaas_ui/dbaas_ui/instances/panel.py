# Copyright 2017, IBM US, Inc.
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
from django.utils.translation import ugettext_lazy as _
import horizon
import logging

from openstack_dashboard.api import keystone

LOG = logging.getLogger(__name__)


class Instances(horizon.Panel):
    name = _("Instances")
    slug = 'instances'

    def can_access(self, context):

        if keystone.is_multi_domain_enabled() \
                and not keystone.is_domain_admin(context['request']):
            return False
        return super(Instances, self).can_access(context)

    @staticmethod
    def can_register():
        return keystone.VERSIONS.active >= 3
