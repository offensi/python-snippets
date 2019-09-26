#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# getGcpIpRanges - list all ipv4/ipv6 ranges reserved for Google Cloud Platform
# usage: pip install dnspython; python getGcpIprange.py
# wtm@offensi.com

import dns.resolver


def getGcpIpRanges(txtRecord):
    """ returns a list of _cloud-netblocksX TXT records to be queried """
    resolver = dns.resolver.Resolver()
    netblockRecords = []

    myAnswers = resolver.query(txtRecord, "TXT")

    for rdata in myAnswers:
        txtrecord = rdata.strings
        txtparts = txtrecord[0].split()

        if any("ip" in s for s in txtparts):
            for txt in txtparts:
                if "ip4" in txt:
                    ip = txt.split(':')[1]
                    print "ipv4 : {}".format(ip)
                if "ip6" in txt:
                    ip = txt.replace('ip6:', '')
                    print "ipv6 : {}".format(ip)
        else:
            for txt in txtparts:
                if "netblock" in txt:
                    netblockRecords.append(txt.split(':')[1])

            # recursive call
            for record in netblockRecords:
                getGcpIpRanges(record)


getGcpIpRanges("_cloud-netblocks.googleusercontent.com")  # first record
