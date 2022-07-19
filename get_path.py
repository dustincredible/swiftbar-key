import hid

# Update with the vendor_id and product_id for your device
l = hid.enumerate(65261,24688)
d = next(item for item in l if item['interface_number'] == 1)
p = d['path']
# Update this directory
f = open('/Users/dustin/swiftbar-key/path.log', 'wb')
f.write(p)
f.close()