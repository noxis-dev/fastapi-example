## Receipt-to-JSON API

This API accepts a receipt image URL or file, converts it into JSON, and returns it.

![Gyazo](https://gyazo.com/a3638fed38130d424b052605d3138cf5/raw)

## Implementation Considerations

Please refer to the [fastapi-best-practices](https://github.com/zhanymkanov/fastapi-best-practices) repository for implementing FastAPI best practices.

## Environment Setup
```
docker-compose up -d
```

### Remote Container
During development, it is recommended to use the Remote Container environment.
The VSCode extension is required.
![https://gyazo.com/7a96393b28b39a4066d5fb3a6e2d35ca](https://gyazo.com/7a96393b28b39a4066d5fb3a6e2d35ca/raw)

## Adding Libraries

```
docker-compose exec app poetry add library_name
```

## API Docs

- Swagger UI
http://localhost:8000/docs

- ReDoc
http://localhost:8000/redoc
## Azure AI Vision

> **Warning**: This is currently a preview version and may stop working.
Please update the code when the official release is available.

Refer to the [azure-ai-vision-sdk](https://github.com/Azure-Samples/azure-ai-vision-sdk) repository.
The provided SDK was unable to be installed, so direct HTTP requests are being used.

Refer to the [API documentation](https://centraluseuap.dev.cognitive.microsoft.com/docs/services/unified-vision-apis-public-preview-2023-02-01-preview/operations/61d65934cd35050c20f73ab6) for more details.

