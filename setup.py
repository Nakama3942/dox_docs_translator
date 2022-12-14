# #########################   Dox-docs_Translator   ########################## #
# ---------------------------------------------------------------------------- #
#                                                                              #
# Copyright © 2022 Kalynovsky Valentin. All rights reserved.                   #
#                                                                              #
# Licensed under the Apache License, Version 2.0 (the "License");              #
# you may not use this file except in compliance with the License.             #
# You may obtain a copy of the License at                                      #
#                                                                              #
#     http://www.apache.org/licenses/LICENSE-2.0                               #
#                                                                              #
# Unless required by applicable law or agreed to in writing, software          #
# distributed under the License is distributed on an "AS IS" BASIS,            #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.     #
# See the License for the specific language governing permissions and          #
# limitations under the License.                                               #
#                                                                              #
# ---------------------------------------------------------------------------- #
# ############################################################################ #

from setuptools import setup

with open("README.md", "r", encoding='utf-8') as readme_file:
    readme = readme_file.read()

setup(
    name="dox_docs_translator",
    version="0.1.1",

    author="Kalynovsky 'Nakama3942' Valentin",
    author_email="nakama3942@gmail.com",

    description="Translator of custom Doxygen-documentation",
    long_description=readme,
    long_description_content_type="text/markdown",

    url="https://github.com/Nakama3942/dox_docs_translator",

    license="Apache License, Version 2.0, see LICENSE file",

    packages=['dox_docs_translator'],
    install_requires=['googletrans==4.0.0-rc1'],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
    ]
)
