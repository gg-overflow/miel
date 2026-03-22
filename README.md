
#### normalize
for file in *.mp3; do
  ffmpeg -i "$file" -af loudnorm=I=-16:TP=-1.5:LRA=11 "normalized_${file}"
done

#### build
python3 build.py