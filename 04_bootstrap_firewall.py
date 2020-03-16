def GenerateConfig(context):

    resources = [{
        'name': context.properties['infra_id'] + '-bootstrap-in-ssh',
        'type': 'compute.v1.firewall',
        'properties': {
            'network': context.properties['cluster_network'],
            'allowed': [{
                'IPProtocol': 'tcp',
                'ports': ['22']
            }],
            'sourceRanges':  ['0.0.0.0/0'],
            'targetTags': [context.properties['infra_id'] + '-bootstrap']
        }
    }]

    return {'resources': resources}
