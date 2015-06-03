"""Utility for loading SQLAlchemy model classes and friends. Please see
inbox/models/__init__.py for the explanation of why this is necessary."""


def load_models():
    from inbox.models.account import Account
    from inbox.models.base import MailSyncBase
    from inbox.models.action_log import ActionLog
    from inbox.models.block import Block, Part
    from inbox.models.contact import MessageContactAssociation, Contact
    from inbox.models.calendar import Calendar
    from inbox.models.event import Event
    from inbox.models.folder import Folder
    from inbox.models.message import Message
    from inbox.models.namespace import Namespace
    from inbox.models.search import SearchIndexCursor
    from inbox.models.secret import Secret
    from inbox.models.tag import Tag
    from inbox.models.thread import Thread
    from inbox.models.transaction import Transaction
    from inbox.models.when import When, Time, TimeSpan, Date, DateSpan
    from inbox.models.label import Label
    from inbox.models.category import Category
    exports = [Account, MailSyncBase, ActionLog, Block, Part,
               MessageContactAssociation, Contact, Calendar, Event, Folder,
               Message, Namespace, SearchIndexCursor, Secret, Tag,
               Thread, Transaction, When, Time, TimeSpan, Date, DateSpan,
               Label, Category]
    return exports
