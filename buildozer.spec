[app]
title = MotorApp
package.name = motorapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.main = main.py
version = 0.1

requirements = python3,kivy,requests
orientation = portrait
fullscreen = 1
android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a
android.copy_libs = 1

# (str) Icon of the application
# icon.filename = %(source.dir)s/icon.png

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
