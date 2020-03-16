def GenerateConfig(context):

    resources = [{
        'name': context.properties['infra_id'] + '-ingress-health-checks',
        'type': 'compute.v1.firewall',
        'properties': {
            'network': context.properties['cluster_network'],
            'allowed': [{
                'IPProtocol': 'tcp',
                'ports': ['32410', '1936']
            }],
            'sourceRanges':  ['35.191.0.0/16', '209.85.152.0/22', '209.85.204.0/22', '130.211.0.0/22'],
            'targetTags': [context.properties['infra_id'] + '-master'],
            'targetTags': [context.properties['infra_id'] + '-worker']
        }
    }, {
        'name': context.properties['infra_id'] + '-ingress-router',
        'type': 'compute.v1.firewall',
        'properties': {
            'network': context.properties['cluster_network'],
            'allowed': [{
                'IPProtocol': 'tcp',
                'ports': ['80', '443']
            }],
            'sourceRanges':  ['0.0.0.0/0'],
            'targetTags': [context.properties['infra_id'] + '-master'],
            'targetTags': [context.properties['infra_id'] + '-worker']
        }
    }]

    return {'resources': resources}
