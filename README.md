# A fresh take on ASReview's API

See `test/test_api.py` for the complete programming interface.

## Avoiding unintentional reexports with private module pattern

```shell
python3 -m venv venv
source venv/bin/activate
pip install --editable ./asreviewlib/[test]
python3
>>> import asreviewlib
>>> asreviewlib.demo_d  # works
>>> asreviewlib.demo_d.fun()
module demo/_demo.py imports built-in module 'sys': <module 'sys' (built-in)>
>>> dir(asreviewlib.demo_d)  # has fun, but not sys
Ctrl-D
pytest asreviewlib # all tests pass 
```

Let's change it so `asreviewlib` uses `fun` from `demo_f` instead of from `demo_d/_demo.py`:

- `asreviewlib.__init__.py` update `import` and `__all__`
- `tests.test_api.py` update references to `demo_f`.

```shell
python3 -m venv venv
source venv/bin/activate
pip install --editable ./asreviewlib/[test]
python3
>>> import asreviewlib
>>> asreviewlib.demo_f  # works
>>> asreviewlib.demo_f.fun()
module demo.py imports built-in module 'sys': <module 'sys' (built-in)>
>>> dir(asreviewlib.demo_f)  # has fun, as well as sys 
Ctrl-D
pytest asreviewlib # should fail with messages about sys
```


## entry_points

Not all `entry_points` map one-to-one to commands you can use on the command line, only `console_scripts` do:

```shell
rm -rf venv
python3 -m venv venv
source venv/bin/activate
python3
>>> from importlib.metadata import entry_points as entrypoints
>>> for k, entrypoints_list in entrypoints().items():
...     print(k)
...     for e in entrypoints_list:
...             print(f"    {e}")
... 
console_scripts
    EntryPoint(name='pip', value='pip._internal.cli.main:main', group='console_scripts')
    EntryPoint(name='pip3', value='pip._internal.cli.main:main', group='console_scripts')
    EntryPoint(name='pip3.10', value='pip._internal.cli.main:main', group='console_scripts')
distutils.commands
    EntryPoint(name='alias', value='setuptools.command.alias:alias', group='distutils.commands')
    EntryPoint(name='bdist_egg', value='setuptools.command.bdist_egg:bdist_egg', group='distutils.commands')
    EntryPoint(name='bdist_rpm', value='setuptools.command.bdist_rpm:bdist_rpm', group='distutils.commands')
    EntryPoint(name='build_clib', value='setuptools.command.build_clib:build_clib', group='distutils.commands')
    EntryPoint(name='build_ext', value='setuptools.command.build_ext:build_ext', group='distutils.commands')
    EntryPoint(name='build_py', value='setuptools.command.build_py:build_py', group='distutils.commands')
    EntryPoint(name='develop', value='setuptools.command.develop:develop', group='distutils.commands')
    EntryPoint(name='dist_info', value='setuptools.command.dist_info:dist_info', group='distutils.commands')
    EntryPoint(name='easy_install', value='setuptools.command.easy_install:easy_install', group='distutils.commands')
    EntryPoint(name='egg_info', value='setuptools.command.egg_info:egg_info', group='distutils.commands')
    EntryPoint(name='install', value='setuptools.command.install:install', group='distutils.commands')
    EntryPoint(name='install_egg_info', value='setuptools.command.install_egg_info:install_egg_info', group='distutils.commands')
    EntryPoint(name='install_lib', value='setuptools.command.install_lib:install_lib', group='distutils.commands')
    EntryPoint(name='install_scripts', value='setuptools.command.install_scripts:install_scripts', group='distutils.commands')
    EntryPoint(name='rotate', value='setuptools.command.rotate:rotate', group='distutils.commands')
    EntryPoint(name='saveopts', value='setuptools.command.saveopts:saveopts', group='distutils.commands')
    EntryPoint(name='sdist', value='setuptools.command.sdist:sdist', group='distutils.commands')
    EntryPoint(name='setopt', value='setuptools.command.setopt:setopt', group='distutils.commands')
    EntryPoint(name='test', value='setuptools.command.test:test', group='distutils.commands')
    EntryPoint(name='upload_docs', value='setuptools.command.upload_docs:upload_docs', group='distutils.commands')
distutils.setup_keywords
    EntryPoint(name='dependency_links', value='setuptools.dist:assert_string_list', group='distutils.setup_keywords')
    EntryPoint(name='eager_resources', value='setuptools.dist:assert_string_list', group='distutils.setup_keywords')
    EntryPoint(name='entry_points', value='setuptools.dist:check_entry_points', group='distutils.setup_keywords')
    EntryPoint(name='exclude_package_data', value='setuptools.dist:check_package_data', group='distutils.setup_keywords')
    EntryPoint(name='extras_require', value='setuptools.dist:check_extras', group='distutils.setup_keywords')
    EntryPoint(name='include_package_data', value='setuptools.dist:assert_bool', group='distutils.setup_keywords')
    EntryPoint(name='install_requires', value='setuptools.dist:check_requirements', group='distutils.setup_keywords')
    EntryPoint(name='namespace_packages', value='setuptools.dist:check_nsp', group='distutils.setup_keywords')
    EntryPoint(name='package_data', value='setuptools.dist:check_package_data', group='distutils.setup_keywords')
    EntryPoint(name='packages', value='setuptools.dist:check_packages', group='distutils.setup_keywords')
    EntryPoint(name='python_requires', value='setuptools.dist:check_specifier', group='distutils.setup_keywords')
    EntryPoint(name='setup_requires', value='setuptools.dist:check_requirements', group='distutils.setup_keywords')
    EntryPoint(name='test_loader', value='setuptools.dist:check_importable', group='distutils.setup_keywords')
    EntryPoint(name='test_runner', value='setuptools.dist:check_importable', group='distutils.setup_keywords')
    EntryPoint(name='test_suite', value='setuptools.dist:check_test_suite', group='distutils.setup_keywords')
    EntryPoint(name='tests_require', value='setuptools.dist:check_requirements', group='distutils.setup_keywords')
    EntryPoint(name='use_2to3', value='setuptools.dist:invalid_unless_false', group='distutils.setup_keywords')
    EntryPoint(name='zip_safe', value='setuptools.dist:assert_bool', group='distutils.setup_keywords')
egg_info.writers
    EntryPoint(name='PKG-INFO', value='setuptools.command.egg_info:write_pkg_info', group='egg_info.writers')
    EntryPoint(name='dependency_links.txt', value='setuptools.command.egg_info:overwrite_arg', group='egg_info.writers')
    EntryPoint(name='depends.txt', value='setuptools.command.egg_info:warn_depends_obsolete', group='egg_info.writers')
    EntryPoint(name='eager_resources.txt', value='setuptools.command.egg_info:overwrite_arg', group='egg_info.writers')
    EntryPoint(name='entry_points.txt', value='setuptools.command.egg_info:write_entries', group='egg_info.writers')
    EntryPoint(name='namespace_packages.txt', value='setuptools.command.egg_info:overwrite_arg', group='egg_info.writers')
    EntryPoint(name='requires.txt', value='setuptools.command.egg_info:write_requirements', group='egg_info.writers')
    EntryPoint(name='top_level.txt', value='setuptools.command.egg_info:write_toplevel_names', group='egg_info.writers')
setuptools.finalize_distribution_options
    EntryPoint(name='keywords', value='setuptools.dist:Distribution._finalize_setup_keywords', group='setuptools.finalize_distribution_options')
    EntryPoint(name='parent_finalize', value='setuptools.dist:_Distribution.finalize_options', group='setuptools.finalize_distribution_options')
```