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

dox_tags = {'\\namespace': '$!$ \\namespace $!$',
            '\\brief': '$!$ \\brief $!$',
            '\\details': '$!$ \\details $!$',
            '\\note': '$!$ \\note $!$',
            '\\since': '$!$ \\since $!$',
            '\\author': '$!$ \\author $!$',
            '\\version': '$!$ \\version $!$',
            '\\copyright': '$!$ \\copyright $!$',
            '\\todo': '$!$ \\todo $!$',
            '\\example': '$!$ \\example $!$',
            '\\typedef': '$!$ \\typedef $!$',
            '\\attention': '$!$ \\attention $!$',
            '\\fn': '$!$ \\fn $!$',
            '\\tparam': '$!$ \\tparam $!$',
            '\\param': '$!$ \\param $!$',
            '\\test': '$!$ \\test $!$',
            '\\snippet': '$!$ \\snippet $!$',
            '\\return': '$!$ \\return $!$',
            '\\sa': '$!$ \\sa $!$',
            '\\remark': '$!$ \\remark $!$',
            '\\retval': '$!$ \\retval $!$',
            '\\struct': '$!$ \\struct $!$',
            '\\var': '$!$ \\var $!$',
            '\\throw': '$!$ \\throw $!$',
            '\\interface': '$!$ \\interface $!$',
            '\\warning': '$!$ \\warning $!$',
            '\\class': '$!$ \\class $!$',
            '\\par': '$!$ \\par $!$',
            '\\deprecated': '$!$ \\deprecated $!$',
            '\\code{.cpp}': '$!$ \\code{.cpp} $!$',
            '\\endcode': '$!$ \\endcode $!$',
            '\\enum': '$!$ \\enum $!$',
            '\\bug': '$!$ \\bug $!$',
            '\\image': '$!$ \\image $!$',
            '/*!': '$!$ /*!',
            '\n*/': ' $!$ */ $!$'}

not_translatable_tags = ['\\namespace',
                         '\\since',
                         '\\author',
                         '\\version',
                         '\\copyright',
                         '\\example',
                         '\\typedef',
                         '\\fn',
                         '\\snippet',
                         '\\sa',
                         '\\struct',
                         '\\var',
                         '\\throw',
                         '\\interface',
                         '\\class',
                         '\\code{.cpp}',
                         '\\endcode',
                         '\\enum',
                         '/*!',
                         '\\test',
                         '\\image']

tabs = {"\n\t\t\t   ": "@3 ",
        "\n\t\t   ": "@2 ",
        "\n\t   ": "@1 ",
        "\n   ": "@0 "}
