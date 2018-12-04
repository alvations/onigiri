# Copyright 2016 Rakuten Inc.
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

from distutils.core import setup

setup(
    name='onigiri',
    version='0.0.2',
    packages=['onigiri'],
    description='Unofficial RIT Translate',
    long_description='Unofficial Python API for Rakuten Institute of Technology Translate',
    url = '',
    license="Apache v2.0",
    install_requires = ['requests', 'six']
)
