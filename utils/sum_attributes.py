#!/usr/bin/python
from json import json.load()


class BuildStatsTK(object):
	"""
	Description: A series of methods for working with the build_stats.json file
	Assumptions: Requires a path to the build_stats.json repo.
	Parameters:
	Author(s):
	Last Modified:
	"""
	def __init__

with open('build_stats.json') as data_file:
    data = json.load(data_file)

for item in data['GeocodedResearchReleases']['Level1']:
    print item['dataset_title']
   ....:     if item['dataset_title'] != 'TUFFChinaEcologicalHotSpots':
   ....:         sum+=item['
