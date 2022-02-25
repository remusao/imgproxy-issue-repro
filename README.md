# 

Generate repro URL:
```bash
$ python generate-test-url.py
```

This should output:
```
http://localhost:8000/fSeKiHqtklTyA0CDo_BkvOLPq2-r08PzzpfBjWO3lfs/rs:fill:32:32:1/g:no/aHR0cHM6Ly9jZG4u/c3N0YXRpYy5uZXQv/U2l0ZXMvc3RhY2tv/dmVyZmxvdy9JbWcv/ZmF2aWNvbi5pY28_/dj1lYzYxN2Q3MTUx/OTY.png
```

Working version (v3.0.0.beta1):
```bash
$ VERSION=beta1 docker-compose up --build
```

Visiting the above URL in this version should return: ![](./favicon-working.webp)

Broken version (v3.0.0.beta2):
```bash
$ VERSION=beta2 docker-compose up --build
```

Visiting the above URL in this version should return: ![](./favicon-broken.webp)
