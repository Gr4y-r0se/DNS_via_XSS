# DNS_via_XSS
A toolkit to exfiltrate data via DNS


## Install

```bash
git clone https://github.com/Gr4y-r0se/DNS_via_XSS.git
```

## Usage

Use the payload from `payload.js` with your own [app.interactsh.com](https://app.interactsh.com) domain in. Monitor for DNS interactions

Then, use `parser.py` to reform your cookie like so:
```bash
python app.py /path/to/file.json
```

This will then print your exfiltrated token

## Blog

I wrote a blog on this and why I came up with it. Have a read of it [here](https://www.linkedin.com/pulse/quiet-thief-liam-follin-chcsp-fnxie/).
