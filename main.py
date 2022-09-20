# #########################   Dox-docs_Translator   ########################## #
# ---------------------------------------------------------------------------- #
#                                                                              #
# Copyright © 2021-2022 Kalynovsky Valentin. All rights reserved.              #
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

from googletrans import Translator


# Core functional


def get_doc(name_file: str) -> str:
    """A method that retrieves the documentation text from the given file."""
    input_doc = open(name_file, 'r', encoding='utf-8')
    open_doc = input_doc.read()
    input_doc.close()
    return open_doc


def optimize_origin_doc(doc: str) -> str:
    """Brings the style of the documentation to the form in which it is better to translate."""
    doc = doc.replace("\n\t\t\t   ", " ")
    doc = doc.replace("\n\t\t   ", " ")
    doc = doc.replace("\n\t   ", " ")
    doc = doc.replace("\n\t  ", " ")
    doc = doc.replace("\n   ", " ")
    doc = doc.replace("\n  ", " ")
    doc = doc.replace("\n\t\t\t */", "\n*/").replace("\n\t\t */", "\n*/").replace("\n\t\t*/", "\n*/").replace("\n\t */", "\n*/").replace("\n */", "\n*/")
    return doc


def split_doc(doc: str) -> list[str]:
    """Divides the given documentation into parts."""
    doc_split = doc.replace("\n\t\t\t/*! ", "\n\t\t/*! ").replace("\n\t/*! ", "\n\t\t/*! ").replace("\n/*! ", "\n\t\t/*! ").split(sep="\n\t\t/*! ")
    print(len(doc_split))
    return doc_split


def translate_docs(origin_docs: list[str], from_lang: str, to_lang: str) -> list[str]:
    """Translates parts of the documentation that are less than 5000 characters."""
    translator = Translator()
    count = 0
    translate_docs: list[str] = []
    for item in origin_docs:
        count += 1
        if len(item) < 5000:
            translate_docs.append(translator.translate(item, src=from_lang, dest=to_lang).text)
            print(f"{count} translated")
        else:
            print(f"{count} not translated : len(item) in ua_doc_split >= 5000")
    return translate_docs


def join_docs(translated_docs: list[str]) -> str:
    """Combines the translated parts into a single text."""
    return "".join(translated_docs)


def optimize_translated_doc(doc: str) -> str:
    """Slightly transforms the appearance of the text."""
    doc = doc.replace(" :: ", "::")
    doc = doc.replace("\\ ", "\n\\")
    doc = doc.replace(" (", "(")
    doc = doc.replace("~ ", "~")
    return doc


def save_doc(doc: str, name_file: str):
    """Saves the finished text to a file."""
    output_doc = open(name_file, 'w', encoding='utf-8')
    output_doc.write(doc)
    output_doc.close()


# New functional


dox_tags = {'\\namespace': '$!$ \\namespace $!$', '\\brief': '$!$ \\brief $!$', '\\details': '$!$ \\details $!$', '\\note': '$!$ \\note $!$', '\\since': '$!$ \\since $!$', '\\author': '$!$ \\author $!$', '\\version': '$!$ \\version $!$', '\\copyright': '$!$ \\copyright $!$', '\\todo': '$!$ \\todo $!$', '\\example': '$!$ \\example $!$', '\\typedef': '$!$ \\typedef $!$', '\\attention': '$!$ \\attention $!$', '\\fn': '$!$ \\fn $!$', '\\tparam': '$!$ \\tparam $!$', '\\param': '$!$ \\param $!$', '\\test ': '', '\\snippet': '$!$ \\snippet $!$', '\\return': '$!$ \\return $!$', '\\sa': '$!$ \\sa $!$', '\\remark': '$!$ \\remark $!$', '\\retval': '$!$ \\retval $!$', '\\struct': '$!$ \\struct $!$', '\\var': '$!$ \\var $!$', '\\throw': '$!$ \\throw $!$', '\\interface': '$!$ \\interface $!$', '\\warning': '$!$ \\warning $!$', '\\class': '$!$ \\class $!$', '\\par': '$!$ \\par $!$', '\\deprecated': '$!$ \\deprecated $!$', '\\code{.cpp}': '$!$ \\code{.cpp} $!$', '\\endcode': '$!$ \\endcode $!$', '\\enum': '$!$ \\enum $!$', '\\bug': '$!$ \\bug $!$', '/*!': '$!$ /*! $!$', '\n*/': ' $!$ */ $!$'}


def test_tags(doc: str) -> str:
    for item in dox_tags.keys():
        doc = doc.replace(item, dox_tags[item])
    return doc


# Script


if __name__ == '__main__':
    ua_doc = get_doc('DOCUMENTATION.ua.dox')
    ua_doc = optimize_origin_doc(ua_doc)

    ua_doc = test_tags(ua_doc)

    # ua_doc_split = split_doc(ua_doc)
    # ua_doc = join_docs(ua_doc_split)

    save_doc(ua_doc, 'DOCUMENTATION.test.dox')


# if __name__ == '__main__':
#     ua_doc = get_doc('DOCUMENTATION.ua.dox')
#     ua_doc = optimize_origin_doc(ua_doc)
#     ua_doc_split = split_doc(ua_doc)
#     en_doc_split = translate_docs(ua_doc_split, 'uk', 'en')
#     en_doc = join_docs(en_doc_split)
#     en_doc = optimize_translated_doc(en_doc)
#     save_doc(en_doc, 'DOCUMENTATION.en.dox')
