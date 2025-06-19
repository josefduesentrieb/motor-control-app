[app]
title = MotorApp
package.name = motorapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,requests
orientation = portrait
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a
# (str) Supported orientation (one of: landscape, sensorLandscape, portrait or all)
# orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
# Supported permissions such as 'INTERNET', 'ACCESS_FINE_LOCATION', etc.
android.permissions = INTERNET

# (str) Package identifier
package.domain = org.example

# (str) Entry point, defaults to main.py
source.main = main.py

# (str) Icon of the application
# icon.filename = %(source.dir)s/icon.png

# (list) Supported architectures
android.archs = armeabi-v7a, arm64-v8a

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android API to use
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (bool) Copy library instead of making a libpymodules.so
# This can avoid certain issues on Android 11+ with restrictions
android.copy_libs = 1

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# android.add_jars = libs/somejar.jar

# (str) Custom source folders for requirements
# (Separate multiple paths with commas)
# requirements.source.kivy = ../kivy

# (bool) Enables TouchRing support for supported devices
# android.touchring = 1

[buildozer]
log_level = 2
warn_on_root = 1
