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

from googletrans import Translator
from tags import *


class DoxDocsTranslator:
    def __init__(self, origin_doc_file: str = 'DOCUMENTATION.ua.dox', translated_doc_file: str = 'DOCUMENTATION.en.dox', from_lang: str = 'uk', to_lang: str = 'en'):
        self.origin_doc_file: str = origin_doc_file
        self.translated_doc_file: str = translated_doc_file
        self.from_lang: str = from_lang
        self.to_lang: str = to_lang
        self.origin_doc: str = ""
        self.split_origin_docs: list[str] = []
        self.split_translated_docs: list[str] = []
        self.translated_doc: str = ""

    def get_doc(self):
        """A method that retrieves the documentation text from the given file."""
        try:
            input_doc = open(self.origin_doc_file, 'r', encoding='utf-8')
        except FileNotFoundError as error:
            raise FileNotFoundError(f"File {self.origin_doc_file} not found: " + repr(error))
        self.origin_doc = input_doc.read()
        input_doc.close()

    def save_doc(self):
        """A method that saves the finished text to a file."""
        output_doc = open(self.translated_doc_file, 'w', encoding='utf-8')
        output_doc.write(self.translated_doc)
        output_doc.close()

    def optimize_doc(self):
        """A method that brings the style of documentation into a form in which it is better to translate."""
        for key, value in tabs.items():
            self.origin_doc = self.origin_doc.replace(key, value)

    def restoration_doc(self):
        """A method that restores the original style of the documentation text."""
        for key, value in tabs.items():
            self.translated_doc = self.translated_doc.replace(value, key)

    def tagging(self):
        """A method that separates documentation tags."""
        for key, value in dox_tags.items():
            self.origin_doc = self.origin_doc.replace(key, value)

    def untagging(self):
        """A method that restores documentation tags."""
        for key, value in dox_tags.items():
            self.translated_doc = self.translated_doc.replace(value, key)

    def split_doc(self):
        """A method that divides the submitted documentation into parts."""
        self.split_translated_docs = self.split_origin_docs = self.origin_doc.split('$!$ ')

    def join_docs(self):
        """A method that combines translated parts into a single text."""
        self.translated_doc = "$!$ ".join(self.split_translated_docs)

    def translate_doc_segment(self, translatable_docs: str) -> str:
        """A method that translates parts of the documentation that do not exceed 5000 characters."""
        translator = Translator()
        if len(translatable_docs) < 5000:
            translatable_docs = translator.translate(translatable_docs, self.to_lang, self.from_lang).text
        else:
            raise ValueError("len(translatable_docs) in split_origin_docs >= 5000")
        return translatable_docs

    def translate_docs(self):
        """A method that separates parts of the documentation to be translated."""
        count_of_segment_doc = len(self.split_origin_docs)
        print(count_of_segment_doc)
        for index in range(count_of_segment_doc):
            for tags in dox_tags.keys():
                if self.split_origin_docs[index][:-1] == tags and tags not in not_translatable_tags:
                    index += 1
                    try:
                        self.split_translated_docs[index] = self.translate_doc_segment(self.split_origin_docs[index]) + ' '
                        print(f"{index} translated")
                        print(self.split_translated_docs[index] + '\n')
                    except ValueError as error:
                        print(f"{index} not translated : " + repr(error))
                    break

    def start_global_translate(self) -> bool:
        """The main translation algorithm."""
        try:
            self.get_doc()
        except FileNotFoundError as error:
            print(repr(error))
            return False

        self.optimize_doc()
        self.tagging()
        self.split_doc()

        self.translate_docs()

        self.join_docs()
        self.untagging()
        self.restoration_doc()

        self.save_doc()

        return True
