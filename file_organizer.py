# import essential modules
from pathlib import Path
import shutil
import os
# set directories
directory_path = Path.home() / "Downloads"
archives = directory_path / "archives"
videos = directory_path / "videos"
photos = directory_path / "photos"
executibles = directory_path / "executibles"
images = directory_path / "images"
trash = directory_path / "trash"
archive = ('.rar', '.iso', '.zip', '.torrent')
video = ('.mp4', '.mov', '.avi', '.mkv')
image = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
executables = ('.exe', '.msi', '.bat', '.sh', '.AppImage,','.jar')
trashes = ('.aria2',)
# set tuples for extensions
archive_files = []
video_files = []
image_files = []
executible_files = []
trash_files = []
# index files, add them to a tuple
print('indexing all files')
for file in directory_path.glob('*'):
    if file.is_file():
        if file.suffix in archive:
            archive_files.append(str(file))
        if file.suffix in video:
            video_files.append(str(file))
        if file.suffix in image:
            image_files.append(str(file))
        if file.suffix in executables:
            executible_files.append(str(file))
        if file.suffix in trashes:
            trash_files.append(str(file))
print('creating folders for organization of files')
archives.mkdir(parents=True, exist_ok=True)
videos.mkdir(parents=True, exist_ok=True)
photos.mkdir(parents=True, exist_ok=True)
executibles.mkdir(parents=True, exist_ok=True)
images.mkdir(parents=True, exist_ok=True)
trash.mkdir(parents=True, exist_ok=True)
# move files to the respective areas
print('moving files')
print('moving archive files')
for archivesrc in archive_files:
        shutil.move(archivesrc, archives)
print('moving video files')
for videosrc in video_files:
        shutil.move(videosrc, videos)
print('moving image files')
for imagesrc in image_files:
        shutil.move(imagesrc, images)
print('moving application files')
for executiblessrc in executible_files:
        shutil.move(executiblessrc, executibles)
for trashsrc in trash_files:
        shutil.move(trashsrc, trash)
print('done, exiting now')
