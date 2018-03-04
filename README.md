# anonymizer-nginx-proxy

[![Travis](https://travis-ci.org/vitorbaptista/anonymizer-nginx-proxy.svg?branch=master)](https://travis-ci.org/vitorbaptista/anonymizer-nginx-proxy)

anonymizer-nginx-proxy extends [jwilder/nginx-proxy][nginx-proxy] removing all
user-identifiable headers before passing on the request.

## Motivation

When building a service that requires users to be anonymous, we need to avoid
saving user's identifiable information in the logs. If you control the
webserver configuration, this is relatively easy, you just need to disable the
logs. However, you're out of luck if you can't change the webserver
configuration, for example when you're using Heroku or other PaaS platform.

In that case, you need to either migrate to another platform, or add a proxy in
front of your app to remove the user-identifiable information. This is the goal
of this project.

## Usage

This project only adds some extra configuration to nginx, so all usage
instructions from [jwilder/nginx-proxy][nginx-proxy] applies here. See their
documentation for more information. 

[nginx-proxy]: https://github.com/jwilder/nginx-proxy
