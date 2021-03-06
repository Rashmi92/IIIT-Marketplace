# -*- coding: utf-8 -*-

db=DAL('sqlite://IIITMarketDB.sqlite')

db.define_table('register_user',
                Field('user_name', 'string',requires=IS_NOT_EMPTY()),
                Field('email_id', 'string',requires=IS_EMAIL()),
                Field('alt_email_id', 'string',requires=IS_EMAIL()),
                Field('contact_no', 'integer',requires=IS_NOT_EMPTY()),
                Field('user_img','upload'),
                Field('address', 'text',requires=IS_NOT_EMPTY()))

db.define_table('advertise',
                Field('add_id','integer',),
                Field('item_name','string',requires=IS_NOT_EMPTY()),
                Field('category','string',requires=IS_NOT_EMPTY()),
                Field('user_name','string',requires=IS_NOT_EMPTY()),
                Field('type','string',requires=IS_NOT_EMPTY()),
                Field('status','string',requires=IS_NOT_EMPTY()),
                Field('post_date','date',requires=IS_NOT_EMPTY()),
                Field('ppl_bid','integer',default=0),
                Field('item_img','upload'))

from gluon.tools import Auth, Service, PluginManager

auth = Auth(db)
service = Service()
plugins = PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.janrain_account import use_janrain
use_janrain(auth, filename='private/janrain.key')

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
