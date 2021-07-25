import pytest
import os
import sys
import subprocess

solution_dirs = os.listdir('solutions')
for solution_dir in solution_dirs:
    print(f"Running tests for {solution_dir}")
    solution_abs_path = os.path.abspath(
        os.path.join(f"solutions", solution_dir))

    new_env = os.environ.copy()
    original_pythonpath = new_env.get("PYTHONPATH", "")
    new_env["PYTHONPATH"] = f"{solution_abs_path}:{original_pythonpath}"

    retcode = subprocess.call(
        ["pytest", "-q", "--no-summary", "--tb=no", "teacher_tests"], env=new_env)
    print(f"Done running tests for {solution_dir}")
