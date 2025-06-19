name: Build APK

on:
  push:
    branches:
      - main
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Install dependencies
      run: |
        sudo apt update
        sudo apt install -y python3-pip python3-setuptools git zip unzip openjdk-11-jdk
        pip3 install --upgrade cython==0.29.33 buildozer

    - name: Install Android SDK & NDK dependencies for Buildozer
      run: |
        buildozer android sdk

    - name: Build APK
      run: |
        buildozer -v android debug

    - name: Upload APK artifact
      uses: actions/upload-artifact@v3
      with:
        name: apk
        path: bin/*.apk
