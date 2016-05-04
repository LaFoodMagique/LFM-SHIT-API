#!/usr/bin/env sh

#
#
#

remove_migration() {
    rm -f ./*/migrations/0*_*.py
    echo 'Migration files are now removed.'
}

remove_db() {
    rm -f *.sqlite3
    echo 'DB files are now removed.'
}


#
#
#

remove_migration

remove_db
