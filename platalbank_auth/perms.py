#!/usr/bin/python3
# -*- encoding: utf-8 -*-

def may_access(user, legalperson):
    """whether a user may read the details of legalperson's accounts.
roughly read-only permissions
"""
    # TODO: LDAP stuff
    return True

def may_modify(user, legalperson):
    """whether a user can add new trasactions to events owned by legalperson.
roughly read-write permissions
"""
    # TODO: LDAP stuff
    return True

