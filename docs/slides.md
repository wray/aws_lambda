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
* Organizer of [AlexaRVA meetup](https://www.meetup.com/Alexa-User-Group/)



<!-- .slide: data-background-image="images/lambda.jpg" -->
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


<!-- .slide: data-background-image="images/lambda.jpg" -->
## How Much?
### Requests + cpu/memory usage
---
* First 1M Request Free per month
* $0.20 per 1M requests thereafter
<br />+
* First 400,000 GB-Seconds per month
* $0.00001667 for every GB-second thereafter


<!-- .slide: data-background-image="images/lambda.jpg" -->
## Essentially Free
### More on making it free-er
---
* If you have something getting hit more than 1M times a month
  * Working for an Enterprise
  * Or you have built something to monetize
* For personal exploration, effectively no cost.



<!-- .slide: data-background-image="images/console.jpg" -->
## Let's Build One
### Requires AWS account
---
* You can do this on a browser!


<!-- .slide: data-background-image="images/console.jpg" -->
* [AWS Console](https://console.aws.amazon.com)
* AWS CLI
  * `pip install awscli`
  * Configure local aws settings (key)
  * Setup input.txt: `{ "name":"Wray" }`
  * `aws lambda invoke --invocation-type RequestResponse --function-name myPyLamb --region us-east-1 --payload file://input.txt outfile.txt`



<!-- .slide: data-background-image="images/alexa.jpg" -->
## What is it good for?
### Alexa skills are a great way to get started
---
* You can do this on a browser!
* Publish a skill and get swag
* [Get Promotional Credits](https://developer.amazon.com/alexa-skills-kit/alexa-aws-credits)
* Does require an
[amazon developer account](https://developer.amazon.com)
* All kinds of templates/examples in [github.com](https://github.com/alexa)


## What is it good for?
### Parallel processing, wow!
---
* [PyWren](pywren.io) is cool
* Also requires awscli
* `pip install pywren`
* `pywren-setup`
* Essentially build a function to be run in parallel to achieve results
* Brute force string guess - divide and conquer, the string to guess


## What is it good for?
### Stateless APIs
---
* Trigger via an AWS API Gateway
* Easily build out RESTful CRUD
* Fits nicely with a modern JavaScript FE and a lightweight API layer
* We'll come back to this



<!-- .slide: data-background-image="images/travis.jpg" -->
## Dev Workflow
### Lambda CI/CD
---
* [TravisCI](http://travis-ci.org) is a great, no-cost solution
* Travis includes AWS targets including lambda
* 'Build' and package using transient docker images
* Check out the .travis.yml
* Can also deploy to pypi


## Dev Workflow
### Amazon SAM
---
* Create the pipeline
* Add a buildspec.yml for CodeBuild
  * Creates the cloudformation package
  * Zip up the lambda
* Define a lambda-sam.yaml for the lambda provision
  * SAM - Serverless Application Model  


## Local Dev
---
* Eclipse and Visual Studio supports some local testing capability
* serverless.com also supports this (but more JavaScript oriented)
* [AWS SAM Local](https://docs.aws.amazon.com/lambda/latest/dg/test-sam-local.html) provides a local lambda container to test locally



<!-- .slide: data-background-image="images/zappa.jpg" -->
## Best for last...
### Zappa!
---
* Instantly deploy your flask-app to lambda
* [Publish a Flask API via AWS API GW and lambda](https://github.com/wray/flask-restful-wsgi/tree/serverless)
* Create a virtualenv for your flask app and activate
* `pip install flask flask_restful zappa`
* `zappa init`
* `zappa deploy dev`
* `zappa tail`


<!-- .slide: data-background-image="images/zappa.jpg" -->
## Zappa is pretty cool
---
* Want to build a stateless API immediately available to millions?
* Create a simple flask app
  * Use your normal Python services local tools
  * Green Unicorn (gunicorn)
* Deploy via Zappa
  * Dependencies and project structure is packaged for you
  * AWS API GW is created and as the trigger for the flask app lambda



## Resources again
---
* console.aws.amazon.com
* github.com/alexa
* developer.amazon.com
* github.com/wray/aws_lambda
* github.com/wray/lambda-pipe
* github.com/wray/alexa_python (master and s3 branch)
* github.com/wray/flask-restful-wsgi
* www.zappa.io/
