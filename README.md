# Holmium Demo

Refer to the [article here](http://lifeinvistaprint.com/techblog/unit-testing-holmium-page-objects/).

## Setup

* Install Firefox
* Install `Python 2.7` and `pip`
    * **On OSX**

            sudo easy_install pip

    * **On Windows**
      * Download and install [python 2.7](https://www.python.org/download/releases/2.7.7/)
      * Install `pip`
          * Download and save [get-pip.py](https://raw.github.com/pypa/pip/master/contrib/get-pip.py) as `get-pip.py`
          * `python get-pip.py`
          * Add `C:\Python27\Scripts` to PATH

* Using `pip` install Selenium, nostests and Holmium:

        pip install selenium nose holmium.core
* Clone this repo and navigate to that folder

## Execution

    nosetests vista_test.py --with-holmium --holmium-browser=firefox --holmium-environment=http://vistaprint.com
