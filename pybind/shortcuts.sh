alias pre="rm -rf build/ dist/ prebuilt/ *.egg-info/ && STORE_LIB=ON python -m build --wheel"
alias inst="pre && USE_PREBUILT=ON python -m build --wheel && pip install dist/tobi-1.0.0-cp312-cp312-linux_x86_64.whl --force-reinstall"

alias sdist="pre && USE_PREBUILT=ON python -m build --sdist && cd dist && tar -xf tobi-1.0.0.tar.gz && cd tobi-1.0.0 && USE_PREBUILT=ON pip install . --force-reinstall"