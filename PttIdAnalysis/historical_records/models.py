# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

class Article(DjangoCassandraModel):
    id = columns.UUID(primary_key=True, default=uuid.uuid4())
    author = columns.Text(index=True, required=True)
    title = columns.Text(required=True)
    posted_time = columns.DateTime(required=True)
    url = columns.Text(required=True)
    commenter = columns.Text(index=True, required=False)
    comments = columns.Text(required=False)

