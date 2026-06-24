from data_normalizer import DataNormalizer, SignalData

def test_normalize():
    normalizer = DataNormalizer()
    signal_data = SignalData(10.0, 5.0, 'category1')
    normalized_data = normalizer.normalize(signal_data)
    assert normalized_data['category'] == 'category1'

def test_cache_data():
    normalizer = DataNormalizer()
    signal_data = SignalData(10.0, 5.0, 'category1')
    normalizer.cache_data(signal_data)
    cached_data = normalizer.get_cached_data('category1')
    assert cached_data is not None

def test_get_cached_data():
    normalizer = DataNormalizer()
    signal_data = SignalData(10.0, 5.0, 'category1')
    normalizer.cache_data(signal_data)
    cached_data = normalizer.get_cached_data('category1')
    assert len(cached_data) == 1

def test_normalize_edge_case():
    normalizer = DataNormalizer()
    signal_data = SignalData(0.0, 0.0, 'category1')
    normalized_data = normalizer.normalize(signal_data)
    assert normalized_data['category'] == 'category1'

def test_cache_data_edge_case():
    normalizer = DataNormalizer()
    signal_data = SignalData(10.0, 5.0, 'category1')
    normalizer.cache_data(signal_data)
    cached_data = normalizer.get_cached_data('category2')
    assert cached_data is None
