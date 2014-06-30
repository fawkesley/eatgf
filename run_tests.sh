#!/bin/bash -e

THIS_SCRIPT=$0
THIS_DIR=$(dirname ${THIS_SCRIPT})


function nuke_pyc_files {
  find . -iname '*.pyc' -exec rm {} +
}

function run_pep8_style_checks {
    # F401: imported but unused
    flake8 \
        --ignore=F401 \
        --exclude='eatgf/apps/*/migrations/*.py,eatgf/settings/*.py' \
    .
}


function run_python_unit_tests {
    python manage.py test
}

nuke_pyc_files
run_pep8_style_checks
run_python_unit_tests
