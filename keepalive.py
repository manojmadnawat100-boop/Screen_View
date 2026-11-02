name: Keep Streamlit App Awake

on:
  schedule:
    - cron: "0 */4 * * *"
  workflow_dispatch:

jobs:
  wake:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install selenium
      - run: python keepalive.py
