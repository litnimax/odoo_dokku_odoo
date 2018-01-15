#!/usr/bin/env python3

import logging
logging.basicConfig(level=logging.INFO)
import re
import os
import sys

# Some odoo args are used with _, some with -, like --db-filter and db_name.
keep_args = ['db_user', 'db_host', 'db_port',  'db_password', 
             'db_sslmode', 'db_maxconn', 'pg_path']

# Check env vars and transform them into command line args
odoo_env = filter(lambda a: a.startswith('ODOO_ARG'), os.environ.keys())
odoo_args = []
for arg in odoo_env:
    cast_arg = arg.replace('ODOO_ARG_', '').lower()
    if cast_arg not in keep_args:
        # Replace _ with -
        cast_arg = cast_arg.replace('_', '-')
    val =os.environ.get(arg)
    odoo_args.append('--{}={}'.format(cast_arg, val) if len(os.environ.get(arg)) \
        else '--{}'.format(cast_arg)
    )

# Start default odoo entrypoint
if len(sys.argv) == 1:
    logging.error('You must call entrypoint.py with some args.')
    sys.exit(1)

# Default cmd 
if sys.argv[1] == 'odoo':
    odoo_args.extend(sys.argv[2:])
    logging.info('Starting: odoo {}'.format(' '.join(odoo_args)))
    os.execvp('/usr/bin/odoo', [' '] + odoo_args)

else:
    logging.info('Starting {}.'.format(sys.argv))
    os.execvp(sys.argv[1], sys.argv[1:])

