mocks for an endpoint listening for messages from the repository frontend/metadata store (aka - dataverse) and async process that will send messages to a dataverse endpoint.

the dataverse endpoint is also mocked here (for development; jenkins uses this as well).
the tests for the mock dataverse endpoint aren't run from jenkins - installing the requirements and `nosetest -v -d` didn't seem like it was worth the overhead.

---
- `virtualenv rsal_mock` # if needed
- `source rsal_mock/bin/activate`
- `cd $RSAL_DIR/mock; pip install -r requirements.txt`
- update `pub.sh` if necessary (where `DVAPIKEY` is from if not `.bashrc`, and set dataverse host
- `./dev.sh` ; mock server will listen on port 5050 (unless changed)

