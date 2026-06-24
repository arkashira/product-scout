import json
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class SignalData:
    popularity_score: float
    growth_rate: float
    category: str

class DataNormalizer:
    def __init__(self):
        self.cache = {}

    def normalize(self, signal_data):
        if signal_data.category not in self.cache:
            self.cache[signal_data.category] = {
                'popularity_score': [],
                'growth_rate': []
            }
        self.cache[signal_data.category]['popularity_score'].append(signal_data.popularity_score)
        self.cache[signal_data.category]['growth_rate'].append(signal_data.growth_rate)
        
        popularity_score_mean = sum(self.cache[signal_data.category]['popularity_score']) / len(self.cache[signal_data.category]['popularity_score'])
        growth_rate_mean = sum(self.cache[signal_data.category]['growth_rate']) / len(self.cache[signal_data.category]['growth_rate'])
        
        popularity_score_range = max(self.cache[signal_data.category]['popularity_score']) - min(self.cache[signal_data.category]['popularity_score'])
        growth_rate_range = max(self.cache[signal_data.category]['growth_rate']) - min(self.cache[signal_data.category]['growth_rate'])
        
        if popularity_score_range == 0:
            normalized_popularity_score = 0
        else:
            normalized_popularity_score = (signal_data.popularity_score - popularity_score_mean) / popularity_score_range
        
        if growth_rate_range == 0:
            normalized_growth_rate = 0
        else:
            normalized_growth_rate = (signal_data.growth_rate - growth_rate_mean) / growth_rate_range
        
        return {
            'popularity_score': normalized_popularity_score,
            'growth_rate': normalized_growth_rate,
            'category': signal_data.category
        }

    def cache_data(self, signal_data):
        if signal_data.category not in self.cache:
            self.cache[signal_data.category] = {
                'data': [],
                'timestamp': datetime.now()
            }
        self.cache[signal_data.category]['data'].append(signal_data)
        if (datetime.now() - self.cache[signal_data.category]['timestamp']).total_seconds() > 300:
            self.cache[signal_data.category]['timestamp'] = datetime.now()
            self.cache[signal_data.category]['data'] = []

    def get_cached_data(self, category):
        if category in self.cache and self.cache[category]['data']:
            return self.cache[category]['data']
        else:
            return None
