
[app]
title = FC Assistant AI
package.name = fcassistant
package.domain = org.fcassistant
source.dir = .
source.include_exts = py
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.permissions = INTERNET
android.api = 35
android.minapi = 23
android.archs = arm64-v8a
