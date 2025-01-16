# Recipe API

## Description

This is a simple recipe API built with Django and Django Rest Framework.

## Features

### API

- User API
- Authentication (token based)
- Recipe API
- Tag API
- Ingredient API
- Recipe Image API
- Implement filtering

### CI/CD
- Dockerize app
- GitHub Actions (Linting, Testing)
- Deploy to AWS

### Pre-commit

#### Installation
Install pre-commit hooks.
```sh
pre-commit install
```

Install pre-commit hooks for commit-msg.
```sh
pre-commit install --hook-type commit-msg
```

#### Usage

Use `git commit` command directly, it will trigger pre-commit hooks.

or

```sh
pre-commit run --all-files
```
