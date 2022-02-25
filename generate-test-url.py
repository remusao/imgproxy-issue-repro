import base64
import hashlib
import hmac
import textwrap

IMGPROXY_KEY = bytes.fromhex("943b421c9eb07c830af81030552c86009268de4e532ba2ee2eab8247c6da0881")
IMGPROXY_SALT = bytes.fromhex("520f986b998545b4785e0defbc4f3c1203f22de2374a3d53cb7a7fe9fea309c5")
URL = "https://cdn.sstatic.net/Sites/stackoverflow/Img/favicon.ico?v=ec617d715196"


def main():
    encoded_url = (
        base64.urlsafe_b64encode(URL.encode("utf-8")).rstrip(b"=").decode()
    )
    encoded_url = "/".join(textwrap.wrap(encoded_url, 16))
    path = "/rs:{resize}:{width}:{height}:{enlarge}/g:{gravity}/{encoded_url}.png".format(
        encoded_url=encoded_url,
        resize="fill",
        width=32,
        height=32,
        gravity="no",
        enlarge=1,
    ).encode()
    digest = hmac.new(
        IMGPROXY_KEY, msg=IMGPROXY_SALT + path, digestmod=hashlib.sha256
    ).digest()
    protection = base64.urlsafe_b64encode(digest).rstrip(b"=")
    url = b"%s%s" % (protection, path)
    print(f"http://localhost:8000/{url.decode()}")


if __name__ == "__main__":
    main()
