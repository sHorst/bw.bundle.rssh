defaults = {}

if node.has_bundle('apt'):
    defaults['apt'] = {
        'rush': {'installed': True},
    }
