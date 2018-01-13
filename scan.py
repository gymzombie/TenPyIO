#!/usr/bin/env python3

# See Readme.md for details and instructions

# Import configuration settings
exec(open("./settings.default").read())
exec(open("./settings.local").read())

from tenable_io.client import TenableIOClient

client = TenableIOClient(access_key=tenable_access_key, secret_key=tenable_secret_key)
scan = client.scan_helper.create(name='Test Scan', text_targets='www.tax.virginia.gov', template='basic')
scan.launch().download('Test_Scan.pdf', scan.histories()[0].history_id)
