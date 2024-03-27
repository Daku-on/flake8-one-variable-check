def test_OneLetterVariableChecker() -> None:
    """
    returns OLV001 warning for variable 'x' and not for 'hoge'
    """
    x = 1
    hoge = 'Hello'
    assert (
        x == 1
    )
    assert (
        hoge == 'Hello'
    )

    return None
