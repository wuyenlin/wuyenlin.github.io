import os

dirs = os.listdir('./')

for file in dirs:
    print(file)
    os.system('ffmpeg -i {} -vf "transpose=0" ../{}'.format(file, file))