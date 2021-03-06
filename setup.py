#!/usr/bin/env python
# -*- coding:utf8 -*-

#      Copyright 2017, Schuberg Philis BV
#
#      Licensed to the Apache Software Foundation (ASF) under one
#      or more contributor license agreements.  See the NOTICE file
#      distributed with this work for additional information
#      regarding copyright ownership.  The ASF licenses this file
#      to you under the Apache License, Version 2.0 (the
#      "License"); you may not use this file except in compliance
#      with the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#      Unless required by applicable law or agreed to in writing,
#      software distributed under the License is distributed on an
#      "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#      KIND, either express or implied.  See the License for the
#      specific language governing permissions and limitations
#      under the License.

#      Romero Galiza Jr. - rgaliza@schubergphilis.com

from setuptools import setup, find_packages

base_url = 'https://github.com/romerojunior/cloudian-api'
version_tag = '0.2.4'

setup(
    name='cloudianapi',
    version=version_tag,
    description='Non-official Cloudian (TM) REST Admin API Client',
    author='Romero Galiza Jr',
    license='Apache License Version 2.0',
    author_email='rgaliza@schubergphilis.com',
    url=base_url,
    download_url=base_url + '/archive/' + version_tag + '.tar.gz',
    packages=find_packages(),
    keywords=['cloudian', 'api-client'],
    platforms=['Any']
)
