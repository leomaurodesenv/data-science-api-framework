# Data Science API Framework
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/Code-GitHub-yellow.svg)](https://github.com/leomaurodesenv/data-science-api-framework)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/ca9bfbcc15dc48eba5b5cd22dc8f1329)](https://www.codacy.com/manual/leomaurodesenv/data-science-api-framework?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=leomaurodesenv/data-science-api-framework&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.com/leomaurodesenv/data-science-api-framework.svg?branch=master)](https://travis-ci.com/leomaurodesenv/data-science-api-framework)
   
This repository is the basis for a fast, efficient and scalable python API structure for data scientists.   
This framework presents a continuous integration test using [Travis CI](https://travis-ci.com/), a [Docker](https://www.docker.com/) image to deploy your data science project, and, finally, a simple API Restful implementation to allow security access for everyone; facilitating the documentation, test, development, and deployment for production.  

Combing all these things, this framework provides an potential DataOps procedure for your project. "DataOps is an automated, process-oriented methodology, used by analytic and data teams, to improve the quality and reduce the cycle time of data analytics ... DataOps focuses on continuous delivery by leveraging on-demand IT resources and by automating test and deployment". [Wikipedia](https://en.wikipedia.org/wiki/DataOps).   

![Idea](img/main-idea.png)

---
## Start Coding
### Installation

Important links: [DockerHub](http://hub.docker.com/), [Documentation](https://docs.docker.com/).   

Each Operating System (OS) have its own steps.   
**Note**: Docker CE (Community Edition), Docker EE (Enterprise Edition).   

```shell
# build image
$ docker build -t ds-api .
# running container
$ docker run -it --rm --name ds-api-container -p 5050:80 ds-api
```

Done! You can access your API in http://localhost:5050/.   

### Coding your API

Create your endpoint logic (API), such as [app/endpoints/hello_world.py](app/endpoints/hello_world.py).   
Add the new endpoint to [app/main.py](app/main.py); that is it, just run.   

---
## Deep personalization

Useful personalizations:   
-   Add Python libraries for your API; see [requirements.txt](requirements.txt).
-   Add new API methods; see [app/main.py](app/main.py).
-   Improve the continuos integration tests; see [travis.yml](travis.yml).
-   Improve the Docker image; see [Dockerfile](Dockerfile).
-   Create an issue for any questions or suggestions!

---
## Also look ~

-   License [MIT](LICENSE)
-   Created by Leonardo Mauro ~ [leomaurodesenv](https://github.com/leomaurodesenv/)