from googletrans import Translator


def get_doc(name_file: str) -> str:
    input_doc = open(name_file, 'r', encoding='utf-8')
    open_doc = input_doc.read()
    input_doc.close()
    return open_doc


def optimize_origin_doc(doc: str) -> str:
    doc = doc.replace("\n\t\t\t   ", " ")
    doc = doc.replace("\n\t\t   ", " ")
    doc = doc.replace("\n\t   ", " ")
    doc = doc.replace("\n\t\t\t */", " */")
    doc = doc.replace("\n\t\t */", " */")
    doc = doc.replace("\n\t */", " */")
    return doc


def split_doc(doc: str) -> list[str]:
    doc_split = doc.replace("\n\t\t\t/*! ", "\n\t\t/*! ").replace("\n\t/*! ", "\n\t\t/*! ").split(sep="\n\t\t/*! ")
    print(len(doc_split))
    return doc_split


def translate_docs(origin_docs: list[str], from_lang: str, to_lang: str) -> list[str]:
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
    return "\n".join(translated_docs)


def optimize_translated_doc(doc: str) -> str:
    doc = doc.replace(" :: ", "::")
    doc = doc.replace("\\ ", "\n\\")
    doc = doc.replace(" (", "(")
    doc = doc.replace("~ ", "~")
    return doc


def save_doc(doc: str, name_file: str):
    output_doc = open(name_file, 'w', encoding='utf-8')
    output_doc.write(doc)
    output_doc.close()


if __name__ == '__main__':
    ua_doc = get_doc('DOCUMENTATION.ua.txt')
    ua_doc = optimize_origin_doc(ua_doc)
    ua_doc_split = split_doc(ua_doc)
    en_doc_split = translate_docs(ua_doc_split, 'uk', 'en')
    en_doc = join_docs(en_doc_split)
    en_doc = optimize_translated_doc(en_doc)
    save_doc(en_doc, 'DOCUMENTATION.en.txt')
