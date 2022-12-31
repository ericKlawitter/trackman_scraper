# CSV parses numbers as strings, so this is preferred over casting everywhere
def assertEqualStrings(arg1, arg2):
    assert str(arg1) == str(arg2)
