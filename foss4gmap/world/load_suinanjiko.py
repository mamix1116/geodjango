import os
from django.contrib.gis.utils import LayerMapping
from world.models import Suinanjiko

# Modelとファイルのカラムのマッピング
mapping = {
    'no' : 'no',
    'ym' : 'ym',
    'pref' : 'pref',
    'river' : 'river',
    'jiko' : 'jiko',
    'accurate' : 'accurate',
    'geom' : 'POINT',
}

# ファイルパス
geojson_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'suinanjiko.geojson'))

# 実行
def run(verbose=True):
    lm = LayerMapping(Suinanjiko, geojson_file, mapping, transform=False, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
