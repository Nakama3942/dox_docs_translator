# Changelog
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
