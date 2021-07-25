# testor - Running the same pytests tests for many student solutions

This is a quick demo project of how to run the same tests against many
different solutions. It iterates through all solution directories. For each
directory it adds the directory to the `PYTHONPATH` variable before executing
pytest. This way the import in the pytest always imports from the correct solution.

## How to use

* write tests in files in teacher_tests
* each student creates a directory with a file called `exercise.py`. Any function in this file can be imported by the tests.
* install pytest using `pip3 install pytest`
* run the tests using `python3 run_tests.py`
