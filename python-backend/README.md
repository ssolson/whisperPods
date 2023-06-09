Install whisper

```
pip install -U openai-whisper
```

On windows you need to install ffmpeg follow this guide:
https://phoenixnap.com/kb/ffmpeg-windows

To check that installation worked:

```
ffmpeg -version
```

Should return

> $ ffmpeg -version
> ffmpeg version 2023-04-26-git-e3143703e9-full_build-www.gyan.dev Copyright (c) 2000-2023 the FFmpeg developers
> built with gcc 12.2.0 (Rev10, Built by MSYS2 project)
> configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-libsnappy --enable-zlib --enable-librist --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-libbluray --enable-libcaca --enable-sdl2 --enable-libaribb24 --enable-libaribcaption --enable-libdav1d --enable-libdavs2 --enable-libuavs3d --enable-libzvbi --enable-librav1e --enable-libsvtav1 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxavs2 --enable-libxvid --enable-libaom --enable-libjxl --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-frei0r --enable-libfreetype --enable-libfribidi --enable-liblensfun --enable-libvidstab --enable-libvmaf --enable-libzimg
> --enable-amf --enable-cuda-llvm --enable-cuvid --enable-ffnvcodec --enable-nvdec --enable-nvenc --enable-d3d11va --enable-dxva2 --enable-libvpl --enable-libshaderc --enable-vulkan --enable-libplacebo --enable-opencl --enable-libcdio --enable-libgme --enable-libmodplug --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libshine --enable-libtheora --enable-libtwolame --enable-libvo-amrwbenc --enable-libcodec2 --enable-libilbc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-ladspa --enable-libbs2b --enable-libflite --enable-libmysofa --enable-librubberband --enable-libsoxr --enable-chromaprint
> libavutil 58. 6.100 / 58. 6.100
> libavcodec 60. 10.100 / 60. 10.100
> libavformat 60. 5.100 / 60. 5.100
> libavdevice 60. 2.100 / 60. 2.100
> libavfilter 9. 5.100 / 9. 5.100
> libswscale 7. 2.100 / 7. 2.100
> libswresample 4. 11.100 / 4. 11.100
> libpostproc 57. 2.100 / 57. 2.100

Finally you can install this package by running

```
cd python-backend
pip install -e .
```

Cool now you can run

```
python scripts/theDailyGwei.py --run
```

Which will request the podcast and print the transcript of a hardcoded episode to screen.
