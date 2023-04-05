def check_star_exports(pkgname, actual_exports, expected_exports, exempt="check_star_exports"):
    for _item in actual_exports:
        if _item == exempt:
            continue
        if not _item.endswith('__'):
            assert _item in expected_exports, f"Named export '{_item}' missing from __all__ in '{pkgname}'"
    for _item in expected_exports:
        assert _item in actual_exports, f"__all__ includes unknown item '{_item}' in '{pkgname}'"
