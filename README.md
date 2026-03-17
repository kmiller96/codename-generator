# Deterministic Codename Generator

Generates a codename, deterministically, for a given input.

## Why?

In my work, I often like to alias clients. That way, if I accidentally share my
screen where my client data is (e.g. Notion) it's less likely I'll leak sensitive
information such as who I work for.

Usually, my aliases link back to their name in some way. For example, if one of
my clients was [Suez](https://www.suez.com/en/waste) (for reference, they aren't)
then I might alias them as `CN: Canal` in reference to the Suez Canal.

This project doesn't aim to achieve such logical mappings. All codenames are
completely arbitrary.

## Deployment

You can run this server using fastapi:

```bash
uv run fastapi run app/main.py
```

In practice, I would recommend you deploy this as a docker container. This
service's dockerfile can be found in this repo. If you wish to run this service
via docker:

```bash
docker build -t codename-generator .
docker run --rm -it -p 8000:80 codename-generator
```

## Development Quickstart

If you wish to poke around locally with this service, the easiest way is to do
this via fastapi's development server:

```bash
uv run fastapi dev app/main.py
```

## TODO

- [ ] Deploy this on to my public server as a public prototype.
- [ ] Use an embedding model to find the closest word to an input?
