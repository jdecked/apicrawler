from __future__ import unicode_literals

import urllib2, re

from django.db import models

# from tagging.fields import TagField
# from tagging.models import Tag
# from tagging.registry import register

from yaml import safe_load

class APIDefinition(models.Model):
    host = models.URLField()
    title = models.CharField(max_length=255)
    description = models.TextField(default='No description provided.')
    provider = models.CharField(max_length=255)

class APICrawler(object):
    def __init__(self, start_url):
        self.start_url = start_url

    @staticmethod
    def create_definition(fields):
        new_definition = APIDefinition()

        for field in fields:
            if field == 'tags':
                continue
            elif (field == 'x-providerName') and (fields[field]):
                setattr(new_definition, 'provider', fields[field])
            elif fields[field]:
                setattr(new_definition, field, fields[field])

        new_definition.save()

        # if fields['tags']:
        #     for tag in fields['tags']:
        #         try:
        #             Tag.objects.add_tag(new_definition, tag)
        #         except:
        #             pass

        new_definition.save()

    @staticmethod
    def parse_yaml(data, req_field):
        try:
            return data[req_field]
        except KeyError:
            try:
                return data['info'][req_field]
            except:
                pass

    @staticmethod
    def get_tags(data):
        try:
            tags = []
            for tag in data['tags']:
                tags.append(tag['name'])

            return tags
        except:
            pass

    def crawl(self):
        not_crawled = []
        req_fields = ['host', 'title', 'description', 'x-providerName']

        for url in re.findall('''href=["'](.[^"']+)["']''', urllib2.urlopen(self.start_url).read(), re.I):
            not_crawled.append(url)

        while not_crawled:
            current_url = urllib2.urlopen(urllib2.quote(not_crawled[0], safe=':/')).read()
            definitions = {field: None for field in req_fields}

            data = safe_load(current_url)

            for field in req_fields:
                definitions[field] = self.parse_yaml(data, field)

            # Tag implementation is really tanking performance right now, so it's disabled
            # Docs aren't very clear, better implementation to be found
            # definitions['tags'] = self.get_tags(data)

            self.create_definition(definitions)
            not_crawled.pop(0)

# register(APIDefinition)
