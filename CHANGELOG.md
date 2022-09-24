# Changelog
<!--
Copyright © 2022 Kalynovsky Valentin. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->
<!--
## vX.X.X (DATE)

#### Bug Fixes:
- [# XXX](https : / / github . com / XXX) DESCRIPTION

#### Invalid Fixed:
- [# XXX](https : / / github . com / XXX) DESCRIPTION

#### Documenting:
- [# XXX](https : / / github . com / XXX) DESCRIPTION

#### Duplicating:
- [# XXX](https : / / github . com / XXX) DESCRIPTION

#### Enhancements:
- [# XXX](https : / / github . com / XXX) DESCRIPTION

---
-->
## v0.1.0 (24.09.2022)

#### Documenting:
- Documented new functionality
- Updated the README.md

#### Enhancements:
- Rewritten functionality:
	- def get_doc()
	- def optimize_origin_doc()
	- def optimize_translated_doc()
	- def split_doc()
	- def join_docs()
	- def translate_docs(translatable_docs: str) -> str
- Renamed:
	- optimize_origin_doc() on optimize_doc()
	- optimize_translated_doc() on restoration_doc()
	- translate_docs() on translate_doc_segment()
- Implemented new functionality:
	- def tagging()
	- def untagging()
	- def translate_docs()
	- def start_global_translate() -> bool
- Combined all functionality into a single class - DoxDocsTranslator

---

## v0.0.1 (18.09.2022)

#### Release
- A script has been released that has the basic functionality of bringing the documentation to the translation form, and the functionality of translating the documentation itself. The script is semi-automatic, as it does not collect the given translated documentation into its original form. List of implemented functions:
	- def get_doc(name_file: str) -> str
	- optimize_origin_doc(doc: str) -> str
	- def split_doc(doc: str) -> list[str]
	- def translate_docs(origin_docs: list[str], from_lang: str, to_lang: str) -> list[str]
	- def join_docs(translated_docs: list[str]) -> str
	- def optimize_translated_doc(doc: str) -> str
	- def save_doc(doc: str, name_file: str)
