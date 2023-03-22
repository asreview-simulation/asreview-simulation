```shell
python3 -m venv venv
source venv/bin/activate
pip install --editable .
python3
```

```python
import asreview

dir(asreview)
```


link that describes how type checkers determine what is the public interface of a library: 
https://github.com/microsoft/pyright/blob/3ae66f24b0d5d884ae7219b15b5ccbf0e3e8d477/docs/typed-libraries.md#library-interface

Example package with typed public interface: https://github.com/ethanhs/pep-561
