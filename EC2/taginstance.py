import boto.ec2
conn=boto.ec2.connect_to_region("eu-east-1")
reservations = conn.get_all_instances()
for res in reservations:
    for inst in res.instances:
        if 'Name' in inst.tags:
            print "%s (%s) [%s]" % (inst.tags['Environment'], inst.id, inst.state)
        else:
            print "%s [%s]" % (inst.id, inst.state)