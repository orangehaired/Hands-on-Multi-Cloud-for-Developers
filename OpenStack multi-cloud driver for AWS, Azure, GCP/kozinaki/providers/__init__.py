# Copyright (c) 2016 CompuNova Inc.
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
from azure.provider import AzureProvider
from aws.provider import AWSProvider
from gcp.provider import GCPProvider
from libcloud_driver.provider import LibCloudProvider


def get_provider_by_name(provider_name):
    """Provider factory method"""
    providers = {
        'AZURE': AzureProvider,
        'AWS': AWSProvider,
        'GCP': GCPProvider,
    }
    if provider_name.startswith('LC_'):
        return LibCloudProvider(provider_name)
    elif provider_name in providers:
        return providers[provider_name]()
    else:
        raise NotImplementedError('Provider {} not implemented in driver. Available providers: {}'
                                  .format(provider_name, providers.keys()))
