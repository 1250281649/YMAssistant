pyinstaller -F -D -w python/YMAssistant.py -i assets/pictures/icon.png --upx-dir=thirdparty/upx/upx.exe

robocopy ./assets/pictures dist/YMAssistant/assets/pictures
robocopy ./thirdparty/netron dist/YMAssistant/thirdparty/netron