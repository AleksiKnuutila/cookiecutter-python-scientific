#!/usr/bin/env bash


echo "Creating a virtual environment"
python3 -m venv venv
source venv/bin/activate
if [[ $? != 0 ]]
then
    exit 1
fi
pip install -r requirements.txt
pip install -e .

echo
echo "A virtual environment venv with the required packages has been created in the project's root folder."
