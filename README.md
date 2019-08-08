# frames
This project takes video files (most common types) and splits them into frames using pachyderm.
Steps to run:
1. create a pachyderm repo with: pachctl create repo videos
2. add videos files to this repo with: pachctl put file videos@master:<name-of-file> -f <path-to-file>
3. create the pipeline with: pachctl create pipeline -f 
