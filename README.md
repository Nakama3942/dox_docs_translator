[![template](https://img.shields.io/badge/Repository-template-darkred)](https://github.com/Nakama3942/template_rep)
[![GitHub license](https://img.shields.io/github/license/Nakama3942/Dox-docs_Translator?color=gold&style=flat-square)](https://github.com/Nakama3942/Dox-docs_Translator/blob/main/LICENSE)

<!--[![CHANGELOG](https://img.shields.io/badge/here-CHANGELOG-yellow)](https://github.com/Nakama3942/template_rep/blob/main/CHANGELOG.md)-->
<!--[![CONTRIBUTING](https://img.shields.io/badge/here-CONTRIBUTING-indigo)](https://github.com/Nakama3942/template_rep/blob/main/CONTRIBUTING.md)-->
<!--[![CODE_OF_CONDUCT](https://img.shields.io/badge/here-CODE_OF_CONDUCT-darkgreen)](https://github.com/Nakama3942/template_rep/blob/main/CODE_OF_CONDUCT.md)-->
<!--[![PULL_REQUEST_TEMPLATE](https://img.shields.io/badge/here-PULL_REQUEST_TEMPLATE-orange)](https://github.com/Nakama3942/template_rep/blob/main/.github/PULL_REQUEST_TEMPLATE.md)-->

# Dox-docs_Translator
## Overview
For popular programming languages such as C++, C, C#, Java, Python, etc., Doxygen is used to compile the documentation - software that generates documentation from comments of the established style in the project raws. For the generation of multilingual documentation, storing documentation comments in raw is bad, since in this case it is possible to write documentation in only one language. To solve this problem, Doxygen supports files with the .dox extension. That is, documenting comments can be exported from the code to a .dox file and several copies of it can be made with different translations. Since writing a translation takes a lot of time and it is easier to turn to Google translator - I decided to write this script.

The script opens the documentation file, reads it, breaks it into separate parts and translates the documentation part by part.

<i>At the moment, the script is semi-automatic. After translation, the script does NOT assemble the translated parts back into a whole file. Doxygen tags and names also take part in the translation and the translator breaks them. The text itself is translated correctly. Still possible errors. The product is raw. After translation, you have to insert the translated text into the right place in the original file. But in the future I plan to make a fully automated process of parsing, tagging and translating the documentation.</i>

## Usage
If the <i>googletrans</i> library is not installed or this script does not work, you need to install/reinstall the <i>googletrans</i> library:
```sh
pip install googletrans==4.0.0-rc1
```
Here is an example of using the script from my own experience, as I used it to translate the documentation of my ALGOR project:
```python
if __name__ == '__main__':
    ua_doc = get_doc('DOCUMENTATION.ua.dox')
    ua_doc = optimize_origin_doc(ua_doc)
    ua_doc_split = split_doc(ua_doc)
    en_doc_split = translate_docs(ua_doc_split, 'uk', 'en')
    en_doc = join_docs(en_doc_split)
    en_doc = optimize_translated_doc(en_doc)
    save_doc(en_doc, 'DOCUMENTATION.en.dox')
```
<i>For now this project is a semi-automated simple script and in your own projects you need to rewrite the code in the cloned file, but in the future I will make a full library.</i>

## Authors
<table>
    <tr>
        <td align="center"><a href="https://github.com/Nakama3942"><img src="https://avatars.githubusercontent.com/u/73797846?s=400&u=a9b7688ac521d739825d7003a5bd599aab74cb76&v=4" width="100px;" alt=""/><br /><sub><b>Kalynovsky Valentin</b></sub></a></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
    </tr>
</table>
