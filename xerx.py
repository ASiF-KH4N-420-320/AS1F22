import platform
b = platform.architecture()[0]
if b == '64bit':
    import xerxx
elif b == '32bit':
    import xerxx
