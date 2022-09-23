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
from tags import *


def get_doc(name_file_doc: str) -> str:
    """A method that retrieves the documentation text from the given file."""
    try:
        input_doc = open(name_file_doc, 'r', encoding='utf-8')
    except FileNotFoundError as error:
        raise FileNotFoundError(f"File {name_file_doc} not found: " + repr(error))
    open_doc = input_doc.read()
    input_doc.close()
    return open_doc


def save_doc(doc: str, name_file_doc: str):
    """A method that saves the finished text to a file."""
    output_doc = open(name_file_doc, 'w', encoding='utf-8')
    output_doc.write(doc)
    output_doc.close()


def optimize_doc(doc: str) -> str:
    """A method that brings the style of documentation into a form in which it is better to translate."""
    for key, value in tabs.items():
        doc = doc.replace(key, value)
    return doc


def restoration_doc(doc: str) -> str:
    """A method that restores the original style of the documentation text."""
    for key, value in tabs.items():
        doc = doc.replace(value, key)
    return doc


def tagging(doc: str) -> str:
    """A method that separates documentation tags."""
    for key, value in dox_tags.items():
        doc = doc.replace(key, value)
    return doc


def untagging(doc: str) -> str:
    """A method that restores documentation tags."""
    for key, value in dox_tags.items():
        doc = doc.replace(value, key)
    return doc


def split_doc(doc: str) -> list[str]:
    """A method that divides the submitted documentation into parts."""
    docs_split = doc.split('$!$ ')
    return docs_split


def join_docs(translated_docs: list[str]) -> str:
    """A method that combines translated parts into a single text."""
    return "$!$ ".join(translated_docs)


def translate_doc_segment(translatable_docs: str, from_lang: str, to_lang: str) -> str:
    """A method that translates parts of the documentation that do not exceed 5000 characters."""
    translator = Translator()
    if len(translatable_docs) < 5000:
        translatable_docs = translator.translate(translatable_docs, src=from_lang, dest=to_lang).text
    else:
        raise ValueError("len(item) in ua_doc_split >= 5000")
    return translatable_docs


def translate_docs(docs: list[str], from_lang: str, to_lang: str) -> list[str]:
    """A method that separates parts of the documentation to be translated."""
    print(len(docs))
    for index in range(len(docs)):
        for tags in dox_tags.keys():
            if docs[index][:-1] == tags and tags not in not_translatable_tags:
                index += 1
                try:
                    docs[index] = translate_doc_segment(docs[index], from_lang, to_lang) + ' '
                    print(f"{index} translated")
                    print(docs[index] + '\n')
                except ValueError as error:
                    print(f"{index} not translated : " + repr(error))
                break
    return docs


def main(origin_doc_file: str = 'DOCUMENTATION.ua.dox', translated_doc_file: str = 'DOCUMENTATION.en.dox', from_lang: str = 'uk', to_lang: str = 'en') -> bool:
    """The main translation algorithm."""
    try:
        ua_doc = get_doc(origin_doc_file)
    except FileNotFoundError as error:
        print(repr(error))
        return False

    ua_doc = optimize_doc(ua_doc)
    ua_doc = tagging(ua_doc)
    ua_doc_split = split_doc(ua_doc)

    en_doc_split = translate_docs(ua_doc_split, from_lang, to_lang)

    en_doc = join_docs(en_doc_split)
    en_doc = untagging(en_doc)
    en_doc = restoration_doc(en_doc)

    save_doc(en_doc, translated_doc_file)

    return True
