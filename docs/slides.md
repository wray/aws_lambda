<!-- .slide: data-background-image="images/pyinclouds.jpeg" style="color:black" -->
### Python in the Clouds <!-- .element: style="color:black" -->
---

Brought to you by Wray Mills
February 7, 2018
<br /><br />
Powered by PyRVA



<!-- .slide: data-background-image="images/family.jpg" -->
### About Me
#### Long time Python advocate
---
* A wife and 3 girls (9,11,13)
* In IT over 20 years
* Python for 25 years
* Consultant at CapTech Consulting
* Owner at [Tech Em Studios](http://techemstudios.com)
* Owner at [Wrayesian LLC](http://wrayesian.com)



### What is AWS Lambda?
---
* Run Python in AWS's cloud
* Serverless
  * "No" infrastructure
  * 3008MB(mem) - 512MB(/tmp) - 300seconds
* Highly Available
  * Have your Python code immediately available for millions to use
  * 1,000 max concurrent lambdas
* Microsoft Functions / Google Cloud Functions


## How Much?
### Requests + cpu/memory usage
---
* First 1M Request Free per month
* $0.20 per 1M requests thereafter
<br />+
* First 400,000 GB-Seconds per month
* $0.00001667 for every GB-second thereafter


## Essentially Free
### More on making it free-er
---
* If you have something getting hit more than 1M times a month
  * Working for an Enterprise
  * Or you have built something to monetize
* For personal exploration, effectively no cost.



## Let's Build One
### Requires AWS account
---
* You can do this on a browser!


* [AWS Console](https://console.aws.amazon.com)
* AWS CLI
  * `pip install awscli`
  * Configure local aws settings (key)
  * Setup input.txt: `{ "name":"Wray" }`
  * `aws lambda invoke --invocation-type RequestResponse --function-name myPyLamb --region us-east-1 --payload file://input.txt outfile.txt`



## What is it good for?
### Alexa skills are a great way to get started
---
* You can do this on a browser!
* Publish a skill and get swag
* [Get Promotional Credits](https://developer.amazon.com/alexa-skills-kit/alexa-aws-credits)
* Does require an [amazon developer account](https://developer.amazon.com)


## What is it good for?
### Parallel processing, wow!
---
* [PyWren](pywren.io) is cool
* Also requires awscli
* `pip install pywren`
* `pywren-setup`
* Essentially build a function to be run in parallel to achieve results
* Brute force string guess - divide and conquer, the string to guess



## What about writing functions locally?
### Uploading to the browser is kind of a pain
---
* [TravisCI](http://travis-ci.org) is a great, no-cost way to do lambda CI/CD
* Travis understands AWS deployments, including lambda
* 'Build' and package using transient docker images
* Check out the .travis.yml
* Still my preferred deployment since Travis can also deploy to pypi


## Slightly more complex, but Enterprise-ready
### Amazon provides a template to provision and update lambdas
---
* Create the pipeline
* Add a buildspec.yml for CodeBuild
  * Creates the cloudformation package
  * Zip up the lambda
* Define a lambda-sam.yaml for the lambda provision
  * SAM - Serverless Application Model  


## Environments for local testing
### Some IDEs and also AWS allows local testing
---
* Eclipse and Visual Studio supports some local testing capability
* serverless.com also supports this (but more JavaScript oriented)
* [AWS SAM Local](https://docs.aws.amazon.com/lambda/latest/dg/test-sam-local.html) provides a local lambda container to test locally



## Best for last...
### Zappa!
---
* Instantly deploy your flask-app to lambda
* Publish a Flask API via AWS API GW and lambda
* 
