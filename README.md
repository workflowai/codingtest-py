# Python Coding test

Boilerplate to serve as a base for a backend python coding test

## Usage

```sh
# Create a virtual env
python -m venv .venv
source .venv/bin/activate
# Install dependencies
make install
# Run api in auto reload mode
make run
```

VSCode configuration is provided as a start.

Important libraries are:

- pydantic, a data validation library (similar to dataclasses) https://docs.pydantic.dev/latest/
- fastapi, an API framework https://fastapi.tiangolo.com/

### LiveShare Extension (Optional)

If you use VSCode, you can optionally add the live share
extension so we can collaborate during the session.
