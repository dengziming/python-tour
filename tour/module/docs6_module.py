import sys

print(sys.path)

print(dir())
print(__name__)

from . import docs6_test
from .. import hello
from ..hello import hello

docs6_test.test()
