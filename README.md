## Receipt-to-JSON API

This API accepts a receipt image URL or file, converts it into JSON, and returns it.

![Gyazo](https://gyazo.com/644e711aece3a8440464bfa96a0457ba/raw)

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

This allows you to run Python and execute libraries within the Docker environment.
Once you open the project root folder in VSCode, a pop-up will appear in the lower right corner. Click on it to reopen the project.
Alternatively, you can open the menu from the lower left corner >< icon and choose "Connect to Container".
During the initial connection, it may take some time to install Pylance, and errors may occur. If that happens, relaunch it again.

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

