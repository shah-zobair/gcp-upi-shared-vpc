def GenerateConfig(context):

    resources = [{
        'name': context.properties['infra_id'] + '-ingress-public-ip',
        'type': 'compute.v1.address',
        'properties': {
            'region': context.properties['region']
        }
    }, {
        'name': context.properties['infra_id'] + '-ingress-http-health-check',
        'type': 'compute.v1.httpHealthCheck',
        'properties': {
            'port': 32410,
            'requestPath': '/healthz'
        }
    }, {
        'name': context.properties['infra_id'] + '-ingress-target-pool',
        'type': 'compute.v1.targetPool',
        'properties': {
            'region': context.properties['region'],
            'healthChecks': ['$(ref.' + context.properties['infra_id'] + '-ingress-http-health-check.selfLink)'],
            'instances': []
        }
    }, {
        'name': context.properties['infra_id'] + '-ingress-forwarding-rule',
        'type': 'compute.v1.forwardingRule',
        'properties': {
            'region': context.properties['region'],
            'IPAddress': '$(ref.' + context.properties['infra_id'] + '-ingress-public-ip.selfLink)',
            'target': '$(ref.' + context.properties['infra_id'] + '-ingress-target-pool.selfLink)',
            'portRange': '80-443'
        }
    }]

    return {'resources': resources}
