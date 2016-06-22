def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('registration','/registration')
    config.add_route('loginin','/loginin')
    config.add_route('warehouse','/warehouse')
    config.add_route('lobby','/lobby')
    
