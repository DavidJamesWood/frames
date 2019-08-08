# frames
This project takes video files (most common types) and splits them into frames using pachyderm.
Steps to run:
1. create a pachyderm repo with: pachctl create repo videos
2. add videos files to this repo with: pachctl put file videos@master:<name-of-file> -f <path-to-file>
3. create the pipeline with: pachctl create pipeline -f https://raw.githubusercontent.com/DavidJamesWood/frames/master/frames.json
  
Blog Header: Data Scientists/Engineers, Here's how to increase your value with open source pachyderm!

  Creating predictive models is no longer a rare skill with the advent of data science "get smart quick" courses. So how can you stand out above the other data professionals? The answer is to incorporate stability, auditability, and simple scalability into your AI pipelines. These virtues are of high importance to the modern day corporation, but are after thoughts by most data science practitioners. Let's run through how pachyderm enables the three virtues.
1. Stability: 
2. Auditability:
3. Simple Scalability:
