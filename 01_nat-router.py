def GenerateConfig(context):

    resources = [{
        'name': context.properties['infra_id'] + '-master-nat-ip',
        'type': 'compute.v1.address',
        'properties': {
            'region': context.properties['region']
        }
    }, {
        'name': context.properties['infra_id'] + '-worker-nat-ip',
        'type': 'compute.v1.address',
        'properties': {
            'region': context.properties['region']
        }
    }, {
        'name': context.properties['infra_id'] + '-router',
        'type': 'compute.v1.router',
        'properties': {
            'region': context.properties['region'],
            'network': context.properties['network'],
            'nats': [{
                'name': context.properties['infra_id'] + '-nat-master',
                'natIpAllocateOption': 'MANUAL_ONLY',
                'natIps': ['$(ref.' + context.properties['infra_id'] + '-master-nat-ip.selfLink)'],
                'minPortsPerVm': 7168,
                'sourceSubnetworkIpRangesToNat': 'LIST_OF_SUBNETWORKS',
                'subnetworks': [{
                    'name': context.properties['master-subnet'],
                    'sourceIpRangesToNat': ['ALL_IP_RANGES']
                }]
            }, {
                'name': context.properties['infra_id'] + '-nat-worker',
                'natIpAllocateOption': 'MANUAL_ONLY',
                'natIps': ['$(ref.' + context.properties['infra_id'] + '-worker-nat-ip.selfLink)'],
                'minPortsPerVm': 128,
                'sourceSubnetworkIpRangesToNat': 'LIST_OF_SUBNETWORKS',
                'subnetworks': [{
                    'name': context.properties['worker-subnet'],
                    'sourceIpRangesToNat': ['ALL_IP_RANGES']
                }]
            }]
        }
    }]

    return {'resources': resources}

