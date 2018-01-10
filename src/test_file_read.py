"""."""
from file_read import create_file_dict


def test_dict():
    """."""
    res = create_file_dict()
    res = res.keys()
    assert sorted(res) == [
        'LICENSE', 'README.md', 'coverage', 'coveragerc', 'disemvowel.pyc',
        'find_divisors.pyc', 'forbes_listing.pyc', 'friend_foe.pyc',
        'gitignore', 'grasshopper.pyc', 'hq9.pyc', 'jaden_case.pyc',
        'mult_3_5.pyc', 'multiply.pyc', 'setup.py', 'smallest_int.pyc',
        'src/calc_forbes.py', 'src/disemvowel.py', 'src/file_read.py',
        'src/find_divisors.py', 'src/forbes_listing.py', 'src/friend_foe.py',
        'src/grasshopper.py', 'src/hq9.py', 'src/jaden_case.py',
        'src/mult_3_5.py', 'src/multiply.py', 'src/proper_parenthetics.py',
        'src/rotate_matrix.py', 'src/smallest_int.py', 'src/sort_cards.py',
        'src/string_increment.py', 'src/string_pyramid.py', 'src/sum_terms.py',
        'src/test_disemvowel.py', 'src/test_f_div.py', 'src/test_file_read.py',
        'src/test_forbes.py', 'src/test_friend_foe.py',
        'src/test_grasshopper.py', 'src/test_hq9.py', 'src/test_jaden_case.py',
        'src/test_mult_3_5.py', 'src/test_multiply.py', 'src/test_parens.py',
        'src/test_rotate_matrix.py', 'src/test_smallest_int.py',
        'src/test_sort_cards.py', 'src/test_string_increment.py',
        'src/test_string_pyramid.py', 'src/test_sum_terms.py',
        'src/test_trib.py', 'src/tribonacci.py', 'sum_terms.pyc',
        'travis.yml', 'tribonacci.pyc'
    ]
