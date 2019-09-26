# python-snippets
Collection of small pieces of code i wrote that might be of use to others

### getGcpIpRanges.py
Google publishes all the IP ranges that are in use by the Google Cloud Platform in a SPF record on cloud-netblocks.googleusercontent.com. This script queries all records in a recursive manner to obtain the current ipv4 and ipv6 adresses (also see https://cloud.google.com/compute/docs/faq)

Usage: 
git clone https://github.com/offensi/python-snippets
pip install dnspython
python getGcpIpRanges.py

Output: 
ipv4 : 8.34.208.0/20
ipv4 : 8.35.192.0/21
ipv4 : 8.35.200.0/23
ipv4 : 108.59.80.0/20
ipv6 : 2600:1900::/35
etcetera. 


#### Contact

- e-mail : wtm@offensi.com
- website: https://offensi.com
- twitter: https://twitter.com/wtm_offensi
