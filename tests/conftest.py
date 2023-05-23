import pytest
import sys

'''We use fixtures as a convention to be passed to multiple test, like database connection etc
this fixture will be available to all the tests 
they help to avid all the boiler plate code for the test'''

#monkey patch is a build in fixture, it helps to overwrite the std out for tests 
# and once we are finished, the settings go back to default case or like before.
@pytest.fixture
def capture_stdout(monkeypatch):
    buffer = {"stdout": "", "write_calls": 0}

    def fake_write(s):
        buffer["stdout"] += s
        buffer["write_calls"] += 1

    monkeypatch.setattr(sys.stdout, 'write', fake_write)
    return buffer


@pytest.fixture(scope="session")
def db_conn():
    db = ...
    url = ...
    with db.connect(url) as conn:  # connection will be torn down after all tests finish
        yield conn