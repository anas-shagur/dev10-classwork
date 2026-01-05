# 1. Read the surround_with_tag docstring.
# 2. Complete the surround_with_tag function. You're only allowed to confirm it's working by running
#    the accompanying test in test_exercise_02.TestExercise02.
#    $ python -m unittest tests.test_exercise_02
# 3. The test is incomplete. It doesn't account for all scenarios. Complete the test to insure
#    surround_with_tag is 100% correct.


def surround_with_tag(text, tag_name):
    """
    Given two strings: some text and a tag name, return a string that embeds the text in a pseudo-HTML tag.
    Examples:
    "abc", "boom" -> "<boom>abc</boom>"
    "Cats are mean.", "fact" -> "<fact>Cats are mean.</fact>"
    "this is just text", "" -> "this is just text"
    None, "span" -> "<span></span>"
    "splendid", None -> splendid

    Args:
        text (str): value to be surrounded by an HTML tag
        tag_name (str): the HTML tag name
    Returns:
        str: string in the form: <tag_name>text</tag_name>
    """
    return None
