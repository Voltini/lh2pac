# **Disclaimer:**
- This repository is a fork of the [lh2pac repository](https://gitlab.com/MatthiasDeLozzo/lh2pac/-/tree/modia2024?ref_type=heads).
- The delivrables are in the folder `livrables` please change directory to this folder after creating the virtual environment and installing the dependencies.
- The command to start the GUI is: `streamlit run ihm.py`
- All the code that realizes the project is in the jupyter notebook

# Before running the programs
### Create a virtual environment (only once)

In the directory `"lh2pac"`:

=== "Linux"

    ```
    python -m venv .venv
    source .venv/bin/activate
    pip install --editable .
    source .venv/bin/deactivate
    ```

=== "Windows"

    ```
    python -m venv .venv
    .venv\Scripts\activate.bat
    pip install --editable .
    .venv\Scripts\deactivate.bat
    ```

### Use your virtual environment in a Python console

In the directory `"lh2pac"`:

=== "Linux"

    ```
    source .venv/bin/activate
    ```

=== "Windows"

    ```
    .venv\Scripts\activate.bat
    ```

and use Python as usual.

### Compile the documentation

#### Compile each time you save a file (temporary doc)

=== "Linux"

    ```
    mkdocs serve
    ```

=== "Windows"

    ```
    mkdocs.exe serve
    ```

The documentation is generated and can be accessed at a local domain,
e.g. [http://127.0.0.1:8000](http://127.0.0.1:8000).

Then,
every time you save a file,
the documentation will be updated automatically.

#### Compile (permanent doc)

The previous command does not save the website;
to do so, use the following command.

=== "Linux"

    ```
    mkdocs build
    ```

=== "Windows"

    ```
    mkdocs.exe build
    ```

The LH2PAC adventure starts here!

# Project group:
### ModIA class of 2025:
- Baptiste Giraud
- Aymane Kssim
- Jonas Meyran
- Lucas Zuliani