# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

class Article(DjangoCassandraModel):
    id = columns.UUID(primary_key=True, default=uuid.uuid4())
    author = columns.Text(index=True, required=False)
    title = columns.Text(required=False)
    posted_time = columns.DateTime()

class Comment(DjangoCassandraModel):
    id = columns.Integer(primary_key=True, default=0)