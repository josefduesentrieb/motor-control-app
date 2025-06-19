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
android.build_tools_version = 36.0.0
android.ndk = 25.2.9519653
android.minapi = 21
android.archs = armeabi-v7a, arm64-v8a
android.copy_libs = 1

# Uncomment and set if you have an icon or presplash
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/data/presplash.png

[buildozer]
log_level = 2
warn_on_root = 1
