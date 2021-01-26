defaults = {}

if node.has_bundle('apt'):
    defaults['apt'] = {
        'rssh': {'installed': True},
    }
