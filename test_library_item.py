from library_item import LibraryItem

def test_library_01():
    # Test case with empty name
    try: 
        video_info = LibraryItem("", 'Robert Kiyosaki', 5)
        assert False
    except ValueError as e:
        str(e) == 'Name cannot be empty!'

def test_library_02():
    # Test case with valid name 
    video_info = LibraryItem('Rich Father Poor Father', 'Robert Kiyosaki', 5)
    video_info.info()
    assert 'Rich Father Poor Father - Robert Kiyosaki *****\n'

def test_library_03():
    # Test case with name is a number type
    try:
        video_info = LibraryItem(1, 'Robert Kiyosaki', 5)
        assert False
    except ValueError as e:
        str(e) == 'Name must be letters and cannot be numbers!'

def test_library_04():
    # Test case with name is a string but contain number 
    try:
        video_info = LibraryItem('123', 'Robert Kiyosaki', 5)
        assert False
    except ValueError as e:
        str(e) == 'Name must be letters and cannot be numbers!'

def test_library_05():
    # Test case with name is a special character
    try:
        video_info = LibraryItem('@@$$', 'Robert Kiyosaki', 5)
        assert False
    except ValueError as e:
        str(e) == 'Name cannot be special character!'

def test_library_06():
    # Test case with empty Director
    try:
        video_info = LibraryItem('Rich Dad Poor Dad', '', 5)
        assert False
    except ValueError as e:
        assert str(e) == 'Director cannot be empty!'

def test_library_07():
    # Test case with normal Director
    video_info = LibraryItem('Rich Dad Poor Dad', 'Robert Kiyosaki', 5) 
    video_info.info()
    assert 'Rich Dad Poor Dad - Robert Kiyosaki *****\n'
    

def test_library_08():
    # Test case with number Director
    try:
        video_info = LibraryItem('Rich Dad Poor Dad', 12345, 5)
        assert False
    except ValueError as e:
        assert str(e) == 'Director must be letters and cannot be numbers!'

def test_library_09():
    # Test case with string type but include number 
    try:
        video_info = LibraryItem('Rich Dad Poor Dad', '12345', 5)
        assert False
    except ValueError as e:
        assert str(e) == 'Director must be letters and cannot be numbers!'

def test_library_10():
    # Test case with special characters Director
    try:
        video_info = LibraryItem('Rich Dad Poor Dad', '@@$$%%', 5)
        assert False
    except ValueError as e:
        assert str(e) == 'Director cannot be special character!'

def test_library_11():
    # Test case with default rating
        video_info = LibraryItem('Rich Dad Poor Dad', 'Robert Kiyosaki', 0)
        assert video_info.rating == 0

def test_library_12():
    # Test case with normal Rating
    video_info = LibraryItem('Rich Dad Poor Dad', 'Robert Kiyosaki', 4)
    assert video_info.rating == 4

def test_library_13():
    # Test case with negative-number Rating
    try:
        video_info = LibraryItem('Rich Dad Poor Dad', 'Robert Kiyosaki', -1)
        assert False
    except ValueError as e:
        assert str(e) == 'Rating cannot be negative!'

def test_library_14():
    # Test case with rating > 5 (Rating maximum equal 5)
    try:
        video_info = LibraryItem('Rich Dad Poor Dad', 'Robert Kiyosaki', 6)
        assert False
    except ValueError as e:
        assert str(e) == 'Rating must lower than 6!'