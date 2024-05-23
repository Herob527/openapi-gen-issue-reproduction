# OpenAPI Generator Issue Reproduction

## Description

I had issue that when using recursive type (with ref) in OpenAPI, in typescript I was getting any type when it came to recursive element

Turned out I was using outdated generator (7.4.0 vs 7.6.0) and now it works
