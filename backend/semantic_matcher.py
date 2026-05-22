synonyms = {

    "ml": "machine learning",

    "ai": "artificial intelligence",

    "js": "javascript",

    "py": "python"

}


def semantic_matching(text):

    text = text.lower()

    for short_form, full_form in synonyms.items():

        text = text.replace(
            short_form,
            full_form
        )

    return text