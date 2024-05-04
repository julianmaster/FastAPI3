from src.sentence_prediction import process_sentence, from_str_to_list, tags


def test_process_sentence():
    assert (
        process_sentence("Should i learn html, or css ?")
        == "should i learn html or css "
    )


def test_from_str_to_list():
    assert from_str_to_list("should i learn html or css") == [
        "should i learn html or css"
    ]


def test_tags():
    assert tags(
        [
            [
                0,
                1,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ]
        ]
    ) == ["Other", "android", "iphone"]
